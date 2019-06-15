import json
from django.core import exceptions
from django.http import JsonResponse
from django.views import View
from . import serialiser, responses

__all__ = ['APIModelView']

class APIView(View):
    http_method_names = ['get', 'post', 'delete']

    def dispatch(self, request, *args, **kwargs):
        try:
            response = super().dispatch(request, *args, **kwargs)
        except responses.APIException as e:
            response = e.response
        # except Exception as e:
        #     response = responses.UNEXPECTED_ERROR(e)
        return JsonResponse(response, encoder=serialiser.APIJSONEncoder)

    def http_method_not_allowed(self, request, *args, **kwargs):
        return responses.METHOD_NOT_ALLOWED(request.method, request.path)

class APIModelView(APIView):
    model = None  # Override

    def _getObject(self, **kwargs):
        if self.model is None:
            raise responses.BadAPIException()
        model = self.model
        try:
            return model.objects.get(**kwargs)
        except model.DoesNotExist:
            raise responses.NotFoundException(model, **kwargs)
        except model.MultipleObjectsReturns:
            raise responses.BadAPIException()
        except exceptions.FieldError:
            raise responses.BadAPIException()

    def get(self, request, **kwargs):
        obj = self._getObject(**kwargs)
        return responses.OK(obj)

    def post(self, request, **kwargs):
        try:
            fields = json.loads(request.body)
        except json.JSONDecodeError:
            return responses.BAD_REQUEST(message='Request body is not valid JSON.')
        try:
            obj = self._getObject(**kwargs)
        except responses.NotFoundException:
            # Create new object
            fields.update(kwargs)
            try:
                obj = self.model(**fields)
            except TypeError:
                return responses.BAD_REQUEST(message=f'Request contained invalid fields for model {self.model}.')
            obj.save()
            return responses.OK(obj, message='Object created.')
        else:
            # Edit existing object
            for key, value in list(fields.items()):
                if hasattr(obj, key):  # Doesn't deal with relationship fields yet
                    setattr(obj, key, value)
                    del fields[key]
            if fields:  # This is now any invalid fields
                return responses.BAD_REQUEST(fields, message='Request contained invalid fields.')
            obj.save()
            return responses.OK(obj, message='Object successfully edited.')


    def delete(self, request, **kwargs):
        obj = self._getObject(**kwargs)
        obj.delete()
        return responses.OK(obj)

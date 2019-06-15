import json
from django.db import models
from django.forms import model_to_dict

# All this is really only temporary
class APIJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, models.Model):
            return model_to_dict(obj)
        return super().default(obj)

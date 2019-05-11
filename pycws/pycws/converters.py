class LangCodeConverter:
    regex = r'[a-z]{3,6}'

    def to_python(self, value):
        return value

    def to_url(self, value):
        return value

class UserIDConverter:
    regex = r''

    def to_python(self, value):
        return value

    def to_url(self, value):
        return value

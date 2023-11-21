class LanguageMixin:
    _language = 'EN'  # Язык по умолчанию

    @property
    def language(self):
        return self._language

    @language.setter
    def language(self, value):
        self._language = value

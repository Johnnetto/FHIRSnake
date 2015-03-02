__author__ = 'Federico Milano'

import fhir.client.primitive


class Resource:
    def __init__(self):
        self.extension = []
        self.modifierExtension = []
        self.__language = ''
        self.text = ''
        self.contained = []

    @property
    def language(self):
        return self.__language

    @language.setter
    def language(self, code):
        if not isinstance(code, fhir.client.primitive.Code):
            raise TypeError('code has to be a fhir.primitive.Code instance')
        self.__language = code
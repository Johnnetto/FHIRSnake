__author__ = 'john'

import fhir.client.primitive
import fhir.client.complex
import fhir.client.resource


class Identifier():
    def __init__(self):
        self.__use = fhir.client.primitive.Code('')
        self.label = []
        self.__system = fhir.client.primitive.Uri('')
        self.value = []
        self.__period = fhir.client.complex.Period('', '')
        self.__assigner = fhir.client.Resource('')



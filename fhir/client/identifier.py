__author__ = 'john'

import fhir.client.primitive
import fhir.client.complex
import fhir.client.resource


class Identifier():
    def __init__(self):
        self.__use = fhir.client.primitive.Code('')
        self.label = ''
        self.__system = fhir.client.primitive.Uri('')
        self.value = ''
        self.__period = fhir.client.complex.Period('', '')
        self.__assigner = fhir.client.Resource('')


    @property
    def use(self):
        return self.__use

    @use.setter
    def use(self, use):
        if not isinstance(use, fhir.client.primitive.Code):
            raise TypeError('Use should be of code type.')
        self.__use = use

    @property
    def system(self):
        return self.__system

    @system.setter
    def system(self, system):
        if not isinstance(system, fhir.client.primitive.Uri):
            raise TypeError('System should be of code Uri.')
        self.__system = system

    @property
    def period(self):
        return self.__period

    @period.setter
    def period(self, period):
        if not isinstance(period, fhir.client.complex.Period):
            raise TypeError('Period should be of code Period.')
        self.__period = period

    @property
    def assigner(self):
        return self.__assigner

    @assigner.setter
    def assigner(self, assigner):
        if not isinstance(assigner, fhir.client.Resource):
            raise TypeError('Assigner should be of code Resource.')
        self.__assigner = assigner
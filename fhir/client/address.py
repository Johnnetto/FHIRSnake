__author__ = 'Federico Milano'

import fhir.client.primitive
import fhir.client.complex


class Address:
    def __init__(self):
        self.__code = fhir.client.primitive.Code('home')
        self.lines = []
        self.city = ''
        self.state = ''
        self.zip = ''
        self.country = ''
        self.__period = fhir.client.complex.Period('', '')

    @property
    def code(self):
        return self.__code

    @code.setter
    def code(self, code):
        strcode = code
        if isinstance(code, fhir.client.primitive.Code):
            strcode = code.__str__()

        if strcode != 'home' and strcode != 'work' and strcode != 'temp' and strcode != 'old':
            raise ValueError('A code value must be home or work or temp or old.')
        self.__code = fhir.client.primitive.Code(strcode)

    @property
    def period(self):
        return self.__period

    @period.setter
    def period(self, period):
        if not isinstance(period, fhir.client.complex.Period):
            raise TypeError('Period should be of Period type.')

    def str(self):
        return 'text representation'


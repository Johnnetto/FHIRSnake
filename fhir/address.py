__author__ = 'Federico Milano'

import fhir.primitives
import fhir.period

class Address:
    def __init__(self):
        self.__code = fhir.primitives.Code('home')
        self.lines = []
        self.city = ''
        self.state = ''
        self.zip = ''
        self.country = ''
        self.__period = fhir.complex.Period('', '')

    @property
    def code(self):
        return self.__code

    @code.setter
    def code(self, code):
        strcode = code
        if isinstance(code, fhir.primitives.Code):
            strcode = code.__str__()

        if strcode != 'home' and strcode != 'work' and strcode != 'temp' and strcode != 'old':
            raise ValueError('A code value must be home or work or temp or old.')
        self.__code = fhir.primitives.Code(strcode)

    @property
    def period(self):
        return self.__period

    @code.setter
    def period(self, period):
        if not isinstance(period, fhir.complex.Period):
            raise TypeError('Period should be of Period type.')

    def str(self):
        return 'text representation'


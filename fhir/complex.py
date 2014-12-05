__author__ = 'Federico Milano'

import fhir.primitives

class Period:
    def __init__(self, start, end):
        self.__start = start # check if these are a valid datetime
        self.__end = end


class Address:
    def __init__(self):
        self.__code = fhir.primitives.Code('home')
        self.lines = []
        self.city = ''
        self.state = ''
        self.zip = ''
        self.country = ''
        self.__period = Period('', '')

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
        if not isinstance(period, Period):
            raise TypeError('Period should be of Period type.')

    def str(self):
        return 'text representation'


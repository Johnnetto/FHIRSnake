__author__ = 'Federico Milano'

import re

class Code:
    def __init__(self, code):
        if not isinstance(code, str):
            raise TypeError('Code must be a string.')
        r = re.compile('[^\s]+([\s]+[^\s]+)*')
        if r.match(code) is None:
            raise TypeError('A code is restricted to string which has at least one character and no leading or trailing whitespace, and where there is no whitespace other than single spaces in the contents.')
        self.__code = code

    def __str__(self):
     return self.__code



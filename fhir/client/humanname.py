import fhir.client.primitive
import fhir.client.complex


class HumanName:
    """
    A human name with the ability to identify parts and usage.
    Names may be changed, or repudiated, or people may have different names in different contexts.
    Names may be divided into parts of different type that have variable significance depending on
    context, though the division into parts does not always matter. With personal names, the different
    parts may or may not be imbued with some implicit meaning; various cultures associate different
    importance with the name parts and the degree to which systems must care about name parts around
    the world varies widely.
    """

    def __init__(self):
        # Identifies the purpose for this name.

        self.__use = fhir.client.primitive.Code('home')

        # A full text representation of the name.
        self.__text = ' '

        # The part of a name that links to the genealogy. In some cultures (e.g. Eritrea) the family name of
        # a son is the first name of his father.
        self.__family = []

        # Given name.
        self.__given = []

        # Part of the name that is acquired as a title due to academic, legal, employment or nobility
        # status, etc. and that appears at the start of the name.
        self.__prefix = []

        # Part of the name that is acquired as a title due to academic, legal, employment or nobility
        # status, etc. and that appears at the end of the name.
        self.__suffix = []

        # Indicates the period of time when this name was valid for the named person.
        self.__period = fhir.client.complex.Period('', '')

    @property
    def use(self):
        return self.__use

    @use.setter
    def use(self, use):
        if not isinstance(use, fhir.client.primitive.Code) and not isinstance(use, str):
            raise TypeError('A code value must be of type Code or str.')
        string_use = use
        if isinstance(use, fhir.client.primitive.Code):
            string_use = use.__str__()
        if string_use != 'usual' and string_use != 'official' and string_use != 'temp' and string_use != 'anonymous' \
                and string_use != 'old' and string_use != 'maiden':
            raise ValueError('A Code value must be usual, official, temp, anonymous, old or maiden.')
        self.__use = fhir.client.primitive.Code(string_use)

    @property
    def text(self):
        return self.__text

    @text.setter
    def text(self, text):
        if not isinstance(text, str):
            raise TypeError('A text value must be of type str.')
        self.__text = text

    @property
    def period(self):
        return self.__period

    @period.setter
    def period(self, period):
        if not isinstance(period, fhir.client.complex.Period):
            raise TypeError('A period value must be of type Period.')

    def str(self):
        return 'text representation'
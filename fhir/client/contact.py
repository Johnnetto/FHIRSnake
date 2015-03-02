import fhir.client.primitive
import fhir.client.complex


class Contact:
    """
    All kinds of technology-mediated contact details for a person or organization, including telephone, email, etc.
    """

    def __init__(self):

        # Telecommunications form for contact - what communications system is required to make use of the contact.
        self.__system = fhir.client.primitive.Code('home')

        # The actual contact details, in a form that is meaningful to the designated communication
        # system (i.e. phone number or email address).
        self.value = ' '

        # Identifies the purpose for the address.
        self.__use = fhir.client.primitive.Code('home')

        # Time period when the contact was/is in use.
        self.__period = fhir.client.complex.Period('', '')

    @property
    def system(self):
        return self.__system

    @system.setter
    def system(self, system):
        if not isinstance(system, fhir.client.primitive.Code) and not isinstance(system, str):
            raise TypeError('A code value must be of type Code or str.')
        string_use = system
        if isinstance(system, fhir.client.primitive.Code):
            string_use = system.__str__()
        if string_use != 'phone' and string_use != 'fax' and string_use != 'email' \
                and string_use != 'url':
            raise ValueError('A Code value must be phone, fax, email, or url.')
        self.__use = fhir.client.primitive.Code(string_use)

    @property
    def value(self):
        return self.value

    @value.setter
    def value(self, value):
        if not isinstance(value, str):
            raise TypeError('A value value must be of type str.')
        self.value = value

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
        if string_use != 'home' and string_use != 'work' and string_use != 'temp' \
                and string_use != 'old' and string_use != 'mobile':
            raise ValueError('A Code value must be home, work, temp, old or mobile.')
        self.__use = fhir.client.primitive.Code(string_use)

    @property
    def period(self):
        return self.__period

    @period.setter
    def period(self, period):
        if not isinstance(period, fhir.client.complex.Period):
            raise TypeError('A period value must be of type Period.')

    def str(self):
        return 'text representation'
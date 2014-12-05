__author__ = 'Federico Milano'

import fhir.primitives
import fhir.complex

c = fhir.primitives.Code('hola')
a = fhir.complex.Address()
a.code = fhir.primitives.Code('home')
a.code = 'temp'
a.period = fhir.complex.Period(1, 2)


__author__ = 'Federico Milano'

import fhir.primitive
import fhir.complex

c = fhir.primitive.Code('hola')
a = fhir.complex.Address()
a.code = fhir.primitive.Code('home')
a.code = 'temp'
a.period = fhir.complex.Period(1, 2)

b = fhir.complex.HumanName()
b.use = fhir.primitive.Code('official')
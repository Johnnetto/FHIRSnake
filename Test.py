__author__ = 'Federico Milano'

import fhir.client.primitive
import fhir.client.complex

c = fhir.client.primitive.Code('hola')
a = fhir.client.complex.Address()
a.code = fhir.client.primitive.Code('home')
a.code = 'temp'
a.period = fhir.client.complex.Period(1, 2)

b = fhir.client.complex.HumanName()
b.use = fhir.client.primitive.Code('official')
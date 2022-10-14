from ..baas.customers import Customer
from ..baas import Baas
Baas.init('CF206278CCQ2DF584OK74C7OSG1G',
          'e412451a8a6281d4567a7598e6df4c7a92d5b3e5', 'TEST')

# test customer creation
response = Customer.add('customer008', 'INDIVIDUAL', 'Orpheu The Dog',
                        '9999999999', 'email@x.y')
assert response.status_code == 200
assert "customer" in response.text

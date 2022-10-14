from ..baas.customers import Customer
from ..baas import Baas
import json
import random


def test_baas():
    Baas.init('CF206278CCQ2DF584OK74C7OSG1G',
              'e412451a8a6281d4567a7598e6df4c7a92d5b3e5', 'TEST')


# test customer creation
CUSTOMER_ID = ''


def generate_random_customer_id():
    return 'customer_'+str(random.randint(100000, 10000000))


def test_create_customer():
    customer_id = generate_random_customer_id()
    response = Customer.add(customer_id, 'INDIVIDUAL', 'Orpheu The Dog',
                            '9999999999', 'email@x.y')
    assert response.status_code == 200
    assert "customer" in response.text
    response_object = json.loads(response.text)
    assert "customer" in response_object
    assert response_object["customer"]["customer_id"] == customer_id
    global CUSTOMER_ID
    CUSTOMER_ID = response_object["customer"]["customer_id"]


def test_get_customer():
    assert CUSTOMER_ID != ''
    response = Customer.get(customer_id=CUSTOMER_ID)
    assert response.status_code == 200
    response_object = json.loads(response.text)
    assert "customer" in response_object
    assert response_object["customer"]["customer_id"] == CUSTOMER_ID

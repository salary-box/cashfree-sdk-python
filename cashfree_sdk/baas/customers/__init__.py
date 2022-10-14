from .__create_customer import CreateCustomer
from .__get_customer import GetCustomer
from ...baas import __request as request
from ...baas import __authorize_creds as authorize


class Customer():
    # @authorize.authorize
    @staticmethod
    def add(customer_id, customer_type, full_name, phone, email, remarks=None):
        create_customer_request = CreateCustomer(
            customer_id=customer_id,
            customer_type=customer_type,
            full_name=full_name,
            phone=phone,
            email=email,
            remarks=remarks
        )
        return request.trigger_request(create_customer_request)

    @staticmethod
    def get(customer_id):
        get_customer_request = GetCustomer(
            customer_id=customer_id
        )
        return request.trigger_request(get_customer_request)

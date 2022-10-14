from .__create_customer import CreateCustomer
from ...payouts import __request as request
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

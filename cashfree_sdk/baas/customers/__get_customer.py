class GetCustomer:
    end_point = "/banking/customers"
    req_type = "GET"

    def __init__(self, *args, **kwargs):
        customer_id = kwargs["customer_id"]
        if customer_id:
            self.end_point += "/" + kwargs["customer_id"]

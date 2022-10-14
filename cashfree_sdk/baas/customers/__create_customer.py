class CreateCustomer:
    end_point = "/banking/customers"
    req_type = "POST"

    def __init__(self, *args, **kwargs):
        self.customer_id = kwargs["customer_id"]
        self.type = kwargs["customer_type"]
        self.full_name = kwargs["full_name"]
        self.phone = kwargs["phone"]
        self.email = kwargs["email"]
        self.remarks = kwargs["remarks"]

from .__payouts_creds import PayoutCreds

class PayoutsConfig:
    
    def __init__(self):
        self.payout_creds = PayoutCreds()
        self.env = "TEST"
        self.url = "https://payout-gamma.cashfree.com"
        self.token = ""
        self.expiry = ""

    def init_creds(self, client_id, client_secret, env):
        self.payout_creds.set_creds(client_secret=client_secret, client_id=client_id)
        self.env = env or "TEST"
        if env == "PROD":
            self.url = "https://payout-api.cashfree.com"

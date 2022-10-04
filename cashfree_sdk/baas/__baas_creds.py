from cashfree_sdk.exceptions.exceptions import *


class BaasCreds:

    def __init__(self):
        self.client_id = ""
        self.client_secret = ""

        # initialise client id & secreet from environment variables
        import os
        if os.environ.get("CF_BAAS_CLIENT_ID") and os.environ.get("CF_BAAS_CLIENT_SECRET"):
            self.client_id = os.environ.get("CF_BAAS_CLIENT_ID")
            self.client_secret = os.environ.get("CF_BAAS_CLIENT_SECRET")

    def set_creds(self, client_id, client_secret):
        self.client_id = client_id
        self.client_secret = client_secret

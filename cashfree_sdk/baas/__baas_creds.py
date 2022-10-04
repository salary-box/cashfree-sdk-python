from cashfree_sdk.exceptions.exceptions import *


class BaasCreds:

    def __init__(self):
        self.client_id = ""
        self.client_secret = ""
        self.public_key = b""
        self.public_key_file = ""

    def set_creds(self, client_id, client_secret):
        self.client_id = client_id
        self.client_secret = client_secret

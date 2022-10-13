from .__baas_creds import BaasCreds


class BaasConfig:

    def __init__(self):
        self.baas_creds = BaasCreds()
        self.env = "TEST"
        self.url = "https://test.cashfree.com"
        self.token = ""
        self.expiry = 0
        self.signature = ""
        self.signature_expiry = 0
        self.mode = "IP"

    def init_creds(self, client_id, client_secret, env):
        self.baas_creds.set_creds(
            client_secret=client_secret, client_id=client_id)
        self.env = env or "TEST"
        if env == "PROD":
            self.url = "https://api.cashfree.com"

    def init_signature_creds(self, client_id, client_secret, env, **kwargs):
        self.init_creds(client_id, client_secret, env)
        self.mode = "SIGNATURE"
        if "public_key" in kwargs:
            self.baas_creds.set_public_key(public_key=kwargs["public_key"])
        else:
            self.baas_creds.set_public_key(
                public_key_file=kwargs["public_key_path"])

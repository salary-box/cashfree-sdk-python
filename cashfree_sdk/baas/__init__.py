from .__baas_config import BaasConfig

baas_config_var = BaasConfig()


class Baas():

    @staticmethod
    def init(client_id, client_secret, env, *args, **kwargs):
        global baas_config_var
        baas_config_var.init_creds(
            client_id=client_id, client_secret=client_secret, env=env)

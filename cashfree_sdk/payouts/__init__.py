from .payouts_creds import PayoutCreds
from .payouts_config import PayoutsConfig

payouts_config_var = PayoutsConfig()

class Payouts():

    @staticmethod
    def init(client_id, client_secret, env, *args, **kwargs):
        global payouts_config_var
        payouts_config_var.init_creds(client_id=client_id, client_secret=client_secret, env=env)

                
           

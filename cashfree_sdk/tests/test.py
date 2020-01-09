from payouts import Payouts
from payouts.beneficiary import Benefeciary
from payouts import payouts_config_var


client_id = "cliend_id"
client_secret = "cliend_secret"
env = "TEST"

print("Initializing test")
payouts = Payouts.init(client_id, client_secret, env)
print("-==", type(payouts_config_var), id(payouts_config_var), payouts_config_var.url)

bene_test = Benefeciary.add("kit_test6", "ankur", "ankur@cashfree.com", "9787570389", "aakjakjakja")
bene_det = Benefeciary.get_bene_details("kit_test6")

# print(bene_det.__dict__, "\n\n\n",  bene_test.__dict__ )


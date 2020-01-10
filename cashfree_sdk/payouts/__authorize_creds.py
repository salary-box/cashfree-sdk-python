import requests as rq
from . import payouts_config_var
import json
import time
from cashfree_sdk.exceptions.exceptions import *

auth_endpoint = "/payout/v1/authorize"
verify_endpoint = "/payout/v1/verifyToken"

def authenticate():
    if not payouts_config_var or payouts_config_var.payout_creds.client_id == "" \
        or payouts_config_var.payout_creds.client_secret == "":
        raise ModuleNotInitiatedError
    
    if payouts_config_var.token != "" and (payouts_config_var.expiry - (time.time() + 100)) > 0:
        return

    merchant_id = payouts_config_var.payout_creds.client_id
    merchant_secret = payouts_config_var.payout_creds.client_secret
    auth_url = payouts_config_var.url + auth_endpoint

    headers = { 
        'X-Client-Id': merchant_id,
        'X-Client-Secret': merchant_secret
    }

    res = rq.request("POST", auth_url, headers=headers)

    if res.status_code == 200:
        data = json.loads(res.text)
        if data and "subCode" in data and data["subCode"]:
            if data["subCode"] == "200":
                token = ""
                expiry = 0
                res_data = data.get("data")
                if res_data and "token" in res_data and "expiry" in res_data:
                    token = res_data["token"]
                    expiry = res_data["expiry"]
                else:
                    raise TokenGenFailedError
                if token and token != "":
                    if verify_token(token):
                        payouts_config_var.token = token
                        payouts_config_var.expiry = expiry
                        return
            else:
                raise IncorrectCredsError(data["message"])
        else:
            raise AuthenticationFailureError
    raise ServiceDownError


def verify_token(token):
    verify_url = payouts_config_var.url + verify_endpoint
    headers = {
        'Authorization' : "Bearer "+ token
    }
    res = rq.request("POST", verify_url, headers=headers)

    if res.status_code == 200:
        data = json.loads(res.text)
        if data["status"] == "SUCCESS" and data["subCode"] == "200":
            return True
        return False
    
    raise ServiceDownError

def authorize(func):
    def authenticate_gen_token(*args, **kwargs):
        authenticate()
        return func(*args, **kwargs)
    return authenticate_gen_token









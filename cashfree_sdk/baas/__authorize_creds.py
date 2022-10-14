import requests as rq
from . import baas_config_var
import json
import time
from cashfree_sdk.exceptions.exceptions import *

auth_endpoint = "/banking"
verify_endpoint = "/payout/v1/verifyToken"
three_minutes_secs = 180


def authenticate():
    if not baas_config_var or baas_config_var.baas_creds.client_id == "" \
            or baas_config_var.baas_creds.client_secret == "":
        raise ModuleNotInitiatedError

    if baas_config_var.token != "" and baas_config_var.expiry != 0 and (baas_config_var.expiry - (time.time() + three_minutes_secs)) > 0:
        return

    client_id = baas_config_var.baas_creds.client_id
    client_secret = baas_config_var.baas_creds.client_secret
    auth_url = baas_config_var.url + auth_endpoint

    headers = {
        'X-Client-Id': client_id,
        'X-Client-Secret': client_secret
    }

    if baas_config_var.mode == "SIGNATURE":
        generate_signature()
        if baas_config_var.signature == "":
            raise SignatureCreationFailedError()
        headers['X-Cf-Signature'] = baas_config_var.signature

    res = rq.request("POST", auth_url, headers=headers)

    if res.status_code == 200:
        print('respone text: ' + res.text)
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
                        baas_config_var.token = token
                        baas_config_var.expiry = expiry
                        return
            else:
                raise IncorrectCredsError(data["message"])
    else:
        print('res status code: ' + str(res.status_code))
        raise AuthenticationFailureError
    raise ServiceDownError


def verify_token(token):
    verify_url = baas_config_var.url + verify_endpoint
    headers = {
        'Authorization': "Bearer " + token
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

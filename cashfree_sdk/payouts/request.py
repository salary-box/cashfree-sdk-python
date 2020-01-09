import requests as rq
import json
from cashfree_sdk.payouts import payouts_config_var
from cashfree_sdk.exceptions.exceptions import ServiceDownError


def create_headers(token):
    bearer_token = "Bearer " + token
    headers = { 'Authorization' : bearer_token, 'Content-Type': 'application/json', 
        'cache-control': 'no-cache' }
    return headers

def trigger_request(params, *args, **kwargs):
    if params is None:
        return None
    request_type = getattr(params, "req_type")
    end_point = getattr(params, "end_point")
    if request_type == "GET":
        return make_get_request(end_point=end_point, params=params)
    elif request_type == "POST":
        return make_post_request(end_point=end_point, payload=params)


def make_get_request(end_point, params, *args, **kwargs):
    url = payouts_config_var.url + end_point
    token = payouts_config_var.token
    
    headers = create_headers(token)
    params_dict = {}
    if params:
        params_dict = params.__dict__
    res = rq.request("GET", url, headers=headers, params=params_dict)
    if res.status_code == 200:
        return res
    raise ServiceDownError


def make_post_request(end_point, payload, *args, **kwargs):
    url = payouts_config_var.url + end_point
    token = payouts_config_var.token
    headers = create_headers(token)
    payload_json = ''
    if payload:
        payload_json = json.dumps(payload.__dict__)
    res = rq.request("POST", url, json=payload.__dict__, headers=headers)
    if res.status_code == 200:
        return res
    raise ServiceDownError





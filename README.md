# [BETA]cashfree-sdk-python

The official Cashfree SDK for Python3,

Get started quickly using Cashfree with the Cashfree SDK for python. The SDK helps take the complexity out of coding by providing Python objects for Cashfree services including Payouts, Payment Gateway, Marketplace and Autocollect. The single, downloadable package includes the Cashfree Python Library and documentation.

Please refer to the [Cashfree Docs](https://docs.cashfree.com/docs/)  for the complete API reference.

## Installing
### In Django or Flask Application for Python 3.5+

The preferred way to install the Cashfree SDK for Python is to use the [pip](https://pypi.org/project/pip/) package manager for pip. Simply type the following into a terminal window:
```sh
pip3 install git+https://github.com/cashfree/cashfree-sdk-python.git
```

## Getting Started
### Pre-requisites
  - A [Cashfree Merchant Account](https://merchant.cashfree.com/merchant/sign-up)
  - API keys for different products. You can generate them from your Dashboard
### IP Whitelisting
Your IP has to be whitelisted to hit Cashfree's server. For more information please go here.
## Usage
### Payouts
The package needs to be configured with your account's secret key which is available in your Cashfree Dashboard.
Init the package with your credentials and add the below code in your config.py of your package.
```python

from cashfree_sdk.payouts import Payouts

//Initialize Cashfree Payout
Payouts.init("<client_id>", "<client_secret>", "PROD")
```
| Option              | Default                       | Description                                                                           |
| ------------------- | ----------------------------- | ------------------------------------------------------------------------------------- |
| `ENV`        | `TEST`                        | Environment to be initialized. Can be set to `TEST` or `PROD` |
| `client_id` | ``                             | `ClientID` which can be generated on cashfree dashboard.                  |
| `client_secret`         | ``                        | `ClientSecret` which can be found alongside generated `ClientID`.                        |
[Payout Library Docs](cashfree_sdk/payouts/README.md)


### Using Python requests
Every method returns a python request object which can be used:
```python
from cashfree_sdk.payouts.beneficiary import Benefeciary
bene_add = Benefeciary.add("kit_test6", "ankur", "ankur@cashfree.com", "9999999999", "aakjakjakja")
```
```diff
- All Optional Arguments Should Be Passed As An Keyword (Named) Arguments
```
- For more information about the APIs go to [Payouts](Payouts).
- Complete list of [APIs](https://docs.cashfree.com/docs/payout/guide/#fetch-beneficiary-id).
### TODO
- #### PG
- #### Market Place
- #### Autocollect

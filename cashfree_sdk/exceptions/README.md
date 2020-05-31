# Exceptions

Exceptions are raised from the library on improper operations
- Improper ClientId and Client Secret provided while module init
- Invalid status code received while performing any operation
- Other than 200 or 201 subCode received while performing any request. Details of [subcode](https://docs.cashfree.com/docs/payout/guide/#status-sub-codes)

Exceptions raised for non 200 or 201 subCode contains the details of the wrong operation along with the **X-Request-Id** sent from the server 
 
## List of exceptions

| Exception  | Reason |
| ---------- | ------- |
| CredsNotPresentError | ClientId or Client Secret not provided for the module|
| AuthenticationFailureError | Failed to generate Authentication token for the request |
| IncorrectCredsError | Wrong ClientId or Client Secret provided|
| ConfigMissingForSignatureAuth | Public key missing for generating signature for generating authentication token |
| InvalidPublicKeyError | Invalid Public key .pem file provided |
| SignatureCreationFailedError | Failed to generate signature from the public key |
| InvalidaWebHookPayloadTypeError | Invalid Webhook Payload type provided i.e other than **FORM**, **JSON** |
| BadRequestError | For subcode 400 |
| AuthenticationFailureError | For subcode 401 |
| ForbiddenError | For subcode 403|
| EntityDoesntExistError | For subcode 404 |
| MethodNotAllowedError | For subcode  405 |
| AlreadyExistError | For subcode 409 |
| PreconditionFailedError | For subcode 412 |
| RequestTooLargeError | For subcode 413 |
| InputWrongFormatError | For subcode 422 |
| TooManyRequestError | For subcode 429
| InternalServerError | For subcode  500 |
| ServiceDownError | For subcode 503 |
| UnknownErrorOccurredError| For subcode 520 |

## Exception Handling

Code Snippet to handle exception while integrating the library in python web application.

Example flask app-
```python
from app import app
from cashfree_sdk.payouts.transfers import Transfers
from cashfree_sdk.exceptions import BadRequestError
try:
    tnx_req = Transfers.request_transfer(beneId="JOHN18012", amount="100.1", transferId="DEC2017", \
                transferMode="banktransfer", remarks="Test transfer")
except BadRequestError as e:
    app.logger.exception("Bad request while performing request transfer")
except Exception as e:
    app.logger.exception("Unknown exception while request transfer")
```




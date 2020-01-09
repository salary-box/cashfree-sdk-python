
class IncompleteParametersError(Exception):
    pass

class CredsNotPresentError(Exception):
    pass

class AuthenticationFailureError(Exception):
    pass

class ServiceDownError(Exception):
    pass

class IncorrectCredsError(Exception):
    pass

class TokenGenFailedError(Exception):
    pass

class ModuleNotInitiatedError(Exception):
    pass
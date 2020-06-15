class EventhubException(Exception):
    pass


class Unauthorized(EventhubException):
    pass


class NotFound(EventhubException):
    pass

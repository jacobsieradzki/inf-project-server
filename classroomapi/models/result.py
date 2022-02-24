
class Result:

    def __init__(self, data=None, error=None):
        self.data = data
        self.error = error
        self.is_success = data is not None
        self.is_error = error is not None

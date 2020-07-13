class DuplicateException(Exception):
    def __init__(self, message):
        super().__init__(message+" already exist")

class RecordNotFoundException(Exception):
    def __init__(self, message):
        super().__init__(message+" no exist")

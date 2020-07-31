'''
@function
중복 데이터 처리
'''
class DuplicateException(Exception):
    def __init__(self, message):
        super().__init__(messege+" already exist")

class NotFoundedException(Exception):
    def __init__(self, message):
        super().__init__(message+" no exist")
class NotEvenNumberError(Exception):
    def __init__(self):
        super().__init__('짝수가 아닙니다.')

class Person:
    count=0

    def __init__(self):
        Person.count+=1

    @classmethod
    def create(cls):
        p=cls()
        return p

james = Person()
maria = Person()

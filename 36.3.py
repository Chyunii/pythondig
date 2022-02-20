class Person:
    def __init__(self):
        print('Person __init__')
        self.hello = '안녕하세요.'
 
class Student(Person):
    def __init__(self):
        print('Student__init__')
        super(Student, self).__init__()
        self.school='파이썬 코딩도장'
 
james = Student()

#age = 20
#if age >= 18:
   # print 'your age is', age
   # print 'adult'
class User(object):
    def __init__(self, id, name):
        self.id = id
        self.name = name

[
    User('1', 'Michael'),
    User('2', 'Bob'),
    User('3', 'Adam')
]


class Student:
    def __init__(self):
        self._name = None

    def fget(self):
        print('调用fget')
        return self._name
    def fset(self, name):
        print('调用fset')
        if name == 'root' or name == 'admin':
            raise ValueError('不能使用root或者admin')
        self._name = name

    def fdel(self):
        del self._name

    name = property(fget=fget, fset=fset, fdel=fdel)
# s1 = Student()
# s1.name = "root"
# print(s1.name)

class Teacher:
    def __init__(self):
        self._name = None

    @property
    def name(self):
        print('fget')
        return self._name

    @name.setter
    def name(self, name):
        print('fset')
        self._name = name

t1 = Teacher()
t1.name = 'Jack'
print(t1.name)
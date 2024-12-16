from contextlib import nullcontext


class Employee():

    name = ""
    sername = ""
    age = 0

    def __init__(self, n, s, a):
        self.name = n
        self.sername = s
        self.age = a

    def give_raise(self, t):
        if t == 0:
            self.age += 5000
        else:
            self.age += t
        return self.age
def make_adder(n):
    def adder(k):
        return n + k
    return adder

class Adder(object):
    def __init__(self, n):
        self.n = n
    def __call__(self, k):
        return self.n + k

class Dynamo:
    def __getattr__(self, key):
        if key == 'color':
            return 'PapayaWhip'
        else:
            raise AttributeError

class SuperDynamo:
    def __getattribute__(self, key):
        if key == 'color':
            return 'PapayaWhip'
        else:
            raise AttributeError
class Rastan:
    def __getattribute__(self, key):
        raise AttributeError
    def swim(self):
        pass
        
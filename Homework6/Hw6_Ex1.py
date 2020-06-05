class readonly(object):
    def __init__(self, func):
        self.func = func

    def __get__(self, obj, owner=None):
        if obj is None:
            return self
        else:
            return self.func(obj)

    def __set__(self, obj, value):
        raise AttributeError



class Test(object):
    def __init__(self):
        self.__val = 1

    @readonly
    def val(self):
        return self.__val


test = Test()
print(test.val)
test.val = 3

class Test(object):

    name = "Angel"

    def __init__(self, num1=1):
        self.num1 = num1
        self.__num = 12

    def get(self):
        return self.__num

    def set(self, num):
        self.__num = num

    @classmethod
    def access_name(cls):
        return f"Name from class variable {cls.name}"

    @staticmethod
    def meth1():
        return "This is static method"

    def __str__(self):
        return "This is Test method"


if __name__ == "__main__":
    o = Test(11)
    print(o)
    print(o.num1)
    print(o.get())
    o.set(111)
    print(o.get())
    print(o.meth1())
    print(Test.meth1())
    print(o.access_name())

# creating classes using three different ways

# first way
class A:
    def __init__(self):
        pass


# second way
class B:
    @classmethod
    def __call__(cls, *args, **kwargs):
        return super(B, cls).__call__(cls, *args, **kwargs)


# Third way
class C:
    def __new__(cls, *args, **kwargs):
        return super(C, cls).__new__(cls, *args, **kwargs)

    def __init__(self, *args, **kwargs):
        super(C, self).__init__(*args, **kwargs)


if __name__ == "__main__":
    a = A()
    print(a)
    b = B()
    print(b)
    c = C()
    print(c)

class Meta(type):
    def __new__(cls, *args, **kwargs):
        return super(Meta, cls).__new__(cls, *args, **kwargs)

    def __init__(self, *args, **kwargs):
        super(Meta, self).__init__(*args, **kwargs)


class A(metaclass=Meta):
    def __init__(self):
        pass


if __name__ == "__main__":
    a = A()
    print(a)

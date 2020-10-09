class SingletonException(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message


# first way
class A:
    __instance = None

    def __init__(self, name, age):
        if A.__instance is None:
            A.__instance = self
        else:
            raise SingletonException("Only one instance allowed")
        self.name = name
        self.age = age

    def say_name(self):
        return self.name

    def say_age(self):
        return self.age


# second way
# class SingletonMeta:
#     _instances = {}
#
#     def __call__(cls, *args, **kwargs):
#         if cls not in cls._instances:
#             instance = super().__call__(*args, **kwargs)
#             cls._instances[cls] = instance
#         return cls._instances[cls]
#
#
# class B(metaclass=SingletonMeta):
#     pass


# third way
from functools import wraps


def singleton(original_cls):
    original_new = original_cls.__new__
    instance = None

    @wraps(original_cls.__new__)
    def __new__(cls, *args, **kwargs):
        nonlocal instance
        if instance is None:
            instance = original_new(cls, *args, **kwargs)
        return instance

    original_cls.__new__ = __new__
    return original_cls


@singleton
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_name(self):
        return self.name

    def say_age(self):
        return self.age


if __name__ == "__main__":
    a = A("Angel Dhakal", 19)
    print(id(a))
    print(a.say_name())
    print(a.say_age())

    # b = B()
    # print(id(b))

    # anjal = Person("Angel Dhakal", 19)
    # print(anjal.say_name())
    # print(anjal.say_age())

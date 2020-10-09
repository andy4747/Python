class Animals:
    def __init__(self):
        self.legs = 4
        self.domestic = True
        self.tails = True
        self.mammals = True

    def is_mammal(self):
        print("It is a mammal")

    def is_domestic(self):
        print("It is domestic")


class Dog(Animals):
    def __init__(self):
        super().__init__()

    def is_mammal(self):
        super().is_mammal()


class Horse(Animals):
    def __init__(self):
        super().__init__()

    def hasTailAndLegs(self):
        if self.tails and self.legs == 4:
            print("Has Tails and Legs")

if __name__ == "__main__":
    swen = Dog()
    swen.is_mammal()
    toofan = Horse()
    toofan.hasTailAndLegs()

#chr() method converts int into ascii characters
#ord() method converts ascii characters into int

import random
import os

class PasswordGen:
    def __init__(self,length):
        self.length = length

    def user_input(self):
        self.length = int(input("Enter length for your password: "))
        if self.length<=7:
            return
        return self.length

    def generate_password(self):
        passwrd = ''
        try:
            for i in range(self.user_input()):
                random_num = random.randrange(33,127)
                character = chr(random_num)
                passwrd+=character
            return passwrd
        except TypeError:
            print("Length must be 8 character or above.")

test = PasswordGen(10)
print(test.generate_password())
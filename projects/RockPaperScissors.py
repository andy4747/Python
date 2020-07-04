import random
import time
import os


class RockPaperScissors:

    def player(self):
        computer_result = random.randrange(1,7)
        for i in range(3):
            if i==0:
                print("roll your hand human.")
            print(i+1)
            time.sleep(1.5)
            os.system('cls' if os.name == 'nt' else 'clear')
        human_result = input("enter your result(R/P/S): ")
        if human_result.lower()=='r':
            if computer_result==1 or computer_result==4:
                return "Draw"
            elif computer_result==2 or computer_result==5:
                return "Computer Wins"
            elif computer_result==3 or computer_result==6:
                return 'Human Wins'
        elif human_result.lower()=='p':
            if computer_result==1 or computer_result==4:
                return "Human Wins"
            elif computer_result==2 or computer_result==5:
                return "Draw"
            elif computer_result==3 or computer_result==6:
                return 'Computer Wins'
        elif human_result.lower()=='s':
            if computer_result==1 or computer_result==4:
                return "Computer Wins"
            elif computer_result==2 or computer_result==5:
                return "Human Wins"
            elif computer_result==3 or computer_result==6:
                return 'Draw'
        else:
            return "Enter Valid Input"
        

# 1 = rock
# 2 = paper
# 3 = scissors

test = RockPaperScissors()
print(test.player())
from utils import binary_decimal, decimal_binary
from full_adder import full_adder,adder,user_input

def main():
    run = True
    while run:
        print("------------------")
        print("1. Add Two Numbers")
        print("------------------")
        print("2. Exit The Program")
        print("-------------------")
        choice = int(input("Enter Your Choice: "))
        print("--------------------")  
        if choice==1:    
            num1, num2 = user_input()
            answer = adder(num1,num2)
            if binary_decimal(int(answer)) > 255:
                print("{{{{{{{{Please Enter Valid Input}}}}}}}}")
                print("----------------------------------------")
                print()
                continue
            print("----------------------------------------------------------------")
            print(f"First Number Entered ==> (Binary) ==> {num1} &&& (Deciaml) ==> {binary_decimal(int(num1))}")
            print("----------------------------------------------------------------")
            print(f"Second Number Entered ==> (Binary) ==> {num2} &&& (Decimal) ==> {binary_decimal(int(num2))}")
            print("----------------------------------------------------------------")
            print(f"The result is (Binary) ==> {answer} &&& (Decimal) ==> {binary_decimal(int(answer))}")
            print("------------------------------------------------------")
            print(f"Result is ==> {binary_decimal(int(answer))}")
            print()
        elif choice==2:
            run = False
        else:
            print("Enter Valid Choice")

if __name__ == "__main__":
    main()
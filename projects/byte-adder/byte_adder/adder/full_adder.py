from utils import XOR,adjust_length,decimal_binary,binary_decimal

def full_adder(num1,num2,carry=0):
    a_xor_b = XOR(num1,num2)
    sum_ = XOR(a_xor_b,carry)
    carry = ((num1 and num2) or (num2 and carry) or (num1 and carry))
    return sum_,carry

def adder(num1,num2):
    carry = 0
    result = ''
    for i in range(len(num1)-1, -1, -1):
        sum_,carry = full_adder(int(num1[i]),int(num2[i]),carry)
        result += str(sum_)
    result+=str(carry)
    return result[::-1]

def user_input():
    # print("---------------------------------------------")
    num1 = input("Enter First Number(Decimal):  ")
    print("---------------------------------")
    num2 = input("Enter Second Number(Decimal): ")
    print("---------------------------------")
    print()
    num1 = str(decimal_binary(num1))
    num2 = str(decimal_binary(num2))
    return adjust_length(num1, num2)
def XOR(x,y):
    return int(x != y)


def binary_decimal(num):
    num_ = int(num)
    base = 1
    dec = 0
    while num_!=0:
        digit = num_%10
        num_ = num_//10
        dec += digit*base
        base *= 2
    return dec


def decimal_binary(num):
    num = int(num)
    bin = 0
    temp = 1
    while num!=0:
        bin += num%2*temp
        num = num//2
        temp *= 10  
    return bin


def list_to_String(list_):  
    string = ""
    result = []
    for i in list_:
        result.append(str(i))
    return string.join(result)


def fill_string(string,fill='0',num=1):
    _list = []
    for i in string:
        _list.append(i)
    for i in range(num):
        _list.insert(0,fill)
    string = list_to_String(_list)
    return string
    

def adjust_length(str1,str2):
    if len(str1)<len(str2):
        num = len(str2) - len(str1)
        str1 = fill_string(str1,num=num)
    if len(str2)<len(str1):
        num = len(str1) - len(str2)
        str2 = fill_string(str2,num=num)
    return str1,str2
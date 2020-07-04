import math
from statistics import mean

#Lambda functions OR anonymous function practice

# lambda arguments:expresion

# add = lambda a,b : a+b #a,b are parameters and both values are added and returned
# a = add(2,3)
# b = add(10,10)
# c = add(5,5)
# print(f"{a} and {b} and {c}")

#anonymous function within user defined functions

#lambda within user defined function
print()
def a(x):
    return(lambda y: x+y)

t = a(10)
print("lambda function within user defined function")
print(t(8))

###Lambda function within higher order functions

def area(r):
    """ Area of circle, radius r"""
    return math.pi * (r**2)

#find the radius for all the radii in list below

radii = [10,45,67,35,78]
areas = []

#Method 1 = Using loop
print()
print("Using loop")
for i in radii:
    a = area(i)
    areas.append(a)

print(areas)
print()

#Method 2 = Using map function
#map func is used to calculate ceratin operation from a function to each item in a iterable
#map(function,iterable) - returns a map object

#Example 01
print("Using 'map' function")
values = map(area,radii) # returns map object

#convert map object into list using 'list' method
values = list(values)
print(values)
print()

#Example 02
temps = [("Kathmandu",29),("Biratnagar",33),("Pokhara",27)]

c_to_f = lambda data: (data[0],(9/5)*data[1]+32)

values = list(map(c_to_f,temps))
print("mapped celcius into fahrenheit")
print(values)
print()

#### Filter Function
#Used to filter out datas from iterable
# filter(function,iterable) - returns filter object

#Example 01
#filter out the below average value from given list
datas = [23,12,23,5,34,7,34,23,21]
avg = mean(datas)
values = list(filter(lambda x: x>avg,datas))
print("Above average values")
print(values)
print()
values = list(filter(lambda x: x<avg,datas))
print("Below average values")
print(values)
print()

#Filter out the empty string from the countries list

countries = ["","Nepal","","Bhutan"]
values = list(filter(None,countries))
print("Filtered out list of countries")
print(values)
print()
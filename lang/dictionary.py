#Below are the two lists convert it into the dictionary
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
kv=dict(zip(keys,values))
print(kv)

#Merge following two Python dictionaries into one
dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
dict3={**dict1,**dict2}
print(dict3)
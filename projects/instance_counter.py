def instance_counter(arr):
    counter=dict()
    for i in arr:
        if arr in counter:
            counter[arr]+=1
        else:
            counter[arr]=1
    return counter

my_list=[1,1,1,2,2,2,3,3,5,5,5]
print(instance_counter(my_list))

def instance_counter(arr):
    counter=dict()
    for i in range(len(arr)):
        if arr[i] in counter:
            counter[arr[i]]+=1
        else:
            counter[arr[i]]=1
    return counter

my_list=[1,1,1,2,2,2,3,3,5,5,5]
print(instance_counter(my_list))

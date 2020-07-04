def count_instances(arr):
	count={}
	for item in arr:
		if item in count:
			count[item]+=1
		else:
			count=1
	return count

__=[1,1,1,2,2,3,3,3,3,4,4,4,4,4,5,5,9,9,9]
print(count_instances(__))

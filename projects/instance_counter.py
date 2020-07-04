def count_instances(arr):
	result=[]
	for i in arr:
		count=0
		for j in arr:
			if i==j:
				count+=1
		result.append((i,count))
	result = dict(sorted(result))
	return result

__=[1,1,1,2,2,3,3,3,3,4,4,4,4,4,5,5,9,9,9]
print(count_instances(__))
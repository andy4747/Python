#Given a two list. Create a third list by picking an odd-index element from the first list and even index elements from second.
def odd_even_index(first_list,second_list):
	odd_items=first_list[1::2]
	even_items=second_list[0::2]
	result=odd_items+even_items
	return result

#Given an input list removes the element at index 4 and add it to the 2nd position and also, at the end of the list
def back_and_forth(list):
	fourth=list.pop(4)
	list.insert(2,fourth)
	list.insert(len(list),fourth)
	return list

#count of each element from list
def instance_counter(list):
	count={}
	for i in list:
		if i in count:
			count[i]+=1
		else:
			count[i]=1
	return count


def transpose_matrix(matrix):
	inverse=[[x,y] for x,y in zip(matrix[0],matrix[1])]
	return inverse


def intersection(list1,list2):
	list1,list2=set(list1),set(list2)
	result=list1 & list2
	return list(result)
	

def main():
	listOne = [3, 6, 9, 12, 15, 18, 21]
	listTwo = [4, 8, 12, 16, 20, 24, 28]
	print(odd_even_index(listOne,listTwo))
	lis=[34, 54, 67, 89, 11, 43, 94]
	print(back_and_forth(lis))
	liss=[1,1,1,2,2,2,3,3,4,4,5]
	print(instance_counter(liss))
	matrix=[[1,2,3],
 		[4,5,6]]
	print(transpose_matrix(matrix))
	set1=[1,2,3,4,5]
	set2=[4,5,6,7]
	print(intersection(set1,set2))

if __name__=='__main__':
	main()
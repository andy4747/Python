def bin_search(arr,search_item):
    arr = sorted(arr)
    first_index = 0
    last_index = len(arr) - 1
    middle_index = 0
  
    while first_index <= last_index: 
  
        middle_index = int((last_index + first_index)/2)
   
        if arr[middle_index] < search_item: 
            first_index = middle_index + 1
  
        elif arr[middle_index] > search_item: 
            last_index = middle_index - 1
  
        else: 
            return middle_index 
  
    return 'Not Found'
        

print(bin_search([10,20,30,1234,56789,23456,4567,78789,8765,34567,23456,120,130,140,150,160,170,1234,180,190,200],78789))
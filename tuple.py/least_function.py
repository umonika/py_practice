
def smallest(a_list):
    min = a_list[0]
    for val in a_list:
        if val < min :
            min = val
    return min

list1= [-4,2,3,5,1,4]    
print('min :',smallest(list1))
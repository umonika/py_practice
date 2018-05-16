def minimum(numlist):#function definition for minimum number
    min = numlist[0]
    for val in numlist:
        if val <= min:
            min = val
    return min

def maximum(numlist):#function definition for maximum number
    max = numlist[0]
    for val in numlist:
        if val >= max:
            max = val
    return max
list1 = [6,5,4,3,8,2]#list 
print(list1)
print('minimum number is ',minimum(list1)) #calling minimum function
print('maximum number is ',maximum(list1)) #calling maximum function

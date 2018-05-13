list1 = [1,2,3,4,5,5]
dict1 = {}

for a_num in list1:
    if a_num in dict1:
        dict1[a_num] = dict1[a_num] + 1
    else:
        dict1[a_num] = 1

print ("list1",list1) #list
print ("dict1",dict1) #no of occurences
print ("dict1.keys",dict1.keys()) #remove duplicates
print ("Duplicates are : ")
#print duplicates
for a_num in dict1:
    if dict1[a_num] > 1:
        print(a_num, "has occured", dict1[a_num], "times")
num_list=[10,10,11,12,11,14,12]
dup_dict={}
print ("list :",num_list)
for num in num_list: 
    if num in dup_dict:
        dup_dict[num] = dup_dict[num] + 1
    else:
       dup_dict[num] = 1
print ("dictionary : ",dup_dict)
print ("Duplicates in the list : ")       

for num in dup_dict:
    if dup_dict[num] > 1:
        print(num)
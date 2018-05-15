a_list= [2,4,5,6,7,8,3,5]
dup_dict={}
count = 0
for val in a_list:
    if val in dup_dict:
        count = 1
        break
        
    else:
        count = 0
if count == 1:
    print('it has duplicates')            

def avg(*a_list):
    total = 0
    for val in a_list:
        total += val
    return total/len(a_list)

average = avg(3,6,9) 
print(average)   
seq = []
for val in range(2000,3201):
    if(val % 7 == 0) and (val % 5 != 0):
        seq.append(str(val))
print(';'.join(seq))        
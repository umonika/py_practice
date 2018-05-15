def double_list(a_list):
    trk = 0
    while trk < len(a_list):
        a_list[trk] = 2 * a_list[trk]
        trk += 1
list1 = [4,5,6]            
print(list1)
double_list(list1)
print('*' * 5)
print(list1)

def repl(original,frm,to):
    return(original.replace(frm,to))
original = 'iron man' 
frm = 'iron'
to = 'spider'
print('original',original)
original = repl(original,frm,to)
print('after function')
print('original',original)   
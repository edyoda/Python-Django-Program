import pdb 

def linear_search(l,key):
    for value in l:
        if value == key:
            return True
    else:
        return False
    
def add(val1,val2):
    return val1 + val2

def sub(val1,val2):
    return val1 - val2


def mul(val1,val2):
    return val1 * val2


def div(val1,val2):
    return val1 / val2

pdb.set_trace()

l = [10,20,30,40,50]
key = 40 
print(linear_search(l,key))
import operator as op
def DuplicatesExist(op_tuple,orig_tuple):
    return ((len(set(op_tuple)) < len(orig_tuple)), len(set(op_tuple)))

def getOpTuple(initial_tuple, final_tuple, op):
    return tuple(map(op, final_tuple, initial_tuple))

def most_frequent(Tuple): 
    return max(set(Tuple), key = Tuple.count) 

def operateOnTuple(initial_tuple,final_tuple):
    diff_tuple = getOpTuple(initial_tuple,final_tuple,op.sub)
    div_tuple = getOpTuple(initial_tuple, final_tuple,op.truediv)
    exists, n = DuplicatesExist(diff_tuple, initial_tuple)
    exist, p = DuplicatesExist(div_tuple,initial_tuple)
    count = 0
    while(count < 3):
        if n < p and initial_tuple != final_tuple:
            if (0 in (diff_tuple)):
                #print(any(diff_tuple) == 0)
                initial_tuple = getOpTuple(initial_tuple,diff_tuple,op.add)
                count += 1
                print(count)
            else:
                n = most_frequent(list(diff_tuple))
                initial_tuple = getOpTuple(initial_tuple,(n,n,n),op.add)
                count += 1
                print(count)

        elif initial_tuple != final_tuple:
            initial_tuple = getOpTuple(initial_tuple,div_tuple,op.mul)
            count += 1
        else:
            #print(3)
            break
    print(count)
    print(initial_tuple)
        



for _ in range(int(input())):
    initial_tuple = tuple(map(int,input().split()))
    final_tuple = tuple(map(int,input().split()))
    operateOnTuple(initial_tuple,final_tuple)
"""
you are building a diving board by placing a bunch of planks of wood end to end 
there are two types of planks one of length shorter and one of length longer 
you must use exactly K planks of wood
write a method of generate all possible length for the diving board 
"""


def planking_brute(short, longer, k, lengths=set(), total=0):
    if k == 0:
        lengths.add(total) 
    else: 
        planking_brute(short, longer, k-1, lengths, total + short)
        planking_brute(short, longer, k-1, lengths, total + longer)
        
    return lengths

print planking_brute(1,2,3)

def planking(n, k, memo={0:0}):
    if k in memo:
        return memo[k]
    else:
        if k == 0:
            return memo[k]
        if k == 1:
            for i in n:
                lengths = set()
                lengths.add(i)
            memo[1] = lengths
            return memo[1]
        else:
            lengths = set()
            for i in range(k):
                lengths.add(planking(n, k-i, memo))
            memo[k] = lengths
    
    return memo[k]

#print planking([1,2], 3)

from timeit import timeit
def getperm_distinct(n):
    permutations = []
    if len(n) == 0:
        permutations.append("")
        return permutations
        
    for i in range(len(n)):
        before = n[:i]
        last = n[i+1:]
        partials = getperm_distinct(before + last)
        for k in partials:
            permutations.append(n[i] + k)
    return permutations

    
def getperm(n, freq = {}):
    if len(freq) == 0:
        for i in n:
            if n in freq:
                freq[n] += 1
            else:
                freq[n] = 1
    else:
        if len(n) == 0:
            permutations.append("")
            return permutations
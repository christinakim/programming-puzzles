"""
find pairs that equal sum

n = [3, 6, 7, 4]
target = 10
"""

def pairsum_brute(n, target):
    pairs = []
    for i in range(len(n)):
        for j in range(i + 1, len(n)):
            if n[i] + n[j] == target:
                pairs.append((n[i], n[j]))
    return pairs

def pairsum_sorted(n, target):
    n = sorted(n)
    i = 0
    j = len(n) - 1
    pairs = []
    while i < j:
        if n[i] + n[j] == target:
            pairs.append((n[i], n[j]))
            i += 1
            j -= 1
        elif n[i] + n[j] < target:
            i += 1
        else:
            j -= 1   
    return pairs

def pairsum_hash(n, s):
    hashset = set()
    pairs = []
    
    for i in range(len(n)):
        target = s - n[i]
        #this says if target is in hashset but the number we are looking at isnt, then that means that the target exists and we saw previously but we havent seen n[i] which means this is a unique pair to add now
        if target in hashset and n[i] not in hashset:
            pairs.append((n[i], target))
        hashset.add(n[i])
        
    return pairs
            
            

def main():
    n = [3, 6, 7, 4]
    target = 10
    
    assert pairsum_brute(n, 10) == [(3, 7), (6, 4)] 
    assert pairsum_sorted(n, 10) == [(3, 7), (4, 6)] 
    assert pairsum_hash(n, 10) == [(3, 7), (6, 4)] or [(7,3), (4,6)]
    print 'assertions passed!' 

if __name__ == '__main__':
    main()
                            
    


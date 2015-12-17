"""
given a string, produce k letter words
"""
import itertools

def perm1(lst):
    if len(lst) == 0:
        return []
    elif len(lst) == 1:
        return [lst]
    else:
        l = []
        for i in range(len(lst)):
            current = lst[i]
            rest = lst[:i] + lst[i+1:]
            for p in perm1(rest):
                l.append([current] + p)
        return l
        
def perm2(lst):
    if len(lst) == 0:
        yield []
    elif len(lst) == 1:
        yield lst
    else:
        for i in range(len(lst)):
            x = lst[i]
            xs = lst[:i] + lst[i+1:]
            for p in perm2(xs):
                yield [x] + p



def python_permutation(n, k):
    n = [n[i] for i in range(len(n))]

    return list(itertools.permutations(n, k))



if __name__ == '__main__':
	assert k_words("b", 2) == 'nada'
	assert k_words("bb", 0) == 'nada'
    print permutations_maybe("bb", 1)


	print "tests passed"
# input: 2 strings, pattern and test
# output: true if test matches the pattern

# pattern - 'abc', valid tests: 'abc', 'xac', invalid tests: 'aba', 'xxx'
# pattern - 'aba', valid: 'ded', 'xax'

# pattern: 'abca', test: 'defd'
# seen = {'a', 'b', 'c'}, dict: {a: [0,3], b: 1, c: 2}
def match(pattern, test):
    seen = ()
    dict = {}
    if len(pattern) == len(test):
        for i in range(len(pattern)):
            if pattern[i] in seen:
                dict[pattern[i]= dict.get(pattern[i]).append(i)
            else:
                seen.add(pattern[i])
                dict[pattern[i]] = [i]
        
        for j in range(len(test)):
            indicies = dict.get(j) 
            for i in indices:
                if test[j] == test[i]
                     
    else:
        return False
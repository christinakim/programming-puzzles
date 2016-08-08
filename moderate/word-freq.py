def freq(string, word):
    table = {}
    for i in string.split(' '):
        if i == word:
            count += 1

#if wanting to call this many times, first create a hash table of dictionary words and count
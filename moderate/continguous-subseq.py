"""you are given an array of ints(pos and neg).
find the continguous seq with the largest sum return the sum
"""

def seq_brute(n):
    largest = n[0]
    
    for i in range(len(n)):
        temp = n[i]
        for j in range(i + 1, len(n)):
            temp = temp + n[j]
            if temp > largest:
                largest = temp 
    return largest

def seq(n):
    i = 0
    j = 1
    temp = n[0]
    largest = n[0]
    while i < j and j < len(n):
        temp += n[j]
        if temp < 0:
            j += 2
            i = j - 1
            if i < len(n):
                temp = n[i]
        elif temp > largest:
            largest = temp
            j += 1
        else:
            j+= 1
    return largest
            
            
    
def main():
    n = [2, -8, 3, -2, 4, -10]
    print seq(n)
    
if __name__ == '__main__':
    main() 
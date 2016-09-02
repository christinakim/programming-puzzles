
def subsetsum(s, total):
    memo = [][]

    #if the sum is 0 then set doesnt matter because empty set will work
    for i in range(len(s)):
        memo[0][i] = True

    #if the sum is greater than 0 but set is 0 then there can be no subset
    for i in range(len(total)):
        memo[i][0] = False

    for i in range(1, len(total)):
        for j in range(1, len(s)):
            memo[i][j] = memo[i][j-1]
            

    return memo[total][s]
def main():
    s = [1,]
    subsetsum()
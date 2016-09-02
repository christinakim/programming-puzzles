"""
 A child is running up a stair case with n steps and hop either 1 step or 2 or 3 steps at a time. implement a method to cont how many possible ways the child can run up the stairs.

 need to sum all the permutations
 recurrence is for i in steps: 
 triple_step(n-i, steps)
"""

def triple_step(n, steps, memo = {0:1, 1:1}):
    #checking first if we've seen this case before
    if n in memo:
        print memo[n]
        return memo[n]
    elif n < 0:
        return 0
    else:
        """i =0 
        ways = 0
        while i < len(steps) and n >= steps[i]:
            ways += triple_step(n - steps[i], steps, memo)
            i += 1
        memo[n] = ways
        """

        memo[n] = triple_step(n-1, steps, memo) + triple_step(n-2, steps, memo) + triple_step(n-3,steps,memo)
        return memo[n]



def main():
    steps = [1,2,3]
    print triple_step(4, steps)

if __name__ == '__main__':
    main()


"""
for 3 steps
1,1,1,
2,1
1,2
3

for 4 steps
1,1,1,1

2,2 

1,1,2
1,2,1
2,1,1

1,3
3,1

for 5 steps:
1, 1, 1, 1, 1
1, 2, 1, 1, 1
1, 2, ,
2, 3
1, 1, 1, 2
3, 1, 1
2, 2, 1
"""
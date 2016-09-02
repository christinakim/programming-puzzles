# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"
from math import ceil

def solution(S):
    if len(S) == 0:
        return 0
   
    lines = S.split('\n')
    
    #storing calls where key = number and val = [call durations, costs]
    calls = {}
    costs = {}

    total = 0
    
    for i in range(len(lines)):
        line = lines[i].split(',')
        num = line[1]
        
        #convert hh:mm:ss string to seconds 
        h, m, s = line[0].split(':')
        dur = int(h) * 3600 + int(m) * 60 + int(s)
        
        #call is less than 300s -> 3 * seconds
        #call is => 300s --> 150 per * ceil(min)
        if dur < 300:
            cents = dur * 3
            total += cents
        else:
            cents = int(ceil(dur/60.0)) * 150  
            total += cents
            
        if num in calls:
            calls[num] += dur
            costs[num] += cents
        else:
            calls[num] = dur
            costs[num] = cents
            
    longest_dur = max(calls.values())
    
    longest = [key for key,value in calls.items() if value == longest_dur]
    long_intnum = int(longest[0].replace('-',''))
    longest_num = longest[0]
    if len(longest) > 1:
        for i in range(1,len(longest)):
            if long_intnum > int(longest[i].replace('-','')):
                long_intnum = int(longest[i].replace('-',''))
                longest_num = longest[i]
            
    
    remove = costs[longest_num]
    total -= remove

    return total
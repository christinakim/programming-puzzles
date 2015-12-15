# interval_overlap.py
"""
 You are given the start time and finish time of n intervals.
 You have to write a a function that returns the longest continuous interval if there
 was any overlapping interval in the set of existing intervals. (Sort and check, time complexity O(nlogn))
"""
def overlap(n):
  sorted_intervals = sorted(n)
  largest_interval = (0,0)
  start_time = 0

  start_list=[x[0] for x in sorted_intervals]
  end_list=[x[1] for x in sorted_intervals]
  for i in range(len(sorted_intervals)-1):
    if end_list[i] >= start_list[i+1]:
      if largest_interval == (0,0):
        start_time = start_list[i]
      largest_interval = (start_time, end_list[i+1]) 
    else:
      larget_interval=(0,0)
  return largest_interval

assert overlap([(1,2),(2,4),(3,3),(3,5)]) == (1,5)
assert overlap([(1,2),(3,4)]) == (0,0)
print 'all assertions passed!'


"""
Select the interval, x, with the earliest finishing time.
Remove x, and all intervals intersecting x, from the set of candidate intervals.
Continue until the set of candidate intervals is empty.
"""

def schedule_unweighted_intervals(meetings):
    '''Use greedy algorithm to schedule unweighted intervals
       sorting is O(n log n), selecting is O(n)
       whole operation is dominated by O(n log n)
    '''

    meetings.sort(lambda x, y: x.finish - y.finish)  # f_1 <= f_2 <= .. <= f_n

    O = []
    finish = 0
    for i in meetings:
        if finish <= i.start:
            finish = i.finish
            O.append(i)

def scheduling(intervals):
        starts, ends = [], []
        for i in range(len(intervals)):
            starts.append(intervals[i][0])
            ends.append(intervals[i][1])

        starts = sorted(starts)
        ends = sorted(ends)

        #index of start and end
        s, e = 0, 0
        min_rooms, cnt_rooms = 0, 0
        while s < len(starts):
            if starts[s] < ends[e]:
                cnt_rooms += 1  # Acquire a room.
                # Update the min number of rooms.
                min_rooms = max(min_rooms, cnt_rooms)
                s += 1
            else:
                cnt_rooms -= 1  # Release a room.
                e += 1

        return min_rooms


def main():
    meetings = [(12, 13),(13, 14), (15, 17)]
    meetings2 = [(12, 13),(12, 14), (15, 17)]
    meetings3 = [(1,2), (1,4), (4,5), (5,6), (5,6)]
    meetings4 = [(1,2), (2,3), (1,4), (3,5), (5,6), (5,6)]
    
    assert scheduling(meetings) == 1
    assert scheduling(meetings2) == 2
    assert scheduling(meetings3) == 2
    assert scheduling(meetings4) == 2
    
    
if __name__ == '__main__':
    main()

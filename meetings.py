#[(start, end), etc ]
def scheduling(meetings):
    sorted_meetings = sorted(meetings)
    current = sorted_meetings[0]
    max_rooms = 1
    in_use = {}
    
    for i in range(1, len(sorted_meetings)):
        if current[1] > sorted_meetings[i][0]:
            for room_num, end_time in in_use.iteritems():
                if sorted_meetings[i][0] > in_use[room_num]:
                    in_use[room_num] = sorted_meetings[i][1]
                else:
                    in_use[max_rooms+1] = sorted_meetings[i][1]
                    max_rooms += 1
    return max_rooms

def main():
    meetings = [(12, 13),(13, 14), (15, 17)]
    meetings2 = [(12, 13),(12, 14), (15, 17)]
    meetings3 = [(1,2), (1,4), (4,5), (5,6), (5,6)]
    meetings4 = [(1,2), (2,3), (1,4), (3,5), (5,6), (5,6)]
    
    assert scheduling(meetings) == 1
    assert scheduling(meetings2) == 2
    assert scheduling(meetings3) == 2
    # assert scheduling(meetings4) == 2
    
    
if __name__ == '__main__':
    main()

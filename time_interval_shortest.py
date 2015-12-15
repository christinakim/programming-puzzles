
""" Given a list of clock times, find the pair which has the smallest duration between them. 



For instance, if given 03:03, 02:15, 07:42, and 10:23, you should return the pair 02:15 and 03:03. 



Print out the number of minutes between and the two times in any order. For instance, the above set should return (48, 02:15, 03:03)

24 hours, "HH:MM"

 """   

def diff_times(first, second):
  hours = (int(second[0]) - int(first[0])) * 60
  min = int(second[1]) - int(first[1])

  temp = hours + min
  return temp    

def smallest_duration(n):
  sorted_times = sorted(n)
  print sorted_times

  smallest = 24 * 60
  start = ""
  end = ""

  for i in range(len(n)-1):
    first= sorted_times[i].split(":")
    second = sorted_times[i + 1].split(":")

    temp = diff_times(first, second)
    if temp < smallest:
        smallest = temp
        start = sorted_times[i]
        end = sorted_times[i+1]
  
  first= sorted_times[0].split(":")
  last = sorted_times[-1].split(":")
  #23:50 -> 24:00 + 0:00 -> 00:01

  temp = diff_times(last, [24,00] ) + diff_times([00,00],start)
  if temp < smallest:
    smallest = temp
    start = sorted_times[0]
    end = sorted_times[-1]
  

  return (smallest, start, end)

  

if  __name__ == '__main__':

  list_of_times = ["17:21", "23:50", "04:01", "07:07", "03:03", "00:01", "12:42", "16:03"]

  print smallest_duration(list_of_times)
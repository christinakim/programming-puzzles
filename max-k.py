import heapq

def max_k(n, k):
  heap = n[:k]
  print heap
  heapq.heapify(heap)

  for i in range(k,len(n)):
    print i
    if heap[0] < n[i]:
      heapq.heappushpop(heap,n[i])
      heapq.heapify(heap)
  
  return heap

def main():
  n = [1,2,3,4,5,6]
  k = 2
  assert max_k(n,k) == [5,6]
  
  print "tests passed!"

if __name__ == '__main__':
  main()

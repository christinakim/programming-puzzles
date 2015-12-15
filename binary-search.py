def binarysearch(n,k):
  sorted(n)
  if len(n) < 2:
    if n[-1] == k:
      return True
    elif n[0] == k:
      return True
    else: 
      print 'here'
      print n
      return False
  else: 
    a = n[:(len(n)/2)]
    b = n[(len(n)/2):]
    if a[-1] > k:
      return binarysearch(a,k)
    elif b[0] < k:
      return binarysearch(b,k)
    elif b[0] == k:
      return True
    elif a[-1] == k:
      return True

if __name__ == '__main__':
  n = [1, 2, 3, 4, 5, 6]
  m = [1, 2, 3, 4, 5, 6]
  assert binarysearch(n, 4) == True
  print binarysearch(m,0)

def duplicate(n):
  s = set()
  s.update(n)
  print s
  if len(s) == len(n):
    return False
  else:
    return True

if __name__ == '__main__':
  n = [1,1,1,3]
  m = [1,2,3,4]

  assert duplicate(n) == True
  assert duplicate(m) == False

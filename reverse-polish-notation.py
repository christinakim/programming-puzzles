import operator as op

def RPS(n):
  stack = []
  operands = {'+':op.add, '-':op.sub,'/':op.div,'*':op.mul}
  sub_sum = 0
  for i in range(len(n)):
    if n[i] in operands:
      second_int = stack.pop()
      first_int = stack.pop()
      operator = operands.get(n[i])
      sub_sum = operator(first_int, second_int)
      stack.append(sub_sum)
    else:
      stack.append(float(n[i]))
  return stack.pop()

def main():
  assert RPS("693/+2-") == 7
  print 'test passed'
if __name__ == '__main__':
  main()

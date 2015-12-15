class Node: 
  def __init__(self, value):
    self.value = value
    self.next = next

  def getValue(self):
    return self.value
  
  def getNext(self):
    return self.next

def generate_LL(): 
  head = Node(4)
  head.next = Node(5)
  head.next.next= Node(6)
  head.next.next = Node(7)
  return head

def main():
   LL = generate_LL()
   assert LL.next == Node(5)

if __name__ == '__main__':
  main()

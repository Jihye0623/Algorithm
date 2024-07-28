class DNode:
  def __init__(self, elem, prev=None, next=None):
    self.data = elem
    self.next= next
    self.prev = prev

  def append(self, node):
    if node is not None:
      node.next = self.next
      node.prev = self
      if node.next is not None:
        node.next.prev = node
      self.next = node

  def popNext(self):
    node = self.next
    if node is not None:
      self.next = node.next
      if self.next is not None:
        self.next.prev = self
    return node

class DblLinkedList:
  def __init__(self):
    self.head = None

  def isEmpty(self):
    return self.head == None

  def isFull(self):
    return False # 연결된 구조에서는 포화상태 없음

  def getNode(self, pos):
    if pos < 0: return None
    ptr = self.head
    for i in range(pos):
      if ptr == None:
        return None
      ptr = ptr.next
    return ptr
    
  def getEntry(self, pos):
    node = self.getNode(pos)
    if node == None: return None
    else: return node.data

  def size(self):
    ptr = self.head
    count = 0 
    while ptr is not None:
      ptr = ptr.next
      count +=1
    return count

  def display(self, msg='DblLinkedList:'):
    print(msg, end='')
    ptr = self.head
    while ptr is not None:
      print(ptr.data, end ='<=>')
      ptr = ptr.next
    print('None')

  def insert(self, pos, e):
    node = DNode(e)
    before = self.getNode(pos-1)
    if before == None:
      node.next = self.head
      if node.next is not None:
        node.next.prev = node
      self.head = node
    else: before.append(node)

  def delete(self, pos):
    before = self.getNode(pos-1)
    if before == None:
      before = self.head
      if self.head is not None:
        self.head = self.head.next
      if self.head is not None:
        self.head.prev = None
      return before
    else: before.popNext()

s = DblLinkedList()
s.display()
s.insert(0,10)
s.insert(0,20)
s.insert(1,30)
s.insert(s.size(),40)
s.insert(2,50)
s.display("연결리스트(삽입x5):")

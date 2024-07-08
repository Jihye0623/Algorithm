capacity = 10
array = [None] * capacity
top = -1 	

def isEmpty():
    if top == -1 : return True
    else: return False

def isFull(): return top == capacity

def pop():
    if not isEmpty():
        top -=1
        return array[top+1]
    else:
        print("stack underflow")
        exit()

def peek():
    if not isEmpty():
      return array[top]
    else: pass

def size(): return top+1
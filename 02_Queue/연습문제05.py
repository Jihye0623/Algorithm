from ArrayQueue import ArrayQueue

Q = ArrayQueue()

Q.enqueue(0)
Q.enqueue(1)
print("F(0) = 0")
print("F(1) = 1")

for i in range(2, 20) :
  val = Q.dequeue() + Q.peek()
  Q.enqueue(val)

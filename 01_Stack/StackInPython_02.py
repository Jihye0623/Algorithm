import queue

s = queue.LifoQueue(maxsize=20)

msg = input("input>>")
for c in msg:
  s.put(c)

print("output>>", end='')
while not s.empty():
  print(s.get(), end='')
print()
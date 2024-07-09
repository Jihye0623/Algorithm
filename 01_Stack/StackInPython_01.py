s = list()

msg = input("input:")
for c in msg:
  s.append(c)

print("output: ", end='')
while len(s)>0:
  print(s.pop(), end='')
print()
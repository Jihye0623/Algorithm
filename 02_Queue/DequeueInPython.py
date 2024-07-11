import collections

dq = collections.deque()

print("덱은 공백상태 아님"if dq else"덱은 공백상태")
for i in range(9):
  if i%2 == 0: dq.append(i)
  else: dq.appendleft(i)
print("홀수는 전단, 짝수는 후단 삽입", dq)

for i in range(2): dq.popleft()
for i in range(3): dq.pop()
print("전단 삭제 2번, 후단 삭제 3번", dq)

for i in range(9,14): dq.appendleft(i)
print("전단에 9~13 삽입", dq)

print("덱은 공백상태 아님"if dq else"덱은 공백상태")
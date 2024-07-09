def hanoi_tower(n, fr, tmp, to):  # 원판의 수, 시작 막대, 임시 막대, 목표 막대
  if (n==1):
    print("원판 1: %s ---> %s" % (fr, to))
  else:
    hanoi_tower(n-1, fr, to, tmp)
    print("원판 %d: %s ---> %s" % (n, fr, to))
    hanoi_tower(n-1, tmp, fr, to)

print(hanoi_tower(5, "a", "b", "c"))
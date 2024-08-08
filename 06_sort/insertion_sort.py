def insertion_sort(A):
  n = len(A)
  for i in range(1, n):
    key = A[i]
    j = i-1
    while j>=0 and key < A[j]:
      A[j+1] = A[j]
      j -= 1
    A[j+1] = key

data = [6,3,7,4,9,1,5,2,8]
print(data)
insertion_sort(data)
print(data)
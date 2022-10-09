n = int(input())
lst = []
for i in range(n):
    lst.append(int(input()))
m=lst[0]
for i in range(n):
 m=min(m,lst[i])
print(m)

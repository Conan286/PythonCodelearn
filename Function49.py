def get_unique_values(lst):
    map=[]
    for i in lst:
     if i not in map:
      map.append(i)
    return map


n = int(input())
lst = []
for i in range(n):
    lst.append(int(input()))
print(get_unique_values(lst))
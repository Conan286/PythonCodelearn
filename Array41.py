n=int(input())
a=[]
b=[]
i=0
j=0
for i in range (n):
 a.append(int(input()))
for i in range (n):
 if a[i]%5==0:
  b.insert(j,a[i])
  j=j+1
if j>0 :
 print(b)
else:
 print("[0]")
n = int(input())
i=1
s=0
while(i<=n):
 s+=i/(i+1)
 i+=1
print(round(s,2))
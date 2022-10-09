n = int(input())

def sumOfAll(n):
 s=1
 k=int(1+n/2)
 for i in range(2,k):
  if n%i==0:
   s+=i
 return s  
print(sumOfAll(n))
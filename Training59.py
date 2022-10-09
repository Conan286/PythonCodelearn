n = int(input())

def is_abundant(n):
 s=0
 k=int(1+n/2)
 for i in range(1,k):
   if n%i==0:
    s+=i
 if s>n :
  return True
 else:
  return False
print(is_abundant(n))

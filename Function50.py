def is_prime(n):
    cnt=0
    for i in range (1,n+1):
     if n%i==0:
      cnt+=1
     
    if cnt==2:
     return True
    return False


n = int(input())
print(is_prime(n))

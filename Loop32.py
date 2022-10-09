#Loop.py
a = int(input())
b = int(input())

i=a
if i%2==0: 
 i+=1
s=0
while i<=b:
 s+=i
 i+=2
print(s)

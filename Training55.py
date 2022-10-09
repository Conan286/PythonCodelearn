str = str(input())
def solve(str):
 s1=[]
 s=str.split(" ")
 for i in s:
    if len(i)>3:
        s1.append(i)
 return s1
print(solve(str))

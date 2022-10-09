s1 = input()
s2 = input()

tmp=s2[0:2]
s2=s1[0:2]+s2[2:]
s1=tmp+s1[2:]


print(s1 + " " + s2)
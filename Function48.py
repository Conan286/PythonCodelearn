def show(s):
    up=0
    low=0
    for i in s:
      if i.isupper():
       up+=1
      elif i.islower():
       low+=1
    print("Given string:",s)
    print("Number of uppercase letters:",up)
    print("Number of lowercase letters:",low)


s = str(input())
show(s)
s = str(input())

def format(s):
 if len(s)<3:
  return s
 else:
  if s[-3:]=="ing":
   s=s+"ly"
  else:
   s=s+"ing"
 return s
print(format(s))
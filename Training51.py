#Initial list
res = []

# Input lengths
lengths = int(input())

# Add element
for i in range(lengths):
    # Input elements
    n = int(input())
    res.append(n)
print(evenNum(res))

def evenNum(res):
 even=[]
 for i in res:
  if i%2==0:
   even.append(i)
 return even
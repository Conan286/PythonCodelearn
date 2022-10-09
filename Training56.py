#Initial list
res = []

# Input lengths
lengths = int(input())

# Add element
for i in range(lengths):
    # Input elements
    n = int(input())
    res.append(n)

s=""
for i in range(lengths):
 s+=str(res[i])
print(s)
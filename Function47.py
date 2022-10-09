def max3(a, b, c):
    max1=max(a,b)
    max2=max(max1,c)
    return max2


a = int(input())
b = int(input())
c = int(input())
print(max3(a, b, c))

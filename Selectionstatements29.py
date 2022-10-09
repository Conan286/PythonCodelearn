a = int(input())
b = int(input())
c = int(input())
avg = (a+b+c)/3;

if avg>a and avg>b: 
 print("The average value is greater than both a and b")
elif avg>a and avg>c:
 print("The average value is greater than both a and c")
elif avg>c and avg>b:
 print("The average value is greater than both b and c")
elif avg>a:
 print("The average value is greater than a")
elif avg>b:
 print("The average value is greater than b")
elif avg>c:
 print("The average value is greater than c")
'''
7. Phương thức split()

Phương thức này được dùng để cắt một chuỗi ra thành list các chuỗi khác dựa trên một phần tử trong chuỗi đầu vào:

s = "Welcome to Codelearn.io!"
print(s.split(" "))
s = "A1B1C1D1E1"
print(s.split("1"))
Kết quả khi chạy chương trình:

['Welcome', 'to', 'Codelearn.io!']
['A', 'B', 'C', 'D', 'E', '']
8. Phương thức join()

Phương thức này được dùng để nối một tập hợp thành một chuỗi sử dụng kí tự cho trước. Ví dụ:

lst = ["Welcome", "to", "Codelearn.io!"]
print(" ".join(lst))
lst = ["A", "B", "C"]
print("-".join(lst))
Kết quả khi chạy chương trình:

Welcome to Codelearn.io!
A-B-C
Bạn có thể sử dụng hàm split() và hàm join() để loại bỏ các khoảng trắng thừa trong chuỗi. Ví dụ:

message = "   Welcome   to Codelearn.io!   "
print(" ".join(message.split()))
Kết quả khi chạy chương trình:

Welcome to Codelearn.io!
'''
s = str(input())

a=s.split(" ")
a.reverse()
print(" ".join(a))


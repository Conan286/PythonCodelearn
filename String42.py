'''
String functions and methods in Python

1. len() function

It returns the number of items in a string:

s = "abc"
print(len(s))
s = "abcd"
print(len(s))
When the code is compiled and executed, it produces the following result:

3
4
2. lower() method

It converts all uppercase characters in a string into lowercase characters and returns it.

s = "CODELEARN123"
print(s.lower())
When the code is compiled and executed, it produces the following result:

codelearn123
3. upper() method

It converts all lowercase characters in a string into uppercase characters and returns it.

s = "codelearn123"
print(s.upper())
When the code is compiled and executed, it produces the following result:

CODELEARN123
4. isalnum() method

It returns True if all characters in the string are alphanumeric (either alphabets or numbers). If not, it returns False.

s = "codelearn2020"
print(s.isalnum())
s = "codelearn2020.io"
# It returns False because string s contains special character
print(s.isalnum())
When the code is compiled and executed, it produces the following result:

True
False
5. isalpha() method

It returns True if all characters in the string are alphabets. If not, it returns False.

s = "codelearn"
print(s.isalpha())
# It returns False because string s contains numbers
s = "codelearn2020"
print(s.isalpha())
When the code is compiled and executed, it produces the following result:

True
False
6. isnumeric() method

It returns True if all characters in a string are numeric characters. If not, it returns False.

s = "2020"
print(s.isnumeric())
s = "c2020"
print(s.isnumeric())
When the code is compiled and executed, it produces the following result:

True
False
7. split() method

It splits a string into a list of strings at the specified separator.

s = "Welcome to Codelearn.io!"
print(s.split(" "))
s = "A1B1C1D1E1"
print(s.split("1"))
When the code is compiled and executed, it produces the following result:

['Welcome', 'to', 'Codelearn.io!']
['A', 'B', 'C', 'D', 'E', '']
8. join() method

It returns a string by joining all the elements of an iterable, separated by a string separator.

lst = ["Welcome", "to", "Codelearn.io!"]
print(" ".join(lst))
lst = ["A", "B", "C"]
print("-".join(lst))
When the code is compiled and executed, it produces the following result:

Welcome to Codelearn.io!
A-B-C
You can use both the split() method and the join() method to remove redundant blank spaces in a string. Example:

message = "   Welcome   to Codelearn.io!   "
print(" ".join(message.split()))
When the code is compiled and executed, it produces the following result:

Welcome to Codelearn.io!
9. replace() method

It returns a copy of the given string where all occurrences of a substring are replaced with another substring.

name = "Cod3l3arn"
print(name.replace("3", "e"))
When the code is compiled and executed, it produces the following result:

Codelearn
'''
s=str(input())
print(s.upper())
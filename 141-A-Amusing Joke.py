#from collections import Counter
a = input()
b = input()
s = input()
if sorted(a+b) == sorted(s):
    print('YES')
else:
    print('NO')
# a = sorted(a)
# b = sorted(b)
# s = sorted(s)
# c = a+b
# if Counter(c) == Counter(s):
#     print('YES')
# else:
#     print('NO')

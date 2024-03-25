from collections import Counter
a = input()
b = input()
s = input()
a = sorted(a)
b = sorted(b)
s = sorted(s)
c = a+b
if Counter(c) == Counter(s):
    print('YES')
else:
    print('NO')

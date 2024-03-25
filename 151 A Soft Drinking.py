n, k, l, c, d, p, nl, np = map(int, input().split())
toasts = (k*l) // nl
limes = c*d
salt = p // np
res = min(toasts, limes, salt) // n
print(res)

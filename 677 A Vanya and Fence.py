n, h = map(int, input().split())
heights = list(map(int, input().split()))
wide = 0
for height in heights:
    if height > h :
        wide += 2
    else:
        wide += 1
print(wide)

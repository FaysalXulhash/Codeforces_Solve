n, k = map(int, input().split())
advance = 0
place = list(map(int, input().split()))
for i in place:
    if i >= place[k-1] and i>0:
        advance += 1
print(advance)

n = int(input())
free_room = 0
for _ in range(n):
    p, q = map(int, input().split())
    if q > p+1:
        free_room += 1
print(free_room)

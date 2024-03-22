n = int(input())
magnates = []
count_group = 1
for i in range(n):
    magnates.append(int(input()))

for i in range(0, n-1):
    if magnates[i] != magnates[i+1]:
        count_group += 1

print(count_group)

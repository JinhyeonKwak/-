n = int(input())
array = list(map(int, input().split()))

d = [0] * 101
d[1] = array[0]

for i in range(2, n+1):
    d[i] = max(d[i-1], d[i-2]+array[i-1])

print(d[n])




# 바닥 공사

n = int(input())
d = [0] * 1001
d[0], d[1] = 1, 1
for i in range(2, n+1):
    d[i] = d[i-1] + 2*d[i-2]

result = d[n] % 796796
print(result)
# 큰 수의 법칙

n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
max1 = data[-1]
max2 = data[-2]

result = (max1 * k + max2) * (m // (k + 1)) + (m % (k + 1)) * max1
print(result)
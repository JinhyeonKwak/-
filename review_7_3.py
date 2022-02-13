# 떡볶이 떡 만들기

n, m = map(int, input().split())
array = list(map(int, input().split()))

start = 0
end = max(array)

result = 0
while start <= end:
    mid = (start + end) // 2
    total = 0
    for x in array:
        tmp = x - mid
        if tmp > 0:
            total += tmp
    if total < m:
        end = mid - 1
    elif total > m:
        start = mid + 1
        result = mid
    else:
        result = mid
        break

print(result)


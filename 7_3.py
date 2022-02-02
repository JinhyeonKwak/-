# 떡볶이 떡 만들기

n, m = map(int, input().split())
data = list(map(int, input().split()))
data.sort()

# 재귀 함수 사용 : 논리적 결함 포함
# 현재 얻을 수 있는 떡볶이의 양에 따라서 자를 위치를 결정해야 하기 때문에
# 이를 재귀적으로 구현하는 것은 귀찮은 작업이 될 수 있다.
# def binary_search(array, target, start, end):
#     if start > end:
#         return None
#     mid = (start + end) // 2
#     total = 0
#     for x in array:
#         if x > mid:
#             total += (x - mid)
#     if total > target:
#         return binary_search(array, target, mid+1, end)
#     elif total < target:
#         return binary_search(array, target, start, mid-1)
#     else:
#         return mid
#
# result = binary_search(data, m, 0, data[-1])
# print(result)


# 반복문 사용

start = 0
end = max(data)

result = 0
while start <= end:
    mid = (start + end) // 2
    total = 0

    for x in data:
        if x > mid:
            total += (x - mid)
    if total < m:
        end = mid - 1
    else:
        result = mid
        start = mid + 1

print(result)



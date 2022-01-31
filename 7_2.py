# 부품 찾기

n = int(input())
n_data = list(map(int, input().split()))
n_data.sort()
m = int(input())
m_data = list(map(int, input().split()))


def binary_search(array, target, start, end):
    if start > end:
        return "no"
    mid = (start + end) // 2
    if array[mid] == target:
        return "yes"
    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)
    else:
        return binary_search(array, target, mid + 1, end)


for i in range(m):
    target = m_data[i]
    result = binary_search(n_data, target, 0, n-1)
    print(result, end=' ')


# 계수 정렬

# count = [0] * (max(n_data) + 1)
#
# for x in n_data:
#     count[x] += 1
#
# for target in m_data:
#     if count[target]:
#         print("yes", end=' ')
#     else:
#         print("no", end=' ')


# 집합 자료형 이용

# n = int(input())
# array = set(map(int, input().split()))
# m = int(input())
# x = list(map(int, input().split()))
#
# for i in x:
#     if i in array:
#         print("yes", end=' ')
#     else:
#         print("no", end=' ')



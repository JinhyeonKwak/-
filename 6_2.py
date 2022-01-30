# 위에서 아래로

n = int(input())
# data = [int(input()) for _ in range(n)]
array = []
for i in range(n):
    array.append(int(input()))

array = sorted(array, reverse=True)

for num in array:
    print(num, end=' ')


# 선택 정렬
# for i in range(len(data)):
#     max_index = i
#     for j in range(i+1, len(data)):
#         if data[j] > data[max_index]:
#             data[max_index], data[j] = data[j], data[max_index]
#
# print(data)


# 삽입 정렬
# for i in range(1, len(data)):
#     for j in range(i, 0, -1):
#         if data[j] > data[j-1]:
#             data[j-1], data[j] = data[j], data[j-1]
#         else:
#             break
#
# for num in data:
#     print(num, end=' ')


# 퀵 정렬 1
# def quick_sort(array):
#     if len(array) <= 1:
#         return array
#
#     pivot = array[0]
#     tail = array[1:]
#
#     left_side = [x for x in tail if x >= pivot]
#     right_side = [x for x in tail if x < pivot]
#
#     return left_side + [pivot] + right_side
#
# result = quick_sort(data)
#
# for num in result:
#     print(num, end=' ')



# 퀵 정렬 2
# def quick_sort(array, start, end):
#     if start >= end:
#         return
#
#     pivot = start
#     left = start + 1
#     right = end
#
#     while left <= right:
#         while left <= end and array[left] <= array[pivot]:
#             left += 1
#         while right > start and array[right] >= array[pivot]:
#             right -= 1
#         if left > right:
#             array[pivot], array[right] = array[right], array[pivot]
#         else:
#             array[left], array[right] = array[right], array[left]
#
#     quick_sort(array, start, right-1)
#     quick_sort(array, right+1, end)
#
# quick_sort(data, 0, len(data)-1)
# data.reverse()
# for num in data:
#     print(num, end=' ')



# 계수 정렬
# count = [0] * (max(data) + 1)
#
# for i in range(len(data)):
#     count[data[i]] += 1
#
# for i in range(len(count)-1, -1, -1):
#     for j in range(count[i]):
#         print(i, end=' ')

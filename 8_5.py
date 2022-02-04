# 효율적인 화폐 구성

n, m = map(int, input().split())
coins = [int(input()) for _ in range(n)]
coins.sort(reverse=True)

# result = 0
# for i in range(len(coins)):
#     if coins[i] <= m:
#         k = m // coins[i]
#         m -= k * coins[i]
#         result += k
#         if m == 0:
#             break
#         if i < len(coins) - 1:
#             if m < coins[i+1]:
#                 m += coins[i]
#                 result -= 1
#
# if m == 0:
#     print(result)
# else:
#     print(-1)




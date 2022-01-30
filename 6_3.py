# 성적이 낮은 순서로 학생 출력하기

n = int(input())

data = []
for i in range(n):
    tmp = input().split()
    data.append((tmp[0], int(tmp[1])))

result = sorted(data, key=lambda student: student[1])
for x in result:
    print(x[0], end=' ')






# 정수 N을 입력받기
n = int(input())
# 모든 식량 정보 입력받기
array = list(map(int, input().split()))

# DP테이블

d = [0] * 100

# 다이나미 그포그래밍(보텀업)

d[0] = array[0]
d[1] = max(array[0], array[1])
for i in range(n):
    d[i] = max(d[i-1], d[i-2] + array[i])
    print(d[i])

#계산된 결과 출력
print(d[n-1])

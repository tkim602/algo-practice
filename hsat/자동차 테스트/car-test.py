from bisect import bisect_left

n, q = map(int, input().split())
efficiency = list(map(int, input().split()))
m = [int(input()) for _ in range(q)]

# Please write your code here.

# 연료소모 적고 주행거리 높게 

# 3개씩만 가능하고, m이 중앙값이 될 수 있는 경우의 수
# m 보다 큰 수의 개수 * m 보다 작은 수의 개수

# l = efficiency.index(m)

# print(efficiency)
efficiency.sort()

for mi in m:
    idx = bisect_left(efficiency, mi)

    if idx == n or efficiency[idx] != mi:
        print(0)
        continue

    left = idx
    right = n - idx - 1

    print(left * right)

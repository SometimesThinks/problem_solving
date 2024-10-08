import sys

input = sys.stdin.readline

n = int(input().rstrip())
dp = [0 for _ in range(n + 1)]
dp[0] = 1

for i in range(1, n + 1):
    res = 0
    for j in range(i):
        res += dp[j] * dp[i - 1 - j]
    dp[i] = res

print(dp[n])

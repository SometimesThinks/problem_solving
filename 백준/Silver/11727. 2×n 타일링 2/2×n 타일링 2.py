import sys

input = sys.stdin.readline

n = int(input().rstrip())
dp = [0 for _ in range(n + 1)]
dp[0] = 1
dp[1] = 3

for i in range(2, n + 1):
    dp[i] = dp[i - 1] + 2 * (dp[i - 2])

print(dp[n - 1] % 10007)

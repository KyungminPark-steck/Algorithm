import sys
int_num = sys.maxsize 

n, m = list(map(int, input().split()))

coin = [0] + list(map(int, input().split()))


dp = [int_num for _ in range(m+1)]
dp[0] = 0


for i in range(1, m+1):
    for j in range(1, n+1):
        if i >= coin[j]:
            dp[i] = min(dp[i], dp[i-coin[j]]+1)
            
ans = dp[m] 

if ans == int_num:
	ans = -1
print(ans)

#####

n = int(input())

a = [0] + list(map(int, input().split()))

dp = [0 for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(i):
        if a[j] < a[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))

######

import sys

int_min = -sys.maxsize

n = int(input())

a = [
    list(map(int, input().split()))
    for _ in range(n)
]

dp = [[0]*n for _ in range(n)]

def initialize():
    dp[0][0] = a[0][0]

    for i in range(1,n):
        dp[i][0] = dp[i-1][0] + a[i][0]

    for i in range(1,n):
        dp[0][i] = dp[0][i-1] + a[0][i]

    
initialize()

for i in range(1,n):
    for j in range(1,n):
        dp[i][j] = max(dp[i][j-1], dp[i-1][j]) + a[i][j]

print(dp[n-1][n-1])

#######

n = int(input())
memo = [-1] * (n+1)
def fibbo(n):
    if memo[n] != -1:
        return memo[n]
    if n <= 2:
        memo[n] = 1
    else:
        memo[n] = fibbo(n-2) + fibbo(n-1)
    return memo[n]

print(fibbo(n))

######

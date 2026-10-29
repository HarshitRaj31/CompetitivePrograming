#Given a non-negative integer n, find the n-th Fibonacci number using bottom-up
#dynamic programming
def fibonacci(n):
    if n <= 1:
        return n

    dp=[0]*(n + 1)
    dp[0]=0
    dp[1]=1

    for i in range(2, n + 1):
        dp[i]=dp[i-1]+dp[i-2]

    return dp[n]


n = int(input("Enter n: "))
print("Fibonacci number:", fibonacci(n))

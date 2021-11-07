# AtCoder Educational DP Contest A - Frog 1
# there are N steps and the hieght of step_i is h_i
# frog starts from step_0 and select the following actions
# 1. move from step_i to step_i+1, cost is h_i-h_i+1
# 2. move from step_i to step_i+2, cost is h_i-h_i+2
# calculate minimum sum of cost from step_0 to step_N-1
# considering relaxation
# O(N)

INF = 20000

# function to choose minimum
# list is mutable
# i -> i+1, i+2
# push-based pattern
def ch_min(dp, h, i, N):
    if (i+1) < N:
        if dp[i+1] > (dp[i] + abs(h[i] - h[i+1])):
                dp[i+1] = (dp[i] + abs(h[i] - h[i+1]))
    if (i+2) < N:
        if dp[i+2] > (dp[i] + abs(h[i] - h[i+2])):
                dp[i+2] = (dp[i] + abs(h[i] - h[i+2]))

def main():
    h = [2, 9, 4, 5, 1, 6, 10]
    
    N = len(h)
    
    dp = [INF] * N
    dp[0] = 0
    
    for i in range(N):
        ch_min(dp, h, i, N)
    
    print(dp[N-1])

if __name__ == "__main__":
    main()
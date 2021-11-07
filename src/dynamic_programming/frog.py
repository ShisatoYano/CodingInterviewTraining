# AtCoder Educational DP Contest A - Frog 1
# there are N steps and the hieght of step_i is h_i
# frog starts from step_0 and select the following actions
# 1. move from step_i to step_i+1, cost is h_i-h_i+1
# 2. move from step_i to step_i+2, cost is h_i-h_i+2
# calculate minimum sum of cost from step_0 to step_N-1
# O(N)

def main():
    h = [2, 9, 4, 5, 1, 6, 10]
    
    N = len(h)
    
    dp = [2^60] * N
    dp[0] = 0
    
    for i in range(1, N):
        if i == 1: dp[i] = abs(h[i] - h[i-1])
        else: dp[i] = min([dp[i-1] + abs(h[i] - h[i-1]),
                          dp[i-2] + abs(h[i] - h[i-2])])
    
    print(dp[N-1])

if __name__ == "__main__":
    main()
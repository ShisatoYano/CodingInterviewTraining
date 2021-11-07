# AtCoder Educational DP Contest A - Frog 1
# there are N steps and the hieght of step_i is h_i
# frog starts from step_0 and select the following actions
# 1. move from step_i to step_i+1, cost is h_i-h_i+1
# 2. move from step_i to step_i+2, cost is h_i-h_i+2
# calculate minimum sum of cost from step_0 to step_N-1
# using recursive function
# O(N)

# input data
h = [2, 9, 4, 5, 1, 6, 10]
N = len(h)

# table to memorize
INF = 20000
dp = [INF] * N

# function to choose minimum
# list is mutable
# i <- i-1, i-2
# pull-based pattern
def ch_min(a, b):
    if a > b: return b
    else: return a

def rec(i):
    # value in dp was updated
    if dp[i] < INF: return dp[i]
    
    # base case
    if i == 0: return 0
    
    # initialize result
    result = INF
    
    # moved from step i-1
    result = ch_min(result, rec(i-1) + abs(h[i] - h[i-1]))
    
    # moved from step i-2
    if i > 1:
        result = ch_min(result, rec(i-2) + abs(h[i] - h[i-2]))
    
    dp[i] = result
    
    return dp[i]

def main():
    print(rec(N - 1))

if __name__ == "__main__":
    main()
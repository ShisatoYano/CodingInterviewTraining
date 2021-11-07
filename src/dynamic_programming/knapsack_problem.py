# knapsack problem
# there are N objects. an object_i has weight and value.
# choose some objects and sum of weights should not be over than W
# calculate maximum sum of value
# W and weight_i are over than 0
# dp[i][w], i=0,1,...,i-1 w=0,1,...,W
# i個の品物までの中から重さがwを超えないように選んだときの価値の総和の最大値
# O(NW)

def ch_max(a, b):
    if a < b:
        return b
    else:
        return a

def main():
    weight = [2, 1, 3, 2, 1, 5]
    value = [3, 2, 6, 1, 3, 85]
    
    # DP table
    N = len(weight)
    W = 15
    dp = [[0]*(W+1) for i in range(N+1)]
    
    # DP loop
    for i in range(N):
        for w in range(W+1):
            # choose object_i
            if (w - weight[i]) >= 0:
                dp[i+1][w] = ch_max(dp[i+1][w], dp[i][w-weight[i]]+value[i])
            # not choose object_i
            dp[i+1][w] = ch_max(dp[i+1][w], dp[i][w])
    
    # output maximum sum of value
    print(dp[N][W])

if __name__ == "__main__":
    main() 
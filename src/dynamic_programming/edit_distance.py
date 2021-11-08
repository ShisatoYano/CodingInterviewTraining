# edit distance
# calculating similarity string T with string S
# you want to convert from string S to string T by
# the following three operations
# 1. choose one of char in string S and change to optional char
# 2. choose one of char in string S and delete it
# 3. insert a char into a plcace you want
# calculate minimum operation times
# dp[i][j] <- edit distance between init i chars in S and init j chars in T

INF = 2**29

def ch_min(a, b):
    if a > b:
        return b
    else:
        return a

def main():
    S = "logistic"
    T = "algorithm"
    
    # DP table
    dp = [[INF]*(len(T)+1) for i in range(len(S)+1)]
    
    # initialize
    dp[0][0] = 0
    
    # DP loop
    for i in range(len(S)+1):
        for j in range(len(T)+1):
            # change
            if (i > 0) and (j > 0):
                if S[i-1] == T[j-1]:
                    dp[i][j] = ch_min(dp[i][j], dp[i-1][j-1])
                else:
                    dp[i][j] = ch_min(dp[i][j], dp[i-1][j-1] + 1)
            
            # delete
            if i > 0: dp[i][j] = ch_min(dp[i][j], dp[i-1][j] + 1)
            
            # insert
            if j > 0: dp[i][j] = ch_min(dp[i][j], dp[i][j-1] + 1)
    
    # output maximum sum of value
    print(dp[len(S)][len(T)])

if __name__ == "__main__":
    main()
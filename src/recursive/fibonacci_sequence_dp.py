# fibonacci sequence
# F_0 = 0
# F_1 = 1
# F_N = F_N-1 + F_N-2(N=2,3,...)
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55,...
# memorize already calculated function
# dynamic programming
# O(N)

# array to memorize fibo(N)
memo = [-1] * 50

def fibo(N):
    # base case
    if N == 0: return 0
    elif N == 1: return 1
    
    # check memo (return answer if already calculated)
    if memo[N] != -1: return memo[N]
    
    # calculate recursively in memorizing answer
    memo[N] = fibo(N-1) + fibo(N-2)
    return memo[N]

def main():
    fibo(49)
    
    # answer is stored in memo[0], ..., memo[49]
    for N in range(2, 50):
        print("{} item: {}".format(N, memo[N]))

if __name__ == "__main__":
    main()
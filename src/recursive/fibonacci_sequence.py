# fibonacci sequence
# F_0 = 0
# F_1 = 1
# F_N = F_N-1 + F_N-2(N=2,3,...)
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55,...
# fibo(N): O((1+sqr(5)/2)^N)

def fibo(N):
    # recursive function was called
    print("fibo({}) was called".format(N))
    
    # base case
    if N == 0: return 0
    elif N == 1: return 1
    
    # calculate answer recursively
    result = fibo(N-1) + fibo(N-2)
    print("{} item = {}".format(N, result))
    
    return result

def main():
    fibo(6)

if __name__ == "__main__":
    main()
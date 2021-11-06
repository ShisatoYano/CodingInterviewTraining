def func(N):
    # report recursive function was called
    print("func({}) was called".format(N))
    
    if N == 0: return 0 # base case
    
    # calculate recursively
    result = N + func(N - 1)
    print("Sum until {} = {}".format(N, result))
    
    return result

def main():
    func(5)

if __name__ == "__main__":
    main()
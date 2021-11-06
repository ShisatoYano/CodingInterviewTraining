# partial sum problem
# check sum W can be calculated by selecting some values
# from a_0, a_1, ..., a_N-1
#
# sub problem 1: W can be calculated from a_0, ..., a_N-2
# sub problem 2: W-a_N-1 can be calculated from a_0, ..., a_N-2
# if 1 or 2 was true at least, original problem would be true too
# W-N
# 0-0 -> 3-1 -> 3-2 -> 9-3 -> 14-4
# worst case of calling base case: 2^N times
# O(2^N)

def func(i, W, a):
    # base case
    if i == 0:
        if W == 0: return True
        else: return False
    
    # not select a[i-1]
    if func(i-1, W, a): return True
    
    # select a[i-1]
    if func(i-1, W-a[i-1], a): return True
    
    return False

def main():
    N = 4
    
    W = 14
    
    a = [3, 2, 6, 5]
    
    # calculate recursively
    if func(N, W, a): print("Yes");
    else: print("No")

if __name__ == "__main__":
    main()

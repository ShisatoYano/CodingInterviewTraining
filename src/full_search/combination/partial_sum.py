import random

def main():
    N = 10
    
    W = 10
    
    a = random.sample(range(20), k=N)
    print("a(N):", a)
    
    # linear search
    exist = False
    for bit in range(1 << N): # total 2^N patterns combination
        sum_value = 0
        
        for i in range(N):
            # check a[i] is included in partial sum
            if (bit & (1 << i)):
                sum_value += a[i]
        
        # check sum is W
        if sum_value == W:
            exist = True
    
    if exist: print("Yes")
    else: print("No")

if __name__ == "__main__":
    main()
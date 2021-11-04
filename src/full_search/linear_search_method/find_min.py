from math import inf
import random

def main():
    N = int(input("size of sequence: "))
    
    print("N: {}".format(N))
    
    a = random.sample(range(20000000), k=N)
    print(a)
    
    # linear search
    min_value = inf
    for i in range(N):
        if a[i] < min_value:
            min_value = a[i]
    
    # output result
    print("Minimum value: {}".format(min_value))

if __name__ == "__main__":
    main()
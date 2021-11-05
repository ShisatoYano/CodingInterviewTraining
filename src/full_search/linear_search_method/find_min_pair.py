import random

def main():
    N = 10
    
    K = 5
    
    a = random.sample(range(20), k=N)
    print("a(N):", a)
    
    b = random.sample(range(20), k=N)
    print("b(N):", b)
    
    # linear search
    min_value = float("inf")
    for i in range(N):
        for j in range(N):
            if (a[i] + b[j]) < K:
                continue
            if (a[i] + b[j]) < min_value:
                min_value = (a[i] + b[j])
    
    # result
    print("min value: ", min_value)

if __name__ == "__main__":
    main()
import random

def main():
    N = int(input("size of sequence: "))
    
    v = int(input("target value: "))
    
    print("N:{} v:{}".format(N, v))
    
    a = random.sample(range(100), k=N)
    print(a)
    
    # linear search
    exist = False
    for i in range(N):
        if a[i] == v:
            exist = True
    
    # output result
    if exist: print("Yes")
    else: print("No")

if __name__ == "__main__":
    main()
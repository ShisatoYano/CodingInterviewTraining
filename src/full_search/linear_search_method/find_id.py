def main():
    N = int(input("size of sequence: "))
    
    v = int(input("target value: "))
    
    print("N:{} v:{}".format(N, v))
    
    a = [0] * N
    for i in range(N):
        a[i] = i
    print(a)
    
    # linear search
    found_id = -1
    for i in range(N):
        if a[i] == v:
            found_id = i
            break
    
    # output result
    print("Found ID: {}".format(found_id))

if __name__ == "__main__":
    main()
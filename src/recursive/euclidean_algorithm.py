# calculate greatest common divisor of m and n
# m / n = a and remainder r
# GCD(m, n) = GCD(n, r), m >= n > 0
# O(log n)

def gcd(m, n):
    # base case
    if n == 0: return m
    
    # recursive call
    return gcd(n, m % n)

def main():
    print(gcd(51, 15)) # result: 3
    print(gcd(15, 51)) # result: 3

if __name__ == "__main__":
    main()
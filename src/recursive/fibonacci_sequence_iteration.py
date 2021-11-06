# fibonacci sequence
# F_0 = 0
# F_1 = 1
# F_N = F_N-1 + F_N-2(N=2,3,...)
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55,...
# calculate by for loop iteration only N-1 times
# O(N)

def main():
    F = [0] * 50
    F[0], F[1] = 0, 1
    for N in range(2, 50):
        F[N] = F[N-1] + F[N-2]
        print("{} item: {}".format(N, F[N]))

if __name__ == "__main__":
    main()
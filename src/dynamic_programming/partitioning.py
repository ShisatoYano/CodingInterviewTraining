# optimize partitioning
# N個の並んだ要素にはN+1個の隙間がある
# N+1個の隙間から２個を選ぶことが区間を作ることになる
# 選んだ隙間が2~6なら、区間は[2,6)と表す
# この区間に含まれるのは2,3,4,5まで
# 
# いくつかの区間に分割し、各区間にはスコアが付いている
# KをN以下の正の整数とし、K+1個の整数t0,t1,...tkをとる
# 0 = t0 < t1 < ... tk = Nを満たすように
# 区間分割[t0, t1), [t1, t2),...,[tK-1, tK)のスコアを
# c_t0,t1 + c_t1,t2 + ... + c_tK-1,tKと定義する
# N要素の区間分割の仕方をすべて考えたときの、考えられるスコアの最小値を求める
# 
# 区間を分割していく動的計画法
# dp[i] <- 区間[0,i)について、いくつかの区間に分解する最小コスト
# 区間[0,i)を分割する方法のうち、最後に区切る場所がどこかで場合分け
# 最後に区切る位置がjとすると、
# 区間[0,i)の分割は、区間[0,j)の分割に対して新たに区間[j,i)を追加したものとみなせる
# ch_min(dp[i], dp[j]+c[j][i])

import random

INF = 2**60

def ch_min(a, b):
    if a > b:
        return b
    else:
        return a

def main():
    N = 10
    
    c = [[0]*(N+1) for i in range(N+1)]
    for i in range(0, N+1):
        for j in range(0, N+1):
            c[i][j] = random.randint(1, 20)
    
    dp = [INF] * (N+1)
    dp[0] = 0
    
    for i in range(N+1):
        for j in range(i):
            dp[i] = ch_min(dp[i], dp[j]+c[j][i])
    
    print(dp[N])

if __name__ == "__main__":
    main()
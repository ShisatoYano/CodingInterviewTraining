# ペア和のK以上の中での最小値
# N個の整数a0, a1, ..., aN-1と
# N個の整数b0, b1, ..., bN-1が与えられる
# 2組の整数列から1個ずつ整数を選んで和をとる
# その和として考えられる値のうち、整数K以上の範囲内での最小値を求める
#
# aiを選ぶ方法を固定して考える
# N個の整数b0, b1, ..., bN-1が与えられる
# このうち、K-ai以上の範囲内での最小値を求める

import bisect

INF = 200000000

def main():
    # 配列の用意
    N = int(input("Input N: "))
    K = int(input("Input K: "))
    a, b = [0]*N, [0]*N
    
    # 要素を入力
    for i in range(N):
        a[i] = int(input("Input element in a: "))
    for i in range(N):
        b[i] = int(input("Input element in b: "))
    
    # 暫定最小値を格納する変数
    min_value = INF
    
    # bをソート: O(N log N)
    b.sort()
    
    # aを固定して解く: N通りをそれぞれO(log N)で解く
    for i in range(N):
        # bの中でK-a[i]以上の範囲での最小値を示す
        # 戻り値はインデックス
        index = bisect.bisect_left(b, K - a[i])
        
        # インデックスが示す値
        val = b[index]
        
        # min_valueと比較する
        if (a[i] + val) < min_value:
            min_value = (a[i] + val)
    
    print(min_value) # 問題全体はO(N log N)で解かれる

if __name__ == "__main__":
    main()

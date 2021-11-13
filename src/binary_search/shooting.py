# 射撃王
# N個の風船が初期状態でHiの高さにあり、1秒ごとにSiだけ上昇する
# すべての風船を射撃で割る
# 開始時に1個割り、そこから1秒ごとに1個の風船を割ることができる
# 風船を割る順番は自由に選べる
# 割ったときの風船の高度がペナルティになる
# 最終的なペナルティは、各風船を割ったときのペナルティの最大値とする
# 最終的なペナルティの最小値を求める
#
# N個の風船すべてについてペナルティをx以下にできるかを判定する
# 各風船を何秒以内に割るべきかを決めて、時間制限が差し迫っているものから割る
# すべての風船が割れたらYes, 途中で高さがxを超える風船が現れたらNo
# 全体計算量: O(N log N log M)

INF = 200000

def main():
    N = int(input("Input number of baloons: "))
    
    h, s = [0]*N, [0]*N
    
    for i in range(N):
        h[i] = int(input("Input height of baloon[{}]: ".format(i)))
        s[i] = h[i]
    
    # 高さ方向の二分探索
    # 反復回数 M = max(H_0+NS_0, ..., H_N-1+NS_N-1)
    bottom, top = 0, INF
    while (top - bottom) > 1:
        mid = (bottom + top) / 2
        
        # 判定
        ok = True
        t = [0] * N # 各風船を割るまでの時間制限
        
        for i in range(N):
            # midから今の高さまでの差分を計算
            # 既に初期高さよりmidが低かったらfalse
            if mid < h[i]: ok = False
            else: t[i] = (mid - h[i]) / s[i] # 時間制限を計算
        
        # 時間制限が迫っている順にソート
        t.sort() # O(N log N)
        
        for i in range(N):
            if t[i] < i: ok = False # 時間切れ
        
        if ok: top = mid
        else: bottom = mid
    
    print(top)

if __name__ == "__main__":
    main()
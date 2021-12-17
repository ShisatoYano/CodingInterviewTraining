# 挿入ソート
# 左からi枚がソートされている状態から
# i+1枚がソートされている状態にするという考え方
# 左からi枚分が整列済みの状態であることを仮定して、
# i+1枚目のカードを適切な場所に挿入する
# in-placeなソート(配列内部のswap処理で実現できる)
# 安定ソート

# ソートする配列
a = [4, 1, 3, 5, 2]

# 挿入ソート
def insertion_sort(a):
    N = len(a)
    
    for i in range(1, N):
        v = a[i] # 挿入したい値
        
        # vを挿入する適切な場所jを探す
        # 最悪でO(N^2)の計算量
        for j in range(i, -1, -1):
            if a[j-1] > v:
                a[j] = a[j-1]
            else:
                break
        a[j] = v
    
    print(a)

if __name__ == "__main__":
    insertion_sort(a)
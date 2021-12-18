# ヒープソート
# 最悪時でも計算量はO(N log N)になる
# 平均的な速度ではクイックソートに劣る
# ダイクストラ法を高速化するときにも活躍する
# 1: 与えられた配列の要素を全てヒープに挿入する(O(log N)の操作をN回実施)
# 2: ヒープの最大値を順にpopして配列の後ろから詰めていく(O(log N)の操作をN回実施)
# ソートしたい配列自体をヒープにして、in-placeなアルゴリズムを実現する
# ヒープ構築に要する計算量がO(N)に改善される

# ソートする配列
a = [10, 12, 15, 3, 8, 17, 4, 1]

# i番目の頂点を根とする部分木について、ヒープ条件を満たすようにする
# aのうち0番目からN-1番目までの部分a[0:N]についてのみ考える
def heapify(a, i, N):
    child_1 = i * 2 + 1 # 左の子供
    if child_1 >= N: return # 子供がないときは終了
    
    # 子供同士を比較
    if (child_1 + 1 < N) and (a[child_1+1] > a[child_1]):
        child_1 += 1
    
    if a[child_1] <= a[i]: return # 逆転がなかったら終了
    
    # swap
    a[i], a[child_1] = a[child_1], a[i]
    
    # 再帰的に
    heapify(a, child_1, N)

# ヒープソート
def heap_sort(a):
    N = len(a)
    
    # ステップ1: 配列全体をヒープにするフェーズ
    for i in range(int(N/2-1), -1, -1):
        heapify(a, i, N)
    
    # ステップ2: ヒープから1個1個最大値をpopするフェーズ
    for i in range(N-1, -1, -1):
        a[0], a[i] = a[i], a[0] # ヒープの最大値を左詰め
        heapify(a, 0, i) # ヒープサイズはiに

if __name__ == "__main__":
    heap_sort(a)
    
    print(a)
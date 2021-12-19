# バケットソート
# ソートしたい配列の各要素値は0以上A未満の整数値である
# という仮定の下ではO(N+A)の計算量を達成できる
# num[x]<-配列a中に値xをもつ要素が何個存在するか

# ソートする配列
a = [10, 12, 15, 3, 8, 17, 4, 1]

# 配列の値は1000未満とする
MAX = 1000

def bucket_sort(a):
    N = len(a)
    
    # 各要素の個数をカウントする
    # num[v]: vの個数
    num = [0] * MAX
    for i in range(0, N):
        num[a[i]] += 1 # a[i]をカウントする
    
    # numの累積和をとる
    # sum[v]: v以下の値の個数
    # 値a[i]が全体の中で何番目に小さいかを求める
    sum = [0] * MAX
    for v in range(1, MAX):
        sum[v] = sum[v-1] + num[v]
    
    # sumをもとにソート処理
    # a2: aをソートしたもの
    a2 = [0] * N
    for i in range(N-1, -1, -1):
        sum[a[i]] -= 1
        a2[sum[a[i]]] = a[i]
    
    print(a2)

if __name__ == "__main__":
    bucket_sort(a)
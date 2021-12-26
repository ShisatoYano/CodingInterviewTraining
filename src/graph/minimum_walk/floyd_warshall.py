# フロイド・ワーシャル法
# グラフ上の全頂点対間について最短路長を求める
# 全点対間最短路問題
# 計算量 O(|V|^3)
# dp[k][i][j]<-頂点0,1,...,k-1のみを中継頂点として
# 通ってよいとした場合の、頂点iから頂点jへの最短路長
# 初期条件1: 0(i=j)
# 初期条件2: l(e)(辺e=(i,j)が存在する)
# 初期条件3: ∞(それ以外)
# dp[k][i][j]の値を用いてdp[k+1][i][j]の値を更新する
# 更新方法1: 新たに使用できる頂点kを使用しない場合=dp[k][i][j]
# 更新方法2: 新たに使用できる頂点kを使用する場合=dp[k][i][k]+dp[k][k][j]
# この2通りのうち、値が小さい方を採用する

# 無限大を表す値
INF = 2 ** 60

# グラフの頂点数
N = 6

# 動的計画法のための配列
dp = [[0, 3, 5, INF, INF, INF],       # 頂点0から始まる辺と重み
      [INF, 0, 4, 12, INF, INF],      # 頂点1から始まる辺と重み
      [INF, INF, 0, 9, 4, INF],       # 頂点2から始まる辺と重み
      [INF, INF, INF, 0, INF, 2],     # 頂点3から始まる辺と重み
      [INF, INF, INF, 7, 0, 8],       # 頂点4から始まる辺と重み
      [INF, INF, INF, INF, INF, 0]]   # 頂点5から始まる辺と重み

def main():
    # dp遷移 フロイド・ワーシャル法
    for k in range(N):
        for i in range(N):
            for j in range(N):
                if dp[i][j] > (dp[i][k] + dp[k][j]):
                    dp[i][j] = (dp[i][k] + dp[k][j])
    
    # 結果出力
    # もしdp[v][v] < 0なら負閉路が存在する
    exist_negative_cycle = False
    for v in range(N):
        if dp[v][v] < 0: exist_negative_cycle = True
    
    if exist_negative_cycle: print("NEGATIVE CYCLE")
    else:
        for i in range(N):
            for j in range(N):
                if dp[i][j] < INF/2: print(i, j, dp[i][j])
                else: print(i, j, INF)

if __name__ == "__main__":
    main()
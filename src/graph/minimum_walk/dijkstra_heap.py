# ダイクストラ法
# 疎グラフの場合はヒープを用いて高速化する
# O(|E|log|V|)の計算量
# 使用済みでない頂点vのうち、d[v]の値が
# 最小の頂点を求める部分を高速化する

import heapq

# 無限大を表す値
INF = 2 ** 60

# 辺を表すクラス
class Edge:
    def __init__(self, to, w):
        self.to = to # 隣接頂点番号
        self.w = w # 重み

# 探索するグラフ
graph = [[Edge(1,3), Edge(2,5)],  # 頂点0
         [Edge(2,4), Edge(3,12)], # 頂点1
         [Edge(3,9), Edge(4,4)],  # 頂点2
         [Edge(5,2)],             # 頂点3
         [Edge(3,7), Edge(5,8)],  # 頂点4
         []]                      # 頂点5

N = len(graph) # 頂点の数

def main():
    s = 0 # 始点
    
    # ダイクストラ法
    dist = [INF] * N # 始点から各頂点への最短路長
    dist[s] = 0
    
    # (dist[v], v)のペアを要素としたヒープを作る
    pq = [(dist[s], s)]
    
    # ダイクストラ法の反復を開始
    while len(pq) > 0:
        # v: 使用済みでない頂点のうちdist[v]が最小の頂点
        # d: vに対するキー値
        d, v = heapq.heappop(pq)
        
        # d > dist[v]は、(d, v)がゴミであることを意味する
        if d > dist[v]: continue
        
        # 頂点vを始点とした各辺を緩和
        for e in graph[v]:
            if dist[e.to] > (dist[v] + e.w):
                dist[e.to] = (dist[v] + e.w)
                # 更新があればヒープに新たに挿入
                heapq.heappush(pq, (dist[e.to], e.to))
    
    # 結果出力
    for v in range(N):
        if dist[v] < INF: print(v, dist[v])
        else: print("INF")

if __name__ == "__main__":
    main()
# ダイクストラ法
# 既に最短路が求められていることが確定している頂点の集合Sを管理する
# 実現するためのデータ構造によって計算量が変わる
# 単純に実装した場合の、計算量O(|V|^2)の方法
# 蜜グラフにおいて有利

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
    used = [False] * N # 使用済み頂点
    dist = [INF] * N # 始点から各頂点への最短路長
    dist[s] = 0
    
    for i in range(N):
        # 使用済みでない頂点のうち、dist値が最小の頂点を探す
        min_dist = INF
        min_v = -1
        
        for v in range(N):
            if not used[v] and (dist[v] < min_dist):
                min_dist = dist[v]
                min_v = v
        
        # もしそのような頂点が見つからなければ終了
        if min_v == -1: break
        
        # min_vを始点とした各辺を緩和する
        for e in graph[min_v]:
            if dist[e.to] > (dist[min_v] + e.w):
                dist[e.to] = (dist[min_v] + e.w)
        used[min_v] = True # min_vを使用済みとする
    
    # 結果出力
    for v in range(N):
        if dist[v] < INF: print(v, dist[v])
        else: print("INF")

if __name__ == "__main__":
    main()
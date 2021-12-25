# ベルマンフォード法
# 始点sから到達できる負閉路が存在するならばそれを報告
# 負閉路が存在しないなら各頂点vへの最短路を求める
# 各辺に対して一通り緩和するという操作を、
# 最短路長推定値d[v]が更新されなくなるまで反復する
# 各辺に対する緩和にO(|E|)の計算量を要し、
# それをO(|V|)回の反復を行うため、
# 計算量はO(|V||E|)となる

# 無限大を表す値
INF = 2 ** 60

# 辺を表すクラス
class Edge:
    def __init__(self, to, w):
        self.to = to # 隣接頂点番号
        self.w = w # 重み

# 探索するグラフ
graph = [[Edge(1,3), Edge(3,100)],               # 頂点0
         [Edge(2,50), Edge(3,57), Edge(4,-4)],   # 頂点1
         [Edge(3,-10), Edge(4,-5), Edge(5,100)], # 頂点2
         [Edge(1,-5)],                           # 頂点3
         [Edge(2,57), Edge(3,25), Edge(5,8)],    # 頂点4
         []]                                     # 頂点5

N = len(graph) # 頂点の数

def main():
    s = 0 # 始点とする頂点の番号
    
    # 負閉路を持つかどうか
    exist_nagative_cycle = False
    
    # 始点から各頂点へ進むときの最短路長を記録する配列
    dist = [INF] * N
    dist[s] = 0
    
    for i in range(N):
        update = False # 更新されたかどうか
        
        for v in range(N):
            # dist[v] = INFのときは頂点vからの緩和を行わない
            if dist[v] == INF: continue
            
            for e in graph[v]:
                # 緩和処理を行い、更新されたらupdateをtrueにする
                if dist[e.to] > (dist[v] + e.w):
                    dist[e.to] = (dist[v] + e.w)
                    update = True
                else: update = False
        
        # 更新がなかったら、既に最短路が求められている
        if not update == False: break
        
        # N回目の反復で更新があったなら、負閉路を持つ
        if i == N-1 and update:
            exist_nagative_cycle = True
    
    # 結果出力
    if exist_nagative_cycle: print("Negative cycle")
    else:
        for v in range(N):
            if dist[v] < INF: print(v, dist[v])
            else: print("INF")

if __name__ == "__main__":
    main()
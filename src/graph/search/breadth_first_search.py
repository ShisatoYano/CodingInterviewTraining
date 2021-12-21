# 最短路アルゴリズムとしての幅優先探索
# 探索の始点となる頂点sから、各頂点への最短路を求めるアルゴリズム
# 配列distには、頂点sから各頂点までの最短路長が格納される
# 頂点vから未訪問の頂点xへの探索: dist[x]の値はdist[v]+1となる
# 配列distは、初期状態では配列全体を-1に初期化しておく
# dist[v]==-1とseen[v]==falseは同じ意味を持つ
# 頂点数Vと辺数E=>計算量はO(V+E)

import queue

# 入力: グラフgraphと探索の始点s
# 出力: sから各頂点への最短路長を表す配列
def bfs(graph, s):
    N = len(graph) # 頂点数
    
    dist = [-1] * N # 全頂点を未訪問に初期化
    
    que = queue.Queue()
    
    # 初期条件(頂点0を初期頂点とする)
    dist[0] = 0
    que.put(0) # 0を橙色頂点にする
    
    # BFS開始(キューが空になるまで探索する)
    while not que.empty():
        v = que.get() # キューから先頭頂点を取り出す
        
        # vから辿れる頂点を全て調べる
        for x in graph[v]:
            # 既に発見済みの頂点は探索しない
            if dist[x] != -1: continue
            
            # 新たな白色頂点xについて距離情報を更新してキューに挿入
            dist[x] = dist[v] + 1
            que.put(x)
    
    return dist

if __name__ == "__main__":
    # 探索するグラフ
    # 無向グラフ
    graph = [[1,2,4], [0,3,4,8], [0,5], [1,7,8], 
             [0,1,8], [2,6,8], [5,7], [3,6], [1,3,4,5]]
    
    # 頂点0を始点としたBFS
    dist = bfs(graph, 0)
    
    # 結果出力(各頂点の頂点0からの距離を見る)
    for v in range(0, len(graph)):
        print(v, ": ", dist[v])
    
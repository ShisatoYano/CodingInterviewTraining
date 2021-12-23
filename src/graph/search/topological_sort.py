# トポロジカルソート
# 与えられた有向グラフに対し、
# 各頂点を辺の向きに沿うように順序付けて並び替えること
# 応用例: ビルドシステムに見られるような依存関係を解決する処理
# 与えられるグラフが有向サイクルをもたないことが必要かつ十分
# DAG(Directed Acyclic Graph)

# ソートする有向グラフ
graph = [[5], [3,6], [5,7], [0,7], [1,2,6], [], [7], [0]]

# グラフの頂点数
N = len(graph)

# 訪問したかを記録する配列
seen = [False] * N

# トポロジカルソート順になった頂点を入れる配列
order = []

# トポロジカルソートする関数
def rec(graph, v):
    seen[v] = True
    
    for next_v in graph[v]:
        # 既に訪問済みなら探索しない
        if seen[next_v]: continue
        rec(graph, next_v)
    
    # v-outを記録する
    order.append(v)

if __name__ == "__main__":
    # 探索
    for v in range(N):
        # 既に訪問済みなら探索しない
        if seen[v]: continue
        rec(graph, v)
    
    # 逆順に
    order.reverse()
    
    # 出力
    for v in order: print(v)
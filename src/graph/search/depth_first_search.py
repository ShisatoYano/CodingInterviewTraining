# 深さ優先探索(Depth First Search)
# 再帰関数を用いることでより簡潔に実装できる
# 頂点vから辿ることのできる頂点のうち、
# まだ訪問していない頂点をすべて訪問する

# 探索するグラフ
graph = [[5], [3,6], [5,7], [0,7], [1,2,6], [], [7], [0]]

# グラフの頂点数
N = len(graph)

# 訪問済みか未訪問か記憶する配列
seen = [False] * N

# 深さ優先探索
def dfs(graph, v):
    seen[v] = True # vを訪問済みとする
    print(v)
    
    # vから行ける各頂点next_vについて
    for next_v in graph[v]:
        if seen[next_v]: continue # next_vが探索済みなら探索しない
        dfs(graph, next_v)

if __name__ == "__main__":
    for v in range(0, N):
        if seen[v]: continue # 既に訪問済みなら探索しない
        
        dfs(graph, v)
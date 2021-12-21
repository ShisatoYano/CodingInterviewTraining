# s-tパスが存在するかを判定する問題
# 有向グラフとグラフ上の2頂点s, tが与えられる
# sから出発してtへたどり着けるか

# 探索するグラフ
graph = [[5], [3,6], [5,7], [0,7], [1,2,6], [], [7], [0]]

# グラフの頂点数
N = len(graph)

# 訪問済みか未訪問か記憶する配列
seen = [False] * N

# 深さ優先探索
def dfs(graph, v):
    seen[v] = True # vを訪問済みとする
    
    # vから行ける各頂点next_vについて
    for next_v in graph[v]:
        if seen[next_v]: continue # next_vが探索済みなら探索しない
        dfs(graph, next_v)

if __name__ == "__main__":
    # sからスタートしてtに向かう
    s, t = 6, 5
    
    # sからtにたどり着けるか探索   
    dfs(graph, s)
    
    # 結果
    if seen[t]: print("Yes")
    else: print("No")
# 与えられたグラフが二部グラフかを判定する問題
# 白色の頂点同士が隣接することはなく
# 黒色の頂点同士が隣接することもない
# という条件を満たすように、各頂点を白色または黒色に
# 塗分けることが可能なグラフ
# グラフを左右のカテゴリに分割して、
# 同じカテゴリ内の頂点間には辺がない状態にできること

# 探索する無向グラフ
graph = [[1,3], [0,2], [1], [0,4], [1,3]]

# グラフの頂点数
N = len(graph)

# 黒か白か
color = [-1] * N

# 深さ優先探索
def dfs(graph, v, cur=0):
    color[v] = cur
    
    for next_v in graph[v]:
        # 隣接頂点がすでに色確定していた場合
        if color[next_v] != -1:
            # 同じ色が隣接した場合は二部グラフではない
            if color[next_v] == cur: return False
            
            # 色が確定した場合には探索しない
            continue
        
        # 隣接頂点の色を変えて再帰的に探索
        # Falseが返ってきたらFalseを返す
        if dfs(graph, next_v, 1-cur) == False: return False
    
    return True

if __name__ == "__main__":
    # 探索
    is_bipartite = True
    
    for v in range(N):
        # vが探索済みの場合は無視
        if color[v] != -1: continue
        if dfs(graph, v) == False: is_bipartite = False
    
    if is_bipartite: print("Yes")
    else: print("No")
        
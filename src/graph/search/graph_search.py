# グラフ探索の基本形
# グラフ上の代表的な1つの頂点sを指定して、
# sから辺をたどって到達できる各頂点を探索する

import queue

def search(graph, s):
    N = len(graph) # グラフの頂点数
    
    # グラフ探索のためのデータ構造
    seen = [False] * N # 全頂点を未訪問に初期化する
    todo = queue.Queue() # First-In First-Out, 幅優先探索
    
    # 初期条件
    seen[s] = True # sは探索済みとする
    print(s)
    todo.put(s) # todoはsのみを含む状態となる
    
    # todoが空になるまで探索を行う
    while not todo.empty():
        # todoから頂点を取り出す
        v = todo.get()
        
        # vから辿れる頂点を全て調べる
        for x in graph[v]:
            # 既に発見済みの頂点は探索しない
            if seen[x]: continue
            
            # 新たな頂点xを探索済みとしてtodoに挿入
            seen[x] = True
            print(x)
            todo.put(x)

if __name__ == "__main__":
    # 探索するグラフ
    graph = [[5], [3,6], [5,7], [0,7], [1,2,6], [], [7], [0]]

    # 探索
    search(graph, 4)
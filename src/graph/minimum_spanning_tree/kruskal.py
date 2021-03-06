# クラスカル法
# 最小全域木問題を解く手法
# ネットワーク設計において、いくつかの通信拠点を
# 全て通信用ケーブルでつなぎ、全ての建物間で
# 通信できるようにしたい
# これを最小の長さのケーブルで実現することを考える
# 計算量
# 辺を重みが小さい順にソートする部分: O(|E|log|V|)
# 各辺を順に処理する部分: O(|E|α|V|)
# 全体でO(|E|log|V|)

# 探索する無向グラフ
GRAPH = [(5, (0, 3)), (6, (0, 5)), (3, (0, 7)),
         (8, (1, 3)), (4, (1, 4)), (3, (1, 6)),
         (9, (2, 4)), (10, (2, 5)), (5, (2, 7)),
         (5, (3, 0)), (8, (3, 1)), (6, (3, 7)),
         (4, (4, 1)), (9, (4, 2)), (2, (4, 6)),
         (6, (5, 0)), (10, (5, 2)),
         (3, (6, 1)), (2, (6, 4)), (7, (6, 7)),
         (3, (7, 0)), (5, (7, 2)), (6, (7, 3)), (7, (7, 6))]

# 辺の数
M = len(GRAPH)

# 頂点の数
N = 8

# Union-Findクラス
class UnionFind(object):
    # 初期化
    def __init__(self, n):
        self.par = [-1] * n # 各頂点の親頂点の番号、自身が根の場合は-1
        self.siz = [1] * n # 各頂点の属する根付き木の頂点数
    
    # 要素xを含むグループの根を返す
    # 頂点xから親を辿っていき、根に到達したらそれを返す
    # xから上へと進んでいって根に到達するまでの経路中の頂点に対し
    # その親を根に張り替える
    def root(self, x):
        if self.par[x] == -1: return x # xが根の場合はxを返す
        else:
            # 経路圧縮
            self.par[x] = self.root(self.par[x])
            return self.par[x]
    
    # x, yが同じグループに属するかどうか
    # 根が一致するかどうか
    def is_same(self, x, y):
        return (self.root(x) == self.root(y))
    
    # xを含むグループとyを含むグループとを併合する
    # 頂点xを含む根付き木の根と、頂点yを含む根付き木の根を求める
    # 一方の根である頂点が、もう一方の根である頂点の子となるようにつなぐ
    def unite(self, x, y):
        # x, yをそれぞれ根まで移動する
        x, y = self.root(x), self.root(y)
        
        # 既に同じグループのときは何もしない
        if x == y: return False
        
        # union by size(y側のサイズが小さくなるようにする)
        if self.siz[x] < self.siz[y]: x, y = y, x
        
        # yをxの子とする
        self.par[y] = x
        self.siz[x] += self.siz[y]
        return True
    
    # xを含むグループのサイズ
    def size(self, x):
        return self.siz[self.root(x)]

def main():
    # グラフの各辺を重みが小さい順にソートする
    GRAPH.sort()
    
    # クラスカル法
    res = 0
    uf = UnionFind(N)
    for i in range(M):
        edge = GRAPH[i]
        
        w = edge[0]
        u = edge[1][0]
        v = edge[1][1]
        
        # 辺(u, v)の追加によってサイクルが形成されるときは追加しない
        if uf.is_same(u, v): continue
        
        # 辺(u, v)を追加する
        res += w
        uf.unite(u, v)
    
    print(res)

if __name__ == "__main__":
    main()
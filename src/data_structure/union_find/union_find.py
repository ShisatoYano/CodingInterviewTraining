# Union-Find
# グループ分けを効率的に管理するデータ構造
# クエリ1: issame(x, y) 要素x, yが同じグループに属するか調べる
# クエリ2: unite(x, y) 要素xを含むグループと、要素yを含むグループとを併合する
# 1つ1つのグループが根付き木を構成するようにして実現できる
# 二分木である必要はない

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

if __name__ == "__main__":
    uf = UnionFind(7)
    
    uf.unite(1, 2)
    uf.unite(2, 3)
    uf.unite(5, 6)
    
    print(uf.is_same(1, 3))
    print(uf.is_same(2, 5))
    
    uf.unite(1, 6)
    print(uf.is_same(2, 5))
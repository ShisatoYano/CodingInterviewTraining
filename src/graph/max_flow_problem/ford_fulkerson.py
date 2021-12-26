# フォード・ファルカーソン法
# 最大流問題を解くための手法
# 供給地である地点sから需要地点tへと
# ものをできるだけ沢山運ぶ方法を考える問題
# 各辺eには運べる量の上限を表す容量c(e)が設けられる
# uからvへの方向にはさらにc(e)-x(e)の流量を流せる
# vからuへの方向に、いくらかフローを流して押し戻せる
# 最大でx(e)の流量を押し戻せる

# 辺を表すクラス
# rev: 逆辺(to, frm)がG[to]の中で何番目の要素か
# cap: 辺(frm, to)の容量
class Edge:
    def __init__(self, r, f, t, c):
        self.rev = r
        self.frm = f
        self.to = t
        self.cap = c

# グラフを表すクラス
class Graph:
    # N: 頂点数
    def __init__(self, N):
        self.list = [[]] * N
    
    # グラフの頂点数を取得
    def size(self):
        return len(self.list)
    
    # 辺e = (u, v)の逆辺(v, u)を取得する
    def redge(self, e):
        return self.list[e.to][e.rev]
    
    # 辺e = (u, v)に流量fのフローを流す
    # e = (u, v)の流量がfだけ減少する
    # このとき逆辺(v, u)の流量を増やす
    def run_flow(self, e, f):
        e.cap -= f
        self.redge(e).cap += f
    
    # 頂点fromから頂点toへ容量capの辺を張る
    # このときtoからfromへも容量0の辺を張っておく
    def add_edge(self, frm, to, cap):
        from_rev = len(self.list[frm])
        to_rev = len(self.list[to])
        self.list[frm].append(Edge(to_rev, frm, to, cap))
        self.list[to].append(Edge(from_rev, to, frm, 0))

# フォード・ファルカーソン法を実行するクラス
INF = 2 ** 50
class FordFulkerson:
    # 初期化
    def __init__(self):
        self.seen = []
    
    # 残余グラフ上でs-tパスを見つける(深さ優先探索)
    # 返り値はs-tパス上の容量の最小値(見つからなければ0)
    # f: sからvへ到達した過程の各辺の容量の最小値
    def fo_dfs(self, G, v, t, f):
        # 終端tに到達したらリターン
        if v == t: return f
        
        # 深さ優先探索
        self.seen[v] = True
        for e in G.list[v]:
            if self.seen[e.to]: continue
            
            # 容量0の辺は実際には存在しない
            if e.cap == 0: continue
            
            # s-tパスを探す
            # 見つかったらflowはパス上の最小容量
            # 見つからなかったらf = 0
            flow = self.fo_dfs(G, e.to, t, min(f, e.cap))
            
            # s-tパスが見つからなかったら次辺を試す
            if flow == 0: continue
            
            # 辺eに容量flowのフローを流す
            G.run_flow(e, flow)
            
            # s-tパスを見つけたらパス上最小容量を返す
            return flow

        # s-tパスが見つからなかったことを示す
        return 0
    
    # グラフGのs-t間の最大流量を求める
    # ただしリターン時にGは残余グラフになる
    def solve(self, G, s, t):
        res = 0
        
        # 残余グラフにs-tパスがなくなるまで反復
        while True:
            self.seen = [0] * G.size()
            
            flow = self.fo_dfs(G, s, t, INF)
            
            # s-tパスが見つからなかったら終了
            if flow == 0: return res
            
            # 答えを加算
            res += flow
        
        # no reach
        return 0

# メインプロセス
if __name__ == "__main__":
    # グラフの定義
    N = 6
    G = Graph(N)
    
    # 容量cの辺(u, v)を張る
    G.add_edge(0, 1, 5), G.add_edge(0, 3, 5)
    G.add_edge(1, 2, 4), G.add_edge(1, 3, 37)
    G.add_edge(2, 4, 56), G.add_edge(2, 5, 9)
    G.add_edge(3, 2, 3), G.add_edge(3, 4, 9)
    G.add_edge(4, 5, 2)
    
    # フォード・ファルカーソン法
    ff = FordFulkerson()
    s, t = 0, N-1
    print(ff.solve(G, s, t))
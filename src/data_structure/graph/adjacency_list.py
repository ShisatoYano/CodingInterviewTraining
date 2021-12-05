# グラフの隣接リスト表現
# グラフにある頂点または辺を全てリストで表現したもの
# 各頂点とその隣接する頂点群の配列をハッシュテーブルで関連づける方法
# 無向グラフに対しても有向グラフに対しても同様に実施することができる

# 頂点
class Vertex(object):
    # 初期化
    def __init__(self, id):
        self.id = id
        self.adjacent = {}
    
    # 隣接ノードと重みの追加
    def add_neighbor(self, neighbor, weight=0):
        self.adjacent[neighbor] = weight
    
    # 隣接ノード群のハッシュテーブルの取得
    def get_neighbors(self):
        return self.adjacent
    
    # 隣接ノード群の取得
    def get_connections(self):
        return self.adjacent.keys()
    
    # ノードIDの取得
    def get_vertex_id(self):
        return self.id
    
    # ノードの重みの取得
    def get_weight(self, neighbor):
        return self.adjacent[neighbor]
    
# グラフ
class Graph(object):
    # 初期化
    def __init__(self):
        self.vertex_dict = {}
        self.vertex_num = 0
    
    # ノードの追加
    def add_vertex(self, id):
        self.vertex_num += 1
        new_vertex = Vertex(id)
        self.vertex_dict[id] = new_vertex
        return new_vertex
    
    # ノードの取得
    def get_vertex(self, id):
        if id in self.vertex_dict:
            return self.vertex_dict[id]
        else:
            return None
    
    # エッジの追加
    def add_edge(self, frm, to, weight=0):
        if frm not in self.vertex_dict:
            self.add_vertex(frm)
        if to not in self.vertex_dict:
            self.add_vertex(to)
        # エッジでつながるもう一方のノードを追加
        self.vertex_dict[frm].add_neighbor(self.vertex_dict[to], weight)
        self.vertex_dict[to].add_neighbor(self.vertex_dict[frm], weight)
    
    # ノード集合の取得
    def get_vertices(self):
        return self.vertex_dict.keys()
    
    # エッジ集合の取得
    def get_edges(self):
        edges = []
        
        for v in self.vertex_dict.values(): # 各ノード
            for w in v.get_connections(): # 隣接ノード
                v_id = v.get_vertex_id()
                w_id = w.get_vertex_id()
                edges.append((v_id, w_id, v.get_weight(w)))
        
        return edges

# メイン
if __name__ == "__main__":
    graph = Graph()
    
    graph.add_vertex('a')
    graph.add_vertex('b')
    graph.add_vertex('c')
    graph.add_vertex('d')
    graph.add_vertex('e')
    
    print("Add Nodes:", graph.get_vertices())
    
    graph.add_edge('a', 'e', 10)
    graph.add_edge('a', 'c', 20)
    graph.add_edge('c', 'b', 30)
    graph.add_edge('b', 'e', 40)
    graph.add_edge('e', 'd', 50)
    
    print("Add Edges:", graph.get_edges())
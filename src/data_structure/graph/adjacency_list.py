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
    
    # 隣接ノード群の取得
    def get_neighbors(self):
        return self.adjacent
    
    # 接続先ノード群の取得
    def get_connection(self):
        return self.adjacent.keys()
    
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
    
    # ノード集合の取得
    def get_vertices(self):
        return self.vertex_dict.keys()
    
    # エッジ集合の取得
    def get_edges(self):
        edges = []
        

# メイン
if __name__ == "__main__":
    graph = Graph()
    
    graph.add_vertex('a')
    graph.add_vertex('b')
    graph.add_vertex('c')
    graph.add_vertex('d')
    graph.add_vertex('e')
    
    print("Nodes: ", graph.get_vertices())
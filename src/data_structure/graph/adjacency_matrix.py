# グラフの隣接リスト表現
# 有限グラフを表すために使われる正方行列
# 各ノード間の隣接と重みを以下のように表現する
#  0  0 20  0 10
#  0  0 30  0 40
# 20 30  0  0  0
#  0  0  0  0 50
# 10 40  0 50  0

# ノード
class Vertex(object):
    # 初期化
    def __init__(self, id):
        self.id = id
    
    # ノードIDの取得
    def get_id(self):
        return self.id
    
    # ノードIDのセット
    def set_id(self, id):
        self.id = id

# グラフ
class Graph(object):
    # 初期化
    def __init__(self, vertex_num):
        self.adj_matrix = [[0] * vertex_num for _ in range(vertex_num)] # num x numの正方行列
        self.vertex_num = vertex_num
        self.vertices = []
        for i in range(0, vertex_num):
            new_vertex = Vertex(i)
            self.vertices.append(new_vertex)
    
    # 隣接行列の表示
    def print_matrix(self):
        print("Adjacent matrix")
        for u in range(0, self.vertex_num):
            row = []
            for v in range(0, self.vertex_num):
                row.append(self.adj_matrix[u][v])
            print(row)
    
    # 全ノードのインデックスを取得
    def get_vertices(self):
        vertices = []
        for idx in range(0, self.vertex_num):
            vertices.append(self.vertices[idx].get_id())
        return vertices
    
    # 全エッジ情報の取得
    def get_edges(self):
        edges = []
        for v in range(0, self.vertex_num):
            for u in range(0, self.vertex_num):
                if self.adj_matrix[u][v] != 0:
                    v_id = self.vertices[v].get_id()
                    u_id = self.vertices[u].get_id()
                    edges.append((v_id, u_id, self.adj_matrix[u][v])) # エッジ両端のノードIDと重み
        return edges

# メイン
if __name__ == "__main__":
    graph = Graph(5)
    
    graph.print_matrix()
    print("Node index:", graph.get_vertices())
    print("Edges:", graph.get_edges())
    print("----------------------------------")
# 二分探索木
# 任意の頂点vに対し、vの左部分木に含まれる
# 全ての頂点v'に対してkey[v]>=key[v']が成立し、
# vの右部分木に含まれる全ての頂点v'に対して
# key[v]<=key[v']が成立する
# 左の子孫の値<=親の値<=右の子孫の値
# 各クエリに対してO(N)の計算量を要する
# 平衡二分探索木でO(log N)に改善できる

# ノードクラス
class Node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None

# 二分探索木クラス
class BST:
    # 初期化
    def __init__(self):
        self.root = None
    
    # 挿入
    # ルートから順に着目しているノードと目的の値を比較する
    # 目的の値 < 着目しているノードなら左の子
    # 着目しているノード <= 目的の値なら右の子
    # が次の着目ノードになる
    # 次のノードが存在しなければ、その位置に挿入
    # 存在すれば次の着目ノードに移って繰り返し
    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert(data, self.root)
    
    # ルートより下の挿入
    def _insert(self, data, cur_node):
        if data < cur_node.data:
            if cur_node.left is None:
                cur_node.left = Node(data)
            else:
                self._insert(data, cur_node.left)
        elif data > cur_node.data:
            if cur_node.right is None:
                cur_node.right = Node(data)
            else:
                self._insert(data, cur_node.right)
        else:
            print("Found same value")
    
    # 列挙
    # 再帰呼び出しにより登録データを全てソートされた順に列挙
    # 左の子をルートとする部分木に対して再帰的に適用
    # 親を表示する
    # 右の子をルートとする部分木に対して再帰的に適用
    def inorder_print_tree(self):
        if self.root:
            self._inorder_print_tree(self.root)
    
    # 再帰呼び出し用
    def _inorder_print_tree(self, cur_node):
        if cur_node:
            self._inorder_print_tree(cur_node.left)
            print(str(cur_node.data))
            self._inorder_print_tree(cur_node.right)
    
    # 探索
    # ルートから順に、着目するノードと目的の値を比較
    # 等しいか、着目ノードが存在しなければ終了
    # 目的の値 < 着目しているノードなら左の子
    # 着目しているノード < 目的の値なら右の子
    # へ移って繰り返し
    def find_by_rec(self, data):
        if self.root:
            is_found = self._find(data, self.root)
            if is_found:
                return True
            return False
        else:
            return None
    
    # 再帰呼び出し用
    def _find(self, data, cur_node):
        if data > cur_node.data and cur_node.right:
            return self._find(data, cur_node.right)
        elif data < cur_node.data and cur_node.left:
            return self._find(data, cur_node.left)
        if data == cur_node.data:
            return True
    
    # ループによる探索
    def find_by_roop(self, data):
        if self.root is None:
            return None
        cur_node = self.root
        while cur_node:
            if data == cur_node.data:
                return True
            if data < cur_node.data:
                cur_node = cur_node.left
            else:
                cur_node = cur_node.right
        return False
        
if __name__ == "__main__":
    bst = BST()
    
    bst.insert(8)
    bst.insert(3)
    bst.insert(10)
    bst.insert(1)
    bst.insert(6)
    bst.insert(14)
    bst.insert(4)
    bst.insert(7)
    bst.insert(13)
    
    bst.inorder_print_tree()
    
    print("Find 6 by rec:", bst.find_by_rec(6))
    print("Find 6 by roop:", bst.find_by_roop(6))
    print("Find 12 by rec:", bst.find_by_rec(12))
    print("Find 12 by roop:", bst.find_by_roop(12))
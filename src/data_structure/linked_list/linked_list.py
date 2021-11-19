# 連結リスト
# 配列の弱点である挿入・削除クエリに強いデータ構造
# 挿入・削除操作をO(1)で実行できる
# 各要素をポインタと呼ばれる矢印によって1列に繋いだもの
# 各要素が全体の何番目かという情報を管理しなくてよい

# ノードクラス
class Node:
    def __init__(self, name):
        self.next = None # 次がどのノードを指すか
        self.name = name # ノードに付随している値

# 連結リストクラス
class LinkedList:
    # 初期化
    def __init__(self):
        self.nil = Node(None) # 番兵
        self.nil.next = self.nil
    
    # 連結リストを出力する
    def print_list(self):
        cur = self.nil.next # 先頭から出発
        while cur != self.nil:
            print("{} -> ".format(cur.name), end=' ')
            cur = cur.next
        print('')
    
    # ノードpの直後にノードvを挿入する
    # ノードpのデフォルト引数をnilとしておく
    # そのためinsert(v, nil)を呼び出す操作はリストの先頭への挿入を表す
    def insert(self, v: Node, p: Node):
        v.next = p.next
        p.next = v

def main():
    # 初期化
    l = LinkedList()
    
    # 作りたいノードの名前一覧
    # 最後尾のノードから順に挿入する
    names = ["yamamoto", "watanabe", "ito", "takahashi", "suzuki", "sato"]
    
    for i, name in enumerate(names):
        # ノードを作成する
        node = Node(name)
        
        # 作成したノードを連結リストの先頭に挿入する
        l.insert(node, l.nil)
        
        # 各ステップの連結リストの様子を出力する
        print("step {}:".format(i), end=' ')
        l.print_list()

if __name__ == "__main__":
    main()
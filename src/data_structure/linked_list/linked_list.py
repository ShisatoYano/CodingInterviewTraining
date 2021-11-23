# 連結リスト
# 配列の弱点である挿入・削除クエリに強いデータ構造
# 挿入・削除操作をO(1)で実行できる
# 各要素をポインタと呼ばれる矢印によって1列に繋いだもの
# 各要素が全体の何番目かという情報を管理しなくてよい

# ノードクラス
# ノード削除時のポインタ繋ぎ変えをしやすくするために
# 双方向連結リスト(bidirectional linked list)を用いる
class Node:
    def __init__(self, name):
        self.next = None # 自分の前がどのノードを指すか
        self.prev = None # 自分の後ろがどのノードを指すか
        self.name = name # ノードに付随している値

# 連結リストクラス
class LinkedList:
    # 初期化
    def __init__(self):
        self.nil = Node(None) # 番兵
        self.nil.next = self.nil
        self.nil.prev = self.nil
    
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
        p.next.prev = v
        p.next = v
        v.prev = p
    
    # ノードvを削除する
    def erase(self, v: Node):
        if v == self.nil: return # vが番兵の場合は何もしない
        v.prev.next = v.next
        v.next.prev = v.prev
        del v

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
        
        # 「渡辺」ノードを保持しておく
        if name == "watanabe": watanabe = node
    
    # 「渡辺」ノードを削除する
    print("before:", end=' ')
    l.print_list() # 削除前を出力
    l.erase(watanabe)
    print("after:", end=' ')
    l.print_list() # 削除後を出力

if __name__ == "__main__":
    main()
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
        self.head = Node(None)
    
    # 挿入操作
    # ポインタの矢印を繋ぎ変えることで実現する
    def insert(self, name):
        front = self.head
        rear = front.next

def main():
    l = LinkedList()

if __name__ == "__main__":
    main()
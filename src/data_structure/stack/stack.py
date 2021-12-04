# スタック
# ものが積みあがった状態に例えられる
# 最後に追加された要素を取り出す
# LIFO(last-in first-out)
# Webブラウザの訪問履歴やテキストエディタにおけるUndo系列

MAX = 100000 # スタック配列の最大サイズ

class Stack(object):
    def __init__(self):
        self.st = [0] * MAX # スタック配列
        self.top = 0 # スタックの先頭を表す添え字

    # スタックが空かどうか判定する
    def is_empty(self):
        return (self.top == 0)

    # スタックが満杯かどうか判定する
    def is_full(self):
        return (self.top == MAX)

    # 挿入
    def push(self, x):
        if self.is_full():
            print("error: stack is full.")
            return
        # xを格納してtopを進める
        self.st[self.top] = x
        self.top += 1

    # 取り出し
    def pop(self):
        if self.is_empty():
            print("error: stack is empty.")
            return -1
        # topをデクリメントしてtopの位置にある要素を返す
        self.top -= 1
        return self.st[self.top]

if __name__ == "__main__":
    stack = Stack()
    
    stack.push(3)
    stack.push(5)
    stack.push(7)
    
    print(stack.pop())
    print(stack.pop())
    
    stack.push(9)
    
    print(stack.st[:stack.top])
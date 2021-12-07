# ヒープ
# 各頂点vがキーと呼ばれる値key[v]をもつ二分木
# ヒープの条件
# 頂点vの親頂点をpとしたとき、key[p] >= key[v]が成立する
# 木の高さをhとしたとき、木の深さh-1以下の部分については、完全二分木を形成する
# 木の高さをhとしたとき、木の深さhの部分については、頂点が左詰めされている
# 強平衡二分木となるため、様々なクエリをO(log N)の計算量で処理できる
#
# 値xを挿入する、最大値を取得する、最大値を削除する
# 処理後もヒープの条件を満たすようにする

# ヒープ
class Heap(object):
    # 初期化
    def __init__(self):
        self.array = []
    
    # ヒープに値xを挿入
    def push(self, x):
        self.array.append(x) # 最後尾に挿入
        i = len(self.array) - 1 # 挿入された頂点番号
        while i > 0:
            p = int((i - 1) / 2) # 親の頂点番号
            if self.array[p] >= x: break # 逆転が無ければ終了
            self.array[i] = self.array[p] # 自分の値を親にする
            i = p # 自分と親を入れ替える
        self.array[i] = x # xは最終的にこの位置に持ってくる
    
    # 最大値を知る
    def top(self):
        if len(self.array) > 0: return self.array[0]
        else: return -1
    
    # 最大値を削除
    def pop(self):
        if len(self.array) == 0: return
        # 最後尾の値を頂点に持ってくる
        x = self.array.pop(-1) # 最後尾の値は削除
        i = 0 # rootから下へ降ろしていく
        while (i * 2 + 1) < len(self.array):
            child_1 = int(i * 2 + 1)
            child_2 = int(i * 2 + 2)
            # 子ノード同士を比較して大きい方を子1にする
            if (child_2 < len(self.array)) and \
               (self.array[child_2] > self.array[child_1]):
                   child_1 = child_2
            if self.array[child_1] <= x: break # 逆転がなければ終了
            self.array[i] = self.array[child_1] # 自分の値を子ノードの値にする
            i = child_1
        self.array[i] = x # 最終的にxはこの位置に持ってくる

if __name__ == "__main__":
    h = Heap()
    
    h.push(5)
    h.push(3)
    h.push(7)
    h.push(1)
    
    print("Current top is", h.top())
    
    h.pop()
    print("Removed top and current top is", h.top())
    
    h.push(11)
    print("Pushed 11 and current top is", h.top())
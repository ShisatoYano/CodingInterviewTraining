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
# ハッシュテーブル
# Mを正の整数、xを0以上M未満の整数として3つのクエリを高速に処理することを考える
# xをデータ構造に挿入、xをデータ構造から削除、xがデータ構造に含まれるか判定
# いずれもO(1)の計算量で処理できる
# 整数とは限らない一般的なデータ集合Sの各要素xに対し、
# 0 <= h(x) < Mを満たす整数h(x)に対応させることを考える
# h(x):ハッシュ関数, x:キー, ハッシュ関数の値h(x):ハッシュ値

# キーをハッシュ値にする際、異なるキーでも同じハッシュ値を生成してしまう
# 衝突が発生することがある。それを回避する方法として、各ハッシュ値ごとに
# 連結リストを構築する方法がある。
# ハッシュ値が等しいもの同士で連結リストを構築する

# ハッシュテーブルの計算量
# 「任意のキーに対してハッシュ値が特定の値をとる確率が1/Mであり、
# 任意の2つのキーに対して、それらの類似性とは関係なくハッシュ値が衝突する
# 確率が1/Mである」という単純一様ハッシュの仮定を満たすとき、
# ハッシュテーブルの各要素にアクセスする計算量は平均的にO(1+N/M)となる
# α=N/Mを負荷率と呼ぶ。α=1/2程度とすれば十分O(1)の計算量が達成できるとされている

# 衝突を回避するための連結リスト
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

# ハッシュテーブルクラス
class HashTable:
    def __init__(self):
        self.table = [None] * 1000
    
    # 1000で割った余りをハッシュ値として扱う
    def hash(self, key):
        return key % 1000
    
    def add(self, key, value):
        hashed_key = self.hash(key)
        if self.table[hashed_key]: # 既にキーにデータが存在していたら
            ll = self.table[hashed_key] # 既に存在しているデータ(連結リストの先頭)
            while ll:
                # 連結リストの最後尾までループして最後にデータを追加する
                if not ll.next: # 連結リストの最後
                    ll.next = LinkedList(value) # 新しい値を連結
                    break
                else:
                    ll = ll.next
        else: # データが存在していない場合
            self.table[hashed_key] = LinkedList(value) # 新しい値を連結リストに連結
    
    def get(self, key):
        values = []
        hashed_key = self.hash(key)
        ll = self.table[hashed_key]
        if not ll: # 指定したキーにデータが存在しない場合
            return -1
        while ll: # 連結リストが存在する場合
            values.append(ll.value) # 連結リストの値をリストに追加
            if not ll.next: # リストの最後尾
                return values
            else:
                ll = ll.next
    
    def remove(self, key, value):
        hashed_key = self.hash(key)
        ll = self.table[hashed_key]
        if not ll: # 指定したキーにデータが存在しない場合
            print("No Data")
            return
        if ll.value == value: # 削除するデータが見つかった場合
            if ll.next: # 先頭を削除してリストを1つ前にずらす
                self.table[hashed_key] = ll.next
            else: # データが1つだけの場合
                self.table[hashed_key] = None
            print(f"Key:{key}, Value:{value} Removed")
            return
        ll_prev = ll
        ll = ll_prev.next
        while ll: # 指定したキーに複数の連結リストが存在する場合
            if ll.value == value:
                ll_prev.next = ll.next
                print(f"Key:{key}, Value:{value} Removed")
                return
            else:
                ll_prev
                ll = ll.next
        print("Data not found")

def main():
    # 初期化
    ht = HashTable()
    
    # 追加
    ht.add(1, "orange")
    ht.add(2, "apple")
    ht.add(3, "grape")
    ht.add(1001, "mikan")
    ht.add(1003, "muscat")
    ht.add(2002, "green apple")
    ht.add(3002, "pineapple")
    ht.add(2004, "melon")
    
    # データを表示
    for i in range(1, 5):
        print(f'Key:{i}, Value:{ht.get(i)}')
    
    # 削除
    ht.remove(1, "orange")
    ht.remove(2002, "green apple")
    ht.remove(3, "muscat")
    
    # データを表示
    for i in range(1, 5):
        print(f'Key:{i}, Value:{ht.get(i)}')

if __name__ == "__main__":
    main()
# 連想配列
# 添え字にスカラー値以外のデータ型も使用できる配列
# 適切なハッシュ関数hを設計することで、データ集合Sの
# 各要素xを非負整数値h(x)に対応付けることができる
# 実現するデータ構造としてハッシュテーブルを採用した場合、
# 各要素へのアクセスを平均的にO(1)の計算量で実行できる

class HashTable(object):
    def __init__(self):
        self.size = 11
        self.keys = [None] * self.size
        self.values = [None] * self.size
    
    # ハッシュ関数
    def make_hash(self, key):
        hash_val = 0
        for pos in range(len(key)):
            hash_val += ord(key[pos]) # キーのそれぞれの文字をordで数値化して足す
        hash_val %= self.size # 配列のインデックスに収まるようサイズの剰余を取る
        return hash_val
    
    # 値の挿入・更新
    def add(self, key, data):
        # ハッシュ関数でインデックスを取得し、
        # それを基に加えるキーを探す
        index = self.make_hash(key)
        
        # 空のインデックスを探す、もし同じキーが存在したら値を更新
        while self.keys[index] is not None:
            if self.keys[index] == key:
                self.values[index] = data
                return
            # 次のインデックスに進む
            # 剰余を取ることで、サイズを超えたら最初に戻る
            index = (index + 1) % self.size
        
        self.keys[index] = key
        self.values[index] = data
    
    # 値の取得
    def lookup(self, key):
        # ハッシュ関数でキーからインデックスを求める
        index = self.make_hash(key)
        
        # インデックスに基づき値を探索
        while self.keys[index] is not None:
            if self.keys[index] == key:
                return self.values[index]
            index = (index + 1) % self.size
        
        return False

if __name__ == "__main__":
    hash_table = HashTable()
    
    hash_table.add("apple", 10)
    hash_table.add("banana", 5)
    hash_table.add("orange", 20)
    
    print(hash_table.keys)
    print(hash_table.values)
    print(hash_table.lookup("apple"))
# キュー
# 店の行列などに例えられる、古いデータから先に処理していく考え方
# 最初に挿入された要素から順に取り出していく
# FIFO(first-in first-out)
# 航空券予約のキャンセル待ち処理、印刷機のジョブスケジューリング

MAX = 100000 # キュー配列の最大サイズ

class Queue(object):
    def __init__(self):
        self.qu = [0] * MAX # キューを表す配列
        self.tail = 0 # キューの要素区間を表す変数
        self.head = 0
    
    # キューが空かどうかの判定
    def is_empty(self):
        return (self.head == self.tail)
    
    # キューが満杯かどうか
    # リングバッファで満杯になったら先頭に戻るようにする
    def is_full(self):
        return (self.head == (self.tail + 1) % MAX)
    
    # 挿入
    def enqueue(self, x):
        if self.is_full():
            print("error: queue is full.")
            return
        self.qu[self.tail] = x
        self.tail += 1
        # リングバッファの終端に来たら0に戻る
        if self.tail == MAX: self.tail = 0
    
    # 取り出し
    def dequeue(self):
        if self.is_empty():
            print("error: queue is empty.")
            return -1
        res = self.qu[self.head]
        self.head += 1
        # リングバッファの終端に来たら0に戻る
        if self.head == MAX: self.head = 0
        return res

if __name__ == "__main__":
    queue = Queue()
    
    queue.enqueue(3)
    queue.enqueue(5)
    queue.enqueue(7)
    
    print(queue.dequeue())
    print(queue.dequeue())
    
    queue.enqueue(9)
    
    print(queue.qu[queue.head:queue.tail])
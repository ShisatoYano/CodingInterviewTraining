# マージソート
# O(N log N)の計算量で動作する
# 分割統治法を活用したソートアルゴリズム
# 配列を半分に分割し、左右それぞれを再帰的にソートして
# その両者を併合することを繰り返す
# 右側をひっくり返してつなげた後、左右両側のうち
# 小さい方を順に取っていく

# ソートしたい配列
a = [12, 9, 15, 3, 8, 17, 6, 1]

# 配列のサイズ
N = len(a)

# マージソート
def merge_sort(a, left, right):
    if (right - left) == 1: return
    
    mid = left + int((right - left) / 2)
    
    # 左半分をソート
    merge_sort(a, left, mid)
    
    # 右半分をソート
    merge_sort(a, mid, right)
    
    # いったん左と右のソート結果をコピーしておく
    # 右は左右反転
    buf = []
    for i in range(left, mid): buf.append(a[i])
    for i in range(right-1, mid-1, -1): buf.append(a[i])
    
    # 併合する
    index_left = 0 # 左側の添え字
    index_right = len(buf) - 1 # 右側の添え字
    for i in range(left, right):
        # 左側採用
        if buf[index_left] <= buf[index_right]:
            a[i] = buf[index_left]
            index_left += 1
        # 右側採用
        else:
            a[i] = buf[index_right]
            index_right -= 1

if __name__ == "__main__":
    merge_sort(a, 0, N)
    
    print(a)
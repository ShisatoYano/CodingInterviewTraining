# クイックソート
# 分割統治法にのっとったアルゴリズム
# 最悪時間計算量はO(N^2)
# 平均時間計算量はO(N log N)
# 配列の中から適当な要素pivotを選び出し、
# 配列全体をpivot未満のグループと以上のグループに
# 分割して、それぞれを再帰的に解く

# ソートする配列
a = [10, 12, 15, 3, 8, 17, 4, 1]

# 配列のサイズ
N = len(a)

def quick_sort(a, left, right):
    if (right - left) <= 1: return
    
    # 中点をpivotとする
    pivot_index = int((left + right) / 2)
    pivot = a[pivot_index]
    
    # pivotと右端を入れ替える
    a[pivot_index], a[right-1] = a[right-1], a[pivot_index]
    
    i = left # iは左詰めされたpivot未満要素の右端を表す
    for j in range(left, right-1):
        # pivot未満のものがあったら左に詰めていく
        if a[j] < pivot:
            a[i], a[j] = a[j], a[i]
            i += 1
    a[i], a[right-1] = a[right-1], a[i] # pivotを適切な場所に挿入
    
    # 再帰的に解く
    quick_sort(a, left, i) # 左半分, pivot未満
    quick_sort(a, i+1, right) # 右半分, pivot以上
    
if __name__ == "__main__":
    quick_sort(a, 0, N)
    
    print(a)
# 配列から目的の値を探索する二分探索法
# N = 2^kと表されるとき、配列サイズはk回のステップで1になる
# k = log Nであることから、計算量はO(log N)となる

import math

N = 8

a = [3, 5, 8, 10, 14, 17, 21, 39]

# 目的の値 key の添字を返す
# 存在しない場合は-1
def binary_search(key):
    left = 0
    right = len(a) - 1
    
    while right >= left:
        mid = left + math.floor((right - left)/2)
        
        if a[mid] == key: return mid
        elif a[mid] > key: right = mid - 1
        elif a[mid] < key: left = mid + 1
    
    return -1

def main():
    print(binary_search(10)) # 3
    print(binary_search(3)) # 0
    print(binary_search(39)) # 7
    
    print(binary_search(-100)) # -1
    print(binary_search(9)) # -1
    print(binary_search(100)) # -1
    
if __name__ == "__main__":
    main()
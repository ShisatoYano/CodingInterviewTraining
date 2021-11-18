# 配列の使い方
# C++: std::vector
# Python: list

def main():
    a = [4, 3, 12, 7, 11, 1, 9, 8, 14, 6]
    
    # 0番目の要素の出力: 4
    print(a[0])
    
    # 2番目の要素の出力: 12
    print(a[2])
    
    # 2番目の要素を5に書き換える
    a[2] = 5
    
    # 2番目の要素を出力: 5
    print(a[2])

if __name__ == "__main__":
    main()
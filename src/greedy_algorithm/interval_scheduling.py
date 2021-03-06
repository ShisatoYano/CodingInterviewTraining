# 区間スケジューリング問題
# N個の仕事があり、i(=0,1,...,N-1)番目の仕事は時刻s_iに開始し、
# 時刻t_iに終了する。この中から自分が行う仕事を出来るだけ多く選びたい
# 時刻が重なっている複数の仕事を選ぶことはできない
# 最大で何個の仕事をこなすことができるか
#
# まずはN個の区間に対して、どの順序で選ぶ、選ばないの選択をするかを上手に定める
# 区間の終端時刻が小さい順にソートする
# 任意の区間の選び方に対して、終端時刻が最も早い区間を選ぶように変更できること
# 
# 残っている区間のうち、終端時刻が最も早いものを選ぶ
# その選んだ区間と重なる区間を消す
# 区間が全て無くなるまで繰り返す

def main():
    # 各区間の開始時刻と終端時刻の配列
    intervals =[[9,16],[11,15],[10,12],[15,18],[19,23],[13,19]]
    
    # 終端時刻が早い順にソートする
    # O(N log N) ここがボトルネックになる
    intervals_sorted = sorted(intervals, key=lambda x: x[1])
    
    # 貪欲に選ぶ
    # O(N)
    result = 0
    current_end_time = 0
    for i in range(6):
        # 最後に選んだ区間と被るのは除く
        if intervals_sorted[i][0] < current_end_time: continue
        
        result += 1
        
        current_end_time = intervals_sorted[i][1]
    
    print(result)

if __name__ == "__main__":
    main()
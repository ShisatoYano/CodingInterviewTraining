# 年齢当てゲーム
# Aさんの年齢は20歳以上３６歳未満であるとわかっている
# Aさんに４回までYes/Noで答えられる質問をすることができる
# 
# 一般化した実数上の二分探索法
# f(x) = 0を満たす実数x(l<x<r)のうちの1つを
# いくらでも高い精度で求めることができる
# x=leftは「Aさんの年齢がx未満である」という条件を常に満たさない
# x=rightは「Aさんの年齢がx未満である」という条件を常に満たす

import math

def main():
    print("Start Game!")
    
    # Aさんの数の候補を表す区間 [left, right)
    left = 20
    right = 36
    
    # Aさんの数を1つに絞れないうちは繰り返す
    while (right - left) > 1:
        mid = left + math.floor((right - left)/2) # 真ん中の区間
        
        # mid以上かを聞いて回答をyes/noで受け取る
        ans = input("Is the age less than {} ? (yes/no)".format(mid))
        
        # 回答に応じて、ありうる数の範囲を絞る
        if ans == "yes": right = mid
        else: left = mid
    
    # 当てる
    print("The age is {}!".format(left))

if __name__ == "__main__":
    main()
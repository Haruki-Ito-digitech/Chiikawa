"""ランチの売り上げを計算しよう"""
#import
import math
import sys
args = sys.argv

#引数を変数に代入
karaage_num = int(args[1])
curry_num = int(args[2])
#売り上げ計算
karaage_sell = 760 * karaage_num
curry_cell = 850 * curry_num
all_cell = karaage_sell + curry_cell

#出力
print(all_cell, end="")


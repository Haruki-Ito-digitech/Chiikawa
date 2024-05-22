"""ランチの粗利を計算しよう"""
#import
import math
import sys
args = sys.argv

#引数を変数に代入
karaage_num = int(args[1])
curry_num = int(args[2])

#売り上げ計算
karaage_sell = 760 * karaage_num
curry_sell = 850 * curry_num
all_sell = karaage_sell + curry_sell
all_sell = round(all_sell)

#原価計算
karaage_cost = 0.323 * karaage_sell
curry_cost = 0.284 * curry_sell
all_cost = karaage_cost + curry_cost
all_cost = round(all_cost)

#粗利計算
karaage_profit = karaage_sell - karaage_cost
curry_profit = curry_sell - curry_cost
all_profit = karaage_profit + curry_profit
all_profit = round(all_profit)

#出力
print(f"売上高：{all_sell}、原価：{all_cost}、粗利：{all_profit}", end="")
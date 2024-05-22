"""タクシー運賃を計算しよう"""
#import
import math
import sys
args = sys.argv

#引数を変数に代入
input_num = int(args[1])
#運賃計算
if 1500 >= input_num:   #1500以下なら630円
    fee = 630
else:
    dis = input_num - 1500  #1500m以上進んだ分を取得
    count = dis / 344       #344で割る
    count = math.ceil(count)#切り上げる
    fee = 630 + 98 * count#運賃算出

#出力
print(fee, end="")
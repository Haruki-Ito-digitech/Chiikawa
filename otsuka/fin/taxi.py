#タクシーの運賃
#初乗り1500mまで630円、以降は344mごとに98円
#引数で乗車距離(m)を渡し、運賃を計算せよ

import sys
args = sys.argv

#距離を入力してもらう
kyori = int(args[1])

#距離が1500mより大きい時
if kyori > 1500:
    a = int(kyori - 1500)
    b = int(a // 344)
    money = 98*(b+1) + 630

#距離が1500m以下の時
else:
    money = 630

#料金を出力する
print(money, end="")
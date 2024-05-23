#タクシーの運賃
#初乗り1500mまで630円、以降は344mごとに98円
#引数で乗車距離(m)を渡し、運賃を計算せよ

import sys
args = sys.argv

kyori = int(args[1])

if kyori > 1500:
    a = int(kyori - 1500)
    b = int(a // 344)
    money = 98*(b+1) + 630



else:
    money = 630
print(money, end="")
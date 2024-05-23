#引数で渡した整数画素数化を判定する
#素数の場合：「Prime」、素数以外の場合「not」と表示するプログラム
#1000以上が入力された際には「1000以上は判定できません」と表示

import sys
args = sys.argv

#素数を判定する関数を定義
def is_prime(n):
    #1より小さいものはダメ
    if n <= 1:
        return False
    #2,3はいいよ
    elif n <= 3:
        return True
    #2,3で割れるものはダメ
    elif n % 2 == 0 or n % 3 == 0:
        return False
    #(6k±1)で割り切れなければ素数
    #6k-1の最小の数5からスタート
    i = 5
    #平方根まで調べればいい
    while i * i <= n:
        #もし、6k±1で割り切れたら素数でない
        if n % i == 0 or n % (i + 2) == 0:
            return False
        #次の6k±1へ
        i += 6
    #割り切れなかったら素数
    return True

n = int(args[1])

#1000以上かどうかの判別
if n >= 1000:
    print("1000以上は判定できません", end="")

#素数か素数でないかで表示するものの判別
else:
    if is_prime(n):
        print("Prime", end="")
    else:
        print("not", end="")
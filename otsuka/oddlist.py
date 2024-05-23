#リストを操作し、奇数の添え字の要素のみを出力する

import sys
args = sys.argv
list = ["Kurita", "Tanaka", "Kaneda", "Noda", "Koyama", "Adachi", "Kuriyama", "Ohyama", "Kishida"]

s = list[1::2]
print(s, end="")
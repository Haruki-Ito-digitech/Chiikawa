#リストを操作し、奇数の添え字の要素のみを出力する
#リスト作成
list = ["Kurita", "Tanaka", "Kaneda", "Noda", "Koyama", "Adachi", "Kuriyama", "Ohyama", "Kishida"]

#リストを１番目から最後までを１個づつ飛ばしたリストを作成
s = list[1::2]

#出力
print(s, end="")
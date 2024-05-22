import sys

# リストの生成
list = ["Kurita", "Tanaka", "Kaneda", "Noda", "Koyama", "Adachi", "Kuriyama", "Ohyama", "Kishida"]

# 奇数の添え字の要素のみoddlistに追加
oddlist=[]
for i in range(len(list)):
    if i % 2 == 0:
        continue
    else:
        oddlist.append(list[i])

print(oddlist, end="")
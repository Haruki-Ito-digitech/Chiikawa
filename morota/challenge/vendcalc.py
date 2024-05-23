import sys
args = sys.argv

# 商品リスト
item_list = ["お茶：110円", "コーヒー：100円", "ソーダ：160円", "コーンポタージュ：130円"]
# 商品リスト（辞書型）
items = {"お茶":110, "コーヒー":100, "ソーダ":160, "コーンポタージュ":130}

# 最初の表示
for i in range(len(item_list)):
    print(item_list[i])

# 投入金額のインプット
money = int(input("投入金額を入力してください"))

if money % 10 != 0:
    print("1円玉、5円玉は使用できません。再度投入金額を入力してください")
elif money > 10000:
    print("10,000円を超える金額は投入できません。再度投入金額を入力してください")
elif money < 100:
    print("{0}円では購入できる商品がありません。再度投入金額を入力してください".format(money))
elif money >= 100 and money <= 10000:
    buy_item = input("何を購入しますか（商品名/cancel）")

while money >= 100:
    money -= int(items[buy_item])
    print("残金：{0}円".format(money))
    answer = input("続けて購入しますか（Y/N）")
    if answer == "N":
        break
    buy_item = input("何を購入しますか（商品名/cancel）")





"""特定の要素を出力しよう"""
#リスト作成
list = ["Kurita", "Tanaka", "Kaneda", "Noda", "Koyama", "Adachi", "Kuriyama", "Ohyama", "Kishida"]
#奇数抽出処理
def odd(num):
    odd_numlist = []
    for i in range(num):
        if i % 2 != 0:
            odd_numlist.append(i)
        else:
            pass
    return odd_numlist

#メイン関数
def main():
    #リストの要素数計算
    num = len(list)
    #奇数のリスト取得
    odd_numlist = odd(num)
    #出力格納用リスト
    odd_list = []
    #奇数の部分だけリストから取り出して新しいリストへ挿入
    for i in odd_numlist:
        odd_list.append(list[i])
    #出力
    print(odd_list, end="")

if __name__ == '__main__':
    main()
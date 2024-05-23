#唐揚げ定食（760円、原価率32.3%）、カレーセット(850円、原価率28.4%)
#引数：それぞれの一日の注文数
#一日の売上高、原価、粗利を出力するプログラム
#粗利＝売上高＊原価率　（小数点第一位を四捨五入、）
import sys
args = sys.argv

#引数
kara = int(args[1])
kare = int(args[2])

#売上高の計算
kara_uri = int(kara*760)
kare_uri = int(kare*850)

#原価の計算
kara_gen = float(760 * 0.323 * kara)
kare_gen = float(850 * 0.284 * kare)

#粗利の計算
kara_ara = float(kara_uri) - kara_gen
kare_ara = float(kare_uri) - kare_gen

#合計計算
uri = kara_uri + kare_uri
gen = float(kara_gen + kare_gen )
gen_1 = round(gen) 
ara = float(kara_ara + kare_ara)
ara_1 = round(ara)

#出力
print("売上高："+ str(uri) + "、原価：" + str(gen_1) + "、粗利：" + str(ara_1), end="")
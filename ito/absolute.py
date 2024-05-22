"""絶対値を出力しよう"""
#import
import sys
args = sys.argv

#引数を変数に代入
input_num = int(args[1])
#絶対値変換
absolute_num = abs(input_num)
#文字列変換
input_num = str(input_num)
absolute_num = str(absolute_num)

#出力
print(input_num + " " + absolute_num, end="")



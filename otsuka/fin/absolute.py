import sys
args = sys.argv

#入力された数字をint型に変換する
z = int(args[1])

#絶対値をつける
z_abs = abs(z)

#出力する
print(str(z) + " " + str(z_abs), end="")
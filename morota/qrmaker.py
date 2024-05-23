import os
import sys
import qrcode   #パッケージをインポート
args = sys.argv 

# 引数のフルパスをディレクトリとファイル名に分割
dir_name,file_name = os.path.split(args[1])

#ファイルを１行ずつ読み込む
with open(args[1], encoding="utf-8") as tf:
    for i, line in enumerate(tf):
        img = qrcode.make(line)                               #QRコードを生成
        img.save(os.path.join(dir_name, str(i+1)+".png"))     #ファイルに保存

"""QRコードを大量作成しよう"""
from urllib.parse import urlparse
import qrcode
import os
import sys
arg = sys.argv

#読み込むファイルのパス取得
read_path = arg[1]
#書き込むファイルのパス
write_path = os.path.dirname(read_path) + "/"

#ドメイン名取得処理
def domain(url):
    #URLからドメイン名取得
    parse = urlparse(url)
    dom = parse.netloc
    dom = dom.replace('www.','')
    return dom

#urlの取得
f = open(read_path, 'r')  #ファイル開く
url_list = f.readlines()  #1行ずつ取り出してリストへ格納

#QRコード作成
for url in url_list:
    #qrコードを作成するURL
    img = qrcode.make(url)
    #ドメイン名取得
    dom = domain(url)
    #保存先
    file_name = write_path + dom + ".png"
    #画像の保存（フルパスを作成して保存）
    img.save(file_name)


"""交通費精算を一覧で出力しよう"""
import sys
from database_train import Base, session, ENGINE
from table import Transport
arg = sys.argv

#引数を変数に入力
file_name = arg[1]
#ファイルパス設定
path = f"/home/matcha-23training/chiikawa/Chiikawa/ito/output/{file_name}"
#書き込みデータ格納用リスト作成
new_line = []
#データ取り出し
data_all = session.query(Transport).all()
f = open(path, 'a')

for line in data_all:
        A = '"'
        new_line = str(line.data),str(line.seq),line.departure,line.arrival,line.via,str(line.amount)
        for i in new_line:
            A += i + '","'
        A = A[:-2]
        f.write(A + '\n')
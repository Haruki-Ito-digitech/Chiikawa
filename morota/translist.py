import os
import sys
import datetime
args = sys.argv

from datetime import date 
from database import session
from transinsert_table import Transport

# データの取得
data = session.query(Transport).all()

# 各データをリスト内に格納
data_list = []
for i in range(len(data)):
    data_list.append(data[i].data.strftime('%Y%m%d'))
    data_list.append(str(data[i].seq))
    data_list.append(data[i].departure)
    data_list.append(data[i].arrival)
    data_list.append(data[i].via)
    data_list.append(str(data[i].amount))

#相対パスの生成
path = os.path.join(".", "output", args[1])

#相対パス先のファイルを開く
file = open(path, mode="w", encoding="utf-8")

# テーブルの項目数を変数に格納(6)
items = len(data_list) / (i+1)

#ファイルに書き込む
for n in range(len(data_list)):
    file.write("\""+data_list[n]+"\"")
    if (n+1) % items == 0:
        file.write("\n")
    else:
        file.write(",")
    
#ファイルを閉じる
file.close()
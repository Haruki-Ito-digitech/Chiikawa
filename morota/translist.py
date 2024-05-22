import os
import sys
import datetime
args = sys.argv

from datetime import date 
from database import session
from transinsert_table import Transport

# データの取得
data = session.query(Transport).all()

data_list = []
for i in range(len(data)):
    data_list.append(data[i][0])
    i += 1
print(data_list)

# #相対パスの生成
# path = os.path.join(".", "output", args[1])

# #相対パス先のファイルを開く
# file = open(path, mode="w", encoding="utf-8")

# #ファイルに書き込む
# file.write(str(data_list))

# #ファイルを閉じる
# file.close()
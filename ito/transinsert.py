import sys
from database_train import Base, session, ENGINE
from table import Transport
from datetime import date
arg = sys.argv

#引数を変数に代入
day = str(arg[1])
dt = date(int(day[0:4]), int(day[4:6]), int(day[6:8]))
seq = int(arg[2])
dep = str(arg[3])
ari = str(arg[4])
via = str(arg[5])
amo = int(arg[6])

#入力リスト作成
input_list = [dt, seq, dep, ari, via, amo]
transrate_list =[]
transrate_list.append(input_list)

try:
    for list in transrate_list:
        transport = Transport(data=list[0], seq=list[1], departure=list[2], arrival=list[3], via=list[4], amount=list[5])
        #INSERT処理
        session.add(transport)
        #コミット
        session.commit()
        print("交通費精算テーブルにデータを登録しました")
except:
    print("交通費精算テーブルにデータを登録できませんでした")

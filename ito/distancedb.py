import sys
from sqlalchemy import Column, String, Date, Integer, Numeric
from database_train import Base, session
from database_train import ENGINE
from table_train import Train
arg = sys.argv

#引数を変数に代入
start = str(arg[1])
end = str(arg[2])
#駅名別の距離をそれぞれ取り出す
dis1 = session.query(Train).filter_by(name=start).first()
dis2 = session.query(Train).filter_by(name=end).first()
#距離の算出
dis = abs(dis2.kilo - dis1.kilo)
dis = round(dis,2)
#結果の表示
print(dis, end="")
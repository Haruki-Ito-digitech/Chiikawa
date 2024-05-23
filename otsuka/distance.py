import sys
from sqlalchemy import Column, String, Date, Integer, Numeric
from database import Base,session
from database import ENGINE
from distancedb import STATION
import sys
args = sys.argv

#STATIONからnammeが入力と同じ行をxとyに格納
x = session.query(STATION).filter_by(name =args[1]).first()
y = session.query(STATION).filter_by(name =args[2]).first()

#STATIONでnameが入力されたものの行にあるkiroを出力
print(x.kilo, end="")
print(y.kilo, end="")

#二駅間の距離の計算
w = abs(x.kilo - y.kilo)

#距離を出力
print(w, end="")
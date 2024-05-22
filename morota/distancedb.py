import sys
args = sys.argv

from database import session
from distancedb_table import Stations

# 距離の取得
station1 = session.query(Stations.kilo).filter_by(name = args[1]).first()
station2 = session.query(Stations.kilo).filter_by(name = args[2]).first()

#２駅間の距離の算出
distance = float(station1[0]) - float(station2[0])

print(abs(round(distance, 2)), end="")

from database import session #データーベースへの接続
from distancedb import STATION #テーブル定義

#登録するデータの編集
station = STATION(
    seq = 1, 
    name = "東京", 
    kilo = 0.00
)

station = STATION(
    seq = 2, 
    name = "品川", 
    kilo = 6.78
)

#INSERT処理
session.add(station)

result = session.query(STATION).filter_by(seq=6(6,新大阪,515.35)),delete()

#コミット
session.commit()
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

station = STATION(
    seq = 3, 
    name = "新横浜", 
    kilo = 25.54
)

station = STATION(
    seq = 4, 
    name = "名古屋", 
    kilo = 342.02
)

station = STATION(
    seq = 5, 
    name = "京都", 
    kilo = 476.31
)

station = STATION(
    seq = 6, 
    name = "新大阪", 
    kilo = 515.35
)

#INSERT処理
session.add(station)

#コミット
session.commit()
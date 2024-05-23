from database_train import session
from table_train import Train

#データ登録
name_list = ["東京", "品川", "新横浜", "名古屋", "京都", "新大阪"]
kilo_list = ["0.00", "6.78", "25.54", "342.02", "476.31", "515.35"]
for i in range(1,6):
    station = Train(
        seq = i,
        name = name_list[i],
        kilo = kilo_list[i]
    )
    #INSERT処理
    session.add(station)
    #コミット
    session.commit()
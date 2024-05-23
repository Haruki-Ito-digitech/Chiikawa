#駅間テーブル(テーブル名：stations)に新幹線駅名と東京駅からの距離を定義し
#第二引数と第三引数に設定した駅名の間の距離を計算し出力する。

import sys
from sqlalchemy import Column, String, Date, Integer, Numeric 
from database import Base
from database import ENGINE

#テーブル：STATIONの定義
class STATION(Base):
    __tablename__ = 'station'
    seq = Column('station_number',Integer, primary_key = True)
    name = Column('station_name',String(20) )
    kilo = Column('km', Numeric(6,2))

#テーブル：TRANSPORTの定義
class TRANSPORT(Base):
    __tablename__ = 'transport'
    data =Column('day', Date, primary_key = True)
    seq = Column('station_number',Integer, primary_key = True)
    depature = Column('start',String(20))
    arrival = Column('goal',String(20))
    via = Column('keiyu',String(20))
    amount = Column('money', Integer)
   
def main(args):
    """
    メイン関数
    """
    Base.metadata.create_all(bind=ENGINE)

if __name__ == "__main__":
        main(sys.argv)
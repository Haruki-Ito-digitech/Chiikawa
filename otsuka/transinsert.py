import sys
from sqlalchemy import Column, String, Date, Integer, Numeric
from database import Base,session
from database import ENGINE
from distancedb import TRANSPORT
import sys
args = sys.argv

try:
    hairetu = TRANSPORT(data = args[1],
                    seq = args[2],
                    depature = args[3],
                    arrival = args[4],
                    via = args[5],
                    amount = args[6]
                    )

    session.add(hairetu)
    session.commit()
    print("交通費精算テーブルにデータを登録しました")

except :
    print("error:交通費精算テーブルにデータを登録できませんでした")
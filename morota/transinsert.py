import sys
import datetime
args = sys.argv

from datetime import date 
from database import session
from transinsert_table import Transport
from sqlalchemy.exc import IntegrityError

#日付読み込み
day = datetime.datetime.strptime(sys.argv[1], "%Y%m%d")

# 登録するデータの編集
transport = Transport(
    data = day.date(),
    seq = int(args[2]),
    departure = args[3],
    arrival = args[4],
    via = args[5],
    amount = int(args[6])
)

# エラー処理
try:
    session.add(transport)                              # INSET処理
    session.commit()                                    # コミット
    print("交通費精算テーブルにデータを登録しました")
except IntegrityError as sqlalchemy_error:
    print("error:交通費精算テーブルにデータを登録できませんでした")
except:
    print("error:交通費精算テーブルにデータを登録できませんでした")

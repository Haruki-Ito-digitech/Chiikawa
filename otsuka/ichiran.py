import sys
from sqlalchemy import Column, String, Date, Integer, Numeric
from database import Base,session
from database import ENGINE
from distancedb import TRANSPORT
import sys
args = sys.argv

a_file = open("output.txt", mode="w",encoding="utf-8")

s = session.query(TRANSPORT).all()

for line in s:
    a_file.write('"')
    q = str(line.data)
    a_file.write(q)
    a_file.write('","')
    qq = str(line.seq)
    a_file.write(qq)
    a_file.write('","')
    a_file.write(line.depature)
    a_file.write('","')
    a_file.write(line.arrival)
    a_file.write('","')
    a_file.write(line.via)
    a_file.write('","')
    qqq = str(line.amount)
    a_file.write(qqq)
    a_file.write('"')

a_file.close()

#ファイルを閉じる
with open("output.txt", encoding="utf-8") as f:
    s = f.read()
    print(s)
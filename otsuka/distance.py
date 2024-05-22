import sys
from sqlalchemy import Column, String, Date, Integer, Numeric
from database import Base,session
from database import ENGINE
from distancedb import STATION
import sys
args = sys.argv

#x = session.query(STATION.kilo).filter(STATION.name == args[1])
#y = session.query(STATION.kilo).filter(STATION.name == args[2])

#print(x, end="")
#print(y, end="")

#a = float(x)
#b = float(y)
#w = abs(a - b)

#print(w, end="")
import sys
args = sys.argv

karaage = int(args[1])
curry = int(args[2])

# 料金計算
print(760*karaage + 850*curry, end="")


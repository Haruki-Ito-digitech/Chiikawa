import sys
args = sys.argv

karaage = int(args[1])
karee = int(args[2])

uriage = (karaage*760 + karee*850)

print(uriage,end="")
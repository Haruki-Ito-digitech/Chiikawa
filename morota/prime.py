import sys
args = sys.argv

num = int(args[1])

# 引数が1000以上の場合
if num >= 1000:
    print("1000以上は判定できません", end="")
# 引数が1000未満の場合
# 素数判定
else:
    prime = True
    for i in range(2, num):
        if num % i == 0:
            prime = False
            break

# PrimeがTrueかFalseか
    if prime:
        print("Prime", end="")
    elif prime == False:
        print("not", end="")



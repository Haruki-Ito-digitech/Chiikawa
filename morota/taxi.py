import sys
args = sys.argv

m = int(args[1])

# 料金計算
if m <= 1500:                                  # 1500mまで
    price = 630
else:                                          # 1500m以後
    add_m = divmod((m - 1500), 344)            # divmod()で商とあまり
    price = 630 + (98 * (add_m[0] + 1))        # 追加料金分の計算

print(price, end="")
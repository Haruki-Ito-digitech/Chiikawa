import sys
args = sys.argv

#　売上個数
karaage = int(args[1])
curry = int(args[2])

# 料金計算
# 売上
sales_k = 760*karaage
sales_c = 850*curry
sales = sales_k + sales_c

# 原価
cost = round(sales_k*0.323 + sales_c*0.284, 0)

# 粗利
profit = sales - round(sales_k*0.323) - round(sales_c*0.284)

print("売上高：{0}、原価：{1:.0f}、粗利：{2}".format(sales, cost, profit), end="")
# {1:.0f}は表示範囲の指定
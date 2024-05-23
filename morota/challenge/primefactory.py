import sys
args = sys.argv

n= int(args[1])

# 素因数分解
prime = []
while n % 2 == 0:
    prime.append(2)
    n //= 2
f = 3
while f * f <= n:
    if n % f == 0:
        prime.append(f)
        n //= f
    else:
        f += 2
if n != 1:
    prime.append(n)

print(prime, end="")
        

mcd = lambda m,n: m if n == 0 else mcd(n,m%n)
print(mcd(4,3))
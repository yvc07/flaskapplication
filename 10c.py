gcd=lambda m,n:m if not n else gcd(n,m%n)
print(gcd(5,25))
lcm=lambda m,n:m if not n else m*n// gcd(n,m%n)
print(lcm(2,3))

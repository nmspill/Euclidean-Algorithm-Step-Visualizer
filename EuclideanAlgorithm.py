
def gcd(a, b):

    while a % b != 0:
        print("%d = %d*%d + %d\n" % (a, b, a//b, a % b))
        r = a % b
        a = b
        b = r

    print("%d = %d*%d + %d\n" % (a, b, a // b, a % b))

    return b


print("gcd(a, b)")
gcdA = int(input("a = "))
gcdB = int(input("b = "))
print()
print("a = bq + r\n")
print("gcd(%d, %d) = %d" % (gcdA, gcdB, gcd(gcdA, gcdB)))

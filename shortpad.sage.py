def franklinreiter(n, e, r, c1, c2):
    R.<X> = Zmod(n)[]
    f1 = X^e - c1
    f2 = (X + r)^e - c2

    return (n-(compositeModulusGCD(f1,f2)).coefficients()[0])

def compositeModulusGCD(a,b):
    if (b == 0):
        return a.monic()
    else:
        return compositeModulusGCD(b, a%b)

def coppersmithshortpad(e, n, c1, c2, eps=1/30):

    import binascii
    P.<x,y> = PolynomialRing(ZZ)
    ZmodN = Zmod(N)
    g1 = x^e - c1
    g2 = (x+y)^e - c2

    result = g1.resultant(g2)
    P.<y> = PolynomialRing(ZmodN)

    raw_input()
    print(str(res).replace('^','**'))
    r_result = input()

    diff = r_result.small_roots(epsilon=eps)[0]
    recoveredM1 = franklinreiter(n, e, diff, c1, c2)
    for i in range(8):
        msg = hex(Integer(recoveredM1*pow(2,i)))
        if(len(msg)%2 == 1):
            msg = '0' + msg
        if(msg[:2]=='0x'):
            msg = msg[:2]
        print(binascii.unhexlify(msg))



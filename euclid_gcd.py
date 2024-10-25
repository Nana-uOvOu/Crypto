def gcd(a,b):
    #递归算法
    r = a % b
    if r == 0:
        return b
    else:
        return gcd(b,r)

def extended_gcd(a,b):
    x = [1,0]
    y = [0,1]
    i = 2
    r = 1
    while r != 0:
        r = a % b
        q = a // b
        if r == 0:
            return b, x[len(x)-1], y[len(y)-1]
        a = b
        b = r
        x.append(x[i-2] - q * x[i-1])
        y.append(y[i-2] - q * y[i-1])
        i += 1




if __name__ == '__main__':
    a = 1160718174
    b = 316258250
    print(gcd(a,b))

    print(extended_gcd(3,8))
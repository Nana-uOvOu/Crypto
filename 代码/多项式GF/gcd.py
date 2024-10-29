import poly_calculate as pc
import AES
def gcd(a,b):
    q_x,r_x = a / b
    if r_x == pc.poly_nomial("0"):
        return b
    else:
        return gcd(b,r_x)
    
def extended_gcd(a,b):
    x = [AES.AES_poly("1"),AES.AES_poly("0")]
    y = [AES.AES_poly("0"),AES.AES_poly("1")]
    i = 2
    r = AES.AES_poly("1")
    if a.max_power < b.max_power:
        a,b = b,a
    while r != AES.AES_poly("0"):
        print(f"i={i},a={a},b={b}")
        q,r = a / b
        if r == AES.AES_poly("0"):
            return b, x[len(x)-1], y[len(y)-1]
        a = b
        b = r
        x.append(x[i-2] - q * x[i-1])
        y.append(y[i-2] - q * y[i-1])
        print(f"i={i},x={x[i]},y={y[i]},q={q},r={r}")
        i += 1

if __name__ == "__main__":
    a = AES.AES_poly("10000011")
    b = AES.AES_poly("100011011")
    print(f"gcd(a,b)={gcd(a,b)}")
    c,x,y = extended_gcd(a,b)
    print(f"c={c},x={x},y={y}")
import poly_calculate as pc


def gcd(a, b):
    q_x, r_x = a / b
    if r_x == pc.poly_nomial("0"):
        return b
    else:
        return gcd(b, r_x)


def extended_gcd(a, b):
    x = [AES_poly("1"), AES_poly("0")]
    y = [AES_poly("0"), AES_poly("1")]
    i = 2
    r = AES_poly("1")
    while r != AES_poly("0"):
        q, r = a / b
        if r == AES_poly("0"):
            return b, x[len(x) - 1], y[len(y) - 1]
        a = b
        b = r
        x.append(x[i - 2] - q * x[i - 1])
        y.append(y[i - 2] - q * y[i - 1])
        i += 1

class AES_poly(pc.poly_nomial):
    ire_poly = pc.poly_nomial("100011011")
    def __init__(self, p):
        super().__init__(p)
        if self.max_power > 7 and not (self == AES_poly.ire_poly):
            # 多项式次数过高，则需要模不可约多项式
            _,r_x = self / AES_poly.ire_poly
            self.max_power = r_x.max_power
            self.para = r_x.para
            self.power = r_x.power
    def __mul__(self,other):
        a = super().__mul__(other)
        return AES_poly(a.para)

def get_AES_mul_inverse():
    mul_inverse_table = {}
    temp = ["0"] * 8
    for i in range(1,2 ** 8):
        t_i = i
        for j in range(8):
            if t_i // (2 ** (7-j)) == 1:
                temp[j] = "1"
                t_i -= (2 ** (7-j))
        _,_,mul_inverse_table["".join(temp)] = extended_gcd(AES_poly.ire_poly,AES_poly(temp))
        temp = ["0"] * 8

    return mul_inverse_table
mul_inverse_table = get_AES_mul_inverse()


    


if __name__ == "__main__":
    a = AES_poly("1010111")
    b = AES_poly("10000011")
    print(f"add={a+b}")
    print(f"a*b={a*b}")
    for key in mul_inverse_table.keys():
        print(f"table[{key}]={''.join(mul_inverse_table[key].para)}")

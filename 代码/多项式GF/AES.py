import poly_calculate as pc

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
    


if __name__ == "__main__":
    a = AES_poly("1010111")
    b = AES_poly("10000011")
    print(f"add={a+b}")
    print(f"a*b={a*b}")

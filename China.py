import euclid_gcd as g
def china(rs,ps):
    #转换为求解逆元的过程
    X = 0
    for i in range(len(rs)):
        y_e = 1
        for j in range(len(rs)):
            if j != i:
                y_e *= ps[j]
        _,k,_ = g.extended_gcd(y_e,ps[i])
        X += rs[i] * k * y_e
    return X

if __name__ == '__main__':
    rs = [2,3,2]
    ps = [3,5,7]
    print(china(rs,ps))
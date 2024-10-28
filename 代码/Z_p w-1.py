import euclid_gcd as g
def isPrime(p):
    if p % 2 == 0:
        return False 
    for i in range(2,p-1):
        if p % i == 0:
            return False 
    return True 
def get_w_1(p):
    if not isPrime(p):
        print(f"{p} is not a prime!")
        return -1
    res = {0:"-"}
    for i in range(1,p):
        _,x,y = g.extended_gcd(p,i)
        res[i] = y 
    return res 

if __name__ == "__main__":
    print(get_w_1(7))


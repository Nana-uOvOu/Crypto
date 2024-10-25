import random
def rabin_miller(n,t):
    if n % 2 == 0:
        print(f"{n}是合数")
    #随机选取t个a
    aa = []
    while len(aa) < t:
        rint = random.randint(2,n-2)
        if aa.count(rint)==0:
            aa.append(rint)

    #将奇整数分解
    k = 1
    while int((n-1) / (2 ** k)) % 2 == 0:
        k += 1
    q = int((n - 1) / (2 ** k))

    #j = 0时，查看是否a^q mod n为1
    for a in aa:
        flag = False
        if (a ** q) % n == 1:
            flag = True
        if not flag:
            for j in range(0,k):
                if (a ** ((2 ** j) * q)) % n == n-1:
                    flag = True
                    break
        if not flag:
            print(f"{n}是合数")
            return
    print(f"在{t}次测试下，{n}均通过测试，可能是素数")













if __name__ == '__main__':
    n = 29
    t = 10
    rabin_miller(n,t)
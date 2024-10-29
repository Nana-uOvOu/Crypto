class poly_nomial(object):
    def __init__(self,poly_para):
        index = -1
        for i in reversed(range(len(poly_para))):
            if poly_para[i] == "0" and index == -1:
                index = i 
            elif poly_para[i] == "1":
                index = -1
        if index != -1:
            self.para = [i for i in poly_para[index+1:len(poly_para)]]
        else:
            self.para = [i for i in poly_para] 
        if len(self.para) == 0:
            self.para = ["0"]
        self.max_power = len(self.para) - 1
        self.power = list(reversed(range(len(self.para))))
    
    def __len__(self):
        return len(self.para)

    
    def __str__(self):
        s = ""
        for i in range(len(self)):
            if self.para[i] != "0":
                if self.power[i] == 0:
                    s += "1"
                else:
                    s += f"x^{self.power[i]}"
                if i != len(self):
                    s += "+"
        if s.endswith("+"):
            s = s[:len(s)-1]
        if len(s) == 0:
            return "0"
        return s
    
    # 定义加函数
    def __add__(self,other):
        # 找出最大次数，并将小次数的para补全
        i,j = len(self),len(other)
        a = self.para.copy()
        b = other.para.copy()
        if i < j:
            self.para = ["0"] * (j - i) + self.para 
            i = j
        elif i > j:
            other.para = ["0"] * (i - j) + other.para 
            j = i 
        res = ["0"] * i 
        for i in range(j):
            # 每位异或
            res[i] = str(int(self.para[i]) ^ int(other.para[i]))
        self.para = a
        other.para = b
        return poly_nomial(res) 
    
    # 定义减函数，与加一致
    def __sub__(self,other):
        # 找出最大次数，并将小次数的para补全
        i,j = len(self),len(other)
        a = self.para.copy()
        b = other.para.copy()
        if i < j:
            self.para = ["0"] * (j - i) + self.para 
            i = j
        elif i > j:
            other.para = ["0"] * (i - j) + other.para 
            j = i 
        res = ["0"] * i 
        for i in range(j):
            # 每位异或
            res[i] = str(int(self.para[i]) ^ int(other.para[i]))
        self.para = a
        other.para = b
        return poly_nomial(res) 
        
    def __mul__(self,other):
        #self×other，按照竖式计算，将other每一位提取出来
        temp = []
        for i in range(len(other)):
            if other.para[i] == "1":
                p = ["0"] * (self.max_power + other.max_power + 1)
                for j in range(len(self)):
                    if self.para[j] == "1":
                        p[len(p) - 1 - other.power[i] - self.power[j]] = "1"
                temp.append(poly_nomial(p))
        a = poly_nomial("0")
        for p in temp:
            a = a + p
        return a 



    def __truediv__(self,other):
        end_max_power = self.max_power 
        div_max_power = other.max_power 
        if end_max_power < div_max_power:
            # 若被除数次数<除数，则直接返回
            return poly_nomial("0"),poly_nomial(other.para)
        q_x = ["0"] * (end_max_power - div_max_power + 1)
        q_x_power = list(reversed(range(len(q_x))))
        r_x = poly_nomial(self.para)
        for i in range(len(q_x)):
            if r_x == poly_nomial("0"):
                return poly_nomial(q_x),r_x 
            r_x_max = r_x.power[0]
            temp_max = q_x_power[i] + other.power[0]
            if r_x_max < temp_max:  # 如果除法过大除不尽，则使i++
                i = i + 1
            else:
                q_x[i] = "1"
                temp = poly_nomial(["1"] + q_x_power[i] * ["0"]) * other
                r_x = r_x - temp 
        return poly_nomial(q_x),r_x 
    
    def __eq__(self,other):
        if len(self) != len(other):
            return False 
        for i in range(len(self)):
            if self.para[i] != other.para[i]:
                return False 
        return True

            

            
            
        

    

if __name__ == "__main__":
    poly_1 = poly_nomial("10111011")
    poly_2 = poly_nomial("1011")
    print(poly_1)
    print(poly_2)
    print(f"add:{poly_1+poly_2}")
    print(f"mul:{(poly_1 * poly_2)}")
    q_x,r_x = poly_1/poly_2
    print(f"div:q(x)={q_x},r(x)={r_x}")
    print(f"mul1:{poly_1 * poly_nomial("1")}")
    q,r = poly_nomial("110") / poly_nomial("1")
    print(f"div1:{q},{r}")


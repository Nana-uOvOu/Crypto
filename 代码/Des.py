import random
PC1_table = [ 57, 49, 41, 33, 25, 17,  9,
			  1, 58, 50, 42, 34, 26, 18,
			 10,  2, 59, 51, 43, 35, 27,
			 19, 11,  3, 60, 52, 44, 36,
			 63, 55, 47, 39, 31, 23, 15,
			  7, 62, 54, 46, 38, 30, 22,
			 14,  6, 61, 53, 45, 37, 29,
			 21, 13,  5, 28, 20, 12,  4 ]

PC2_table = [ 14, 17, 11, 24, 1,   5,
			  3, 28, 15,  6, 21, 10,
			 23, 19, 12,  4, 26,  8,
			 16,  7, 27, 20, 13,  2,
			 41, 52, 31, 37, 47, 55,
			 30, 40, 51, 45, 33, 48,
			 44, 49, 39, 56, 34, 53,
			 46, 42, 50, 36, 29, 32 ]

p_boxes = [ 16, 7, 20, 21, 29, 12, 28, 17, 1, 15, 23, 26, 5, 18, 31,
			 10, 2, 8, 24, 14, 32, 27, 3, 9, 19, 13, 30, 6, 22, 11, 4, 25 ]


s1 = [
		[ 14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7 ],
		[ 0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8 ],
		[ 4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0 ],
		[ 15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13 ] ]
 
s2 = [
		[ 15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10 ],
		[ 3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5 ],
		[ 0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15 ],
		[ 13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9 ] ]
 
s3 = [
		[ 10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8 ],
		[ 13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1 ],
		[ 13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7 ],
		[ 1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12 ] ]
 
s4 = [
		[ 7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15 ],
		[ 13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9 ],
		[ 10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4 ],
		[ 3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14 ] ]
 
s5 = [
		[ 2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9 ],
		[ 14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6 ],
		[ 4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14 ],
		[ 11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3 ] ]
 
s6 = [
		[ 12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11 ],
		[ 10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8 ],
		[ 9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6 ],
		[ 4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13 ] ]
 
s7 = [
		[ 4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1 ],
		[ 13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6 ],
		[ 1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2 ],
		[ 6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12 ] ]
 
s8 = [
		[ 13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7 ],
		[ 1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2 ],
		[ 7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8 ],
		[ 2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11 ] ]

s_boxes = [s1,s2,s3,s4,s5,s6,s7,s8]

# 修正后的二进制转换函数
def get_str_binary(s):
    return ''.join(format(ord(char), '08b') for char in s)

# 修正后的字符串转换函数
def binary_to_str(binary_text):
    result = []
    for i in range(0, len(binary_text), 8):
        result.append(chr(int(binary_text[i:i+8], 2)))
    return "".join(result)

def get_main_key(key_text):
    if len(key_text) < 8:
        key = get_str_binary(key_text)
        key += "0" * 8 * (8 - len(key_text))
    else:
        key = get_str_binary(key_text[0:8])
    return key
# 分组密码：将明文转换为64位一组
def split_plain_text(plain_text):
    groups = []
    # 分64位一组
    while(len(plain_text) > 64):
        groups.append(plain_text[0:64])
        plain_text = plain_text[64:]
    # 剩余正好64位，全部加入
    if len(plain_text) == 64:
        groups.append(plain_text)
    # 剩余不足64位时，需要padding
    else:
        groups.append(plain_text + "0" * (64 - len(plain_text)))
    return groups
def oplus(x, y):
    return ''.join(str(int(a) ^ int(b)) for a, b in zip(x, y))
def IP(group):
    # 构建IP表
    IP_table = 64 * [0]
    IP_head = [58,60,62,64,57,59,61,63] # head保存每行第一个值，后面7个值都是反复减8得到的
    for i in range(8):
        for j in range(8):
            IP_table[i*8+j] = IP_head[i] - 8 * j
    new_group = 64 * [0]
    for i in range(64):
        new_group[i] = group[IP_table[i] - 1]   # 表格中是从1开始计数的，而Python需要从0开始，故-1
    return new_group 

def FP(group):
    FP_head = [40,8,48,16,56,24,64,32]
    FP_table = [0] * 64
    new_group = [0] * 64
    for i in range(8):
        for j in range(8):
            FP_table[8*i+j] = FP_head[j] - i
    for i in range(64):
        new_group[i] = group[FP_table[i]-1]
    return new_group 

def expand_R(R):
    expanded_R = [0] * 48
    # 生成新增的左右两列
    new_left = [32] + [4 * i for i in range(1,8)]
    new_right = [1 + 4 * i for i in range(1,8)] + [1]
    index = 0
    for i in range(8):
        # 每一行先增加左侧列的值
        expanded_R[index] = R[new_left[i]-1]
        index += 1
        for j in range(4):
            expanded_R[index] = R[j + 4*i]
            index += 1
        #放入右侧值
        expanded_R[index] = R[new_right[i]-1]
        index += 1
    return expanded_R

def PC1(key):
    new_key = [0] * 56
    for i in range(56):
        new_key[i] = key[PC1_table[i] - 1]
    return new_key
def PC2(key):
    new_key = [0] * 48
    for i in range(48):
        new_key[i] = key[PC2_table[i] - 1]
    return new_key
def loop_left_move(key):
    temp = key[0]
    for i in range(0,len(key)-1):
        key[i] = key[i+1]
    key[len(key) - 1] = temp 
    return key
# 修正后的密钥生成
def subkey_generate(main_key):
    main_key = PC1(main_key)
    C, D = main_key[:28], main_key[28:]
    shifts = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]
    keys = []
    for shift in shifts:
        C, D = C[shift:] + C[:shift], D[shift:] + D[:shift]
        keys.append(PC2(C + D))
    return keys

def S_box(R_oplus_key):
    new_R = []
    for i in range(8):
        group = R_oplus_key[i*6:(i+1)*6]
        row = int(group[0] + group[-1], 2)
        col = int(group[1:5], 2)
        val = s_boxes[i][row][col]
        new_R.append(format(val, '04b'))
    return ''.join(new_R)


def P_box(R_S):
    new_R = [0] * 32
    for i in range(32):
        new_R[i] = R_S[p_boxes[i]-1]
    return new_R
        
def DES(plain_text, key, mode="enc"):
    plain_text = get_str_binary(plain_text)
    main_key = get_main_key(key)
    groups = split_plain_text(plain_text)
    keys = subkey_generate(main_key)
    if mode == 'dec':
        keys = keys[::-1]

    new_groups = []
    for group in groups:
        group = IP(group)
        L, R = group[:32], group[32:]
        for i in range(16):
            R_expanded = expand_R(R)
            R_oplus_key = oplus(R_expanded, keys[i])
            R_S = S_box(R_oplus_key)
            R_P = P_box(R_S)
            L, R = R, oplus(L, R_P)
        group = FP(R + L) 
        new_groups.append(group)
    res = new_groups[0]
    for i in range(1,len(new_groups)):
        res += new_groups[i]
    result = ''.join(res)
    return binary_to_str(result)
    

            
        
if __name__ == "__main__":
    plain_text = "FFFZZZYYYIIISSSAAABBBIIIGGGPPPIIIGGG!!!"
    encrypted_text = DES(plain_text, "CongMing", "enc")
    dec_text = DES(encrypted_text, "CongMing", 'dec')
    print(f"Encrypted: {encrypted_text}")
    print(f"Decrypted: {dec_text}")
    
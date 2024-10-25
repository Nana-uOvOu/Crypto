def get_str_binary(s):
    # 使用ord函数将s的每一个字符转换为int数字，之后用bin转换为二进制
    res_list = [bin(ord(i)) for i in s]
    # 注意去除中间的b
    if len(res_list) == 1:
        return res_list[0][0] + res_list[0][2:]
    else:
        res = res_list[0][0] + res_list[0][2:] + res_list[1][0] + res_list[1][2:]
        for i in range(2,len(res_list)):
            res += res_list[i][0] + res_list[i][2:]
        return res 
    
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





if __name__ == "__main__":
    plain_text = get_str_binary("FZY is a BIG PIG!!!!!")
    groups = split_plain_text(plain_text)
    for g in groups:
        print(len(g))
        print(g)
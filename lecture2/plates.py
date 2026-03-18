def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    # 规则1：长度必须在2到6之间
    if not (2 <= len(s) <= 6):
        return False

    # 规则2：只能包含字母和数字（无标点、空格等）
    if not s.isalnum():
        return False

    # 规则3：前两个字符必须是字母
    if not (s[0].isalpha() and s[1].isalpha()):
        return False

    # 规则4：数字只能出现在末尾，且第一个数字不能是'0'
    # 找到第一个数字的位置
    for i, ch in enumerate(s):
        if ch.isdigit():
            # 第一个数字不能是'0'
            if ch == '0':
                return False
            # 检查从该位置开始是否全是数字
            if not s[i:].isdigit():
                return False
            break  # 找到第一个数字后即可结束检查

    # 所有规则通过
    return True

main()
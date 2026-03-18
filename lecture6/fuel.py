while True:
    try:
        x, y = map(int, input("Fraction: ").split("/"))
        if y == 0:
            raise ZeroDivisionError            #raise用于主动报告错误状态
        if x > y:
            raise ValueError
        break
    except (ValueError, ZeroDivisionError):
        pass

#计算部分
percentage = round(x / y * 100)
if percentage <= 1:
    print("E")
elif percentage >= 99:
    print("F")
else:
    print(f"{percentage}%")
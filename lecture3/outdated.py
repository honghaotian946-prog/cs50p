months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]


while True:
    a = input("Date:").strip()     
    if "/" in a:
        try:
            b,c,d = a.split("/")
            if len(b) == 1:
                b = "0"+b
            if len(c) == 1:
                c = "0"+c
                if 1 <= int(b) <= 12 and 1 <= int(c) <= 31:    
                    print(f"{d}-{b}-{c}")
                    break
        except ValueError:
            pass
    
    elif " " in a:
        try:
            e,f,g = a.split(" ")
            e = str(months.index(e)+1)
            f = f[0]
            if len(f) == 1:
                f = "0"+f
            if len(e) == 1:
                e = "0"+e    
                if 1 <= int(e) <= 12 and 1 <= int(f) <= 31:
                    print(f"{g}-{e}-{f}")
                    break
        except ValueError:
            pass
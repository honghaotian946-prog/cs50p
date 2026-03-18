import re

def main():
    print(convert(input("Hours: ")))


def convert(s):
    try:
        matches = re.search(r"^(\d{1,2}):?\s?(\d{2})? (AM|PM) to (\d{1,2}):?\s?(\d{2})? (AM|PM)$",s)
        if not matches:
            raise ValueError("Invalid Time")
        a,b,c,d,e,f = matches.groups()
        a = int(a)
        d = int(d)
        b = int(b) if b is not None else 0
        e = int(e) if e is not None else 0
        
        if not ( 0 <= b <= 59
                and 0 <= e <= 59
                and 1 <= a <= 12
                and 0 <= d <= 12
        ):
            raise ValueError
            
        if c == "PM" and a < 12:
            a += 12
        if c == "PM" and a == 12:
            a = 0
        if f == "PM" and d < 12:
            d += 12
        if f == "PM" and d == 12:
            d = 0
            
    except ValueError:
        return None
    else:
        return f"{a:02d}:{b:02d} to {d:02d}:{e:02d}"      

if __name__ == "__main__":
    main()
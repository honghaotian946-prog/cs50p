from datetime import date
import sys
import inflect

def get_num():
    born_day = input("Date of Birth: ")
    if born_day[4] != "-" or born_day[7] != "-":
        sys.exit("Invalid date")
    today = date.today()
    delta = today - date.fromisoformat(born_day)
    return int(delta.total_seconds() // 60)

    

def main():
    p = inflect.engine()
    num = get_num()
    print(f"{p.number_to_words(num)} minutes.")



if __name__ == "__main__":
    main()
import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    matches = re.search(r'"https?://(?:youtube\.com|www\.youtube\.com)/embed/([0-9a-zA-Z_]+)".*',s)
    if matches:
        return f"https://youtu.be/{matches.group(1)}"


if __name__ == "__main__":
    main()
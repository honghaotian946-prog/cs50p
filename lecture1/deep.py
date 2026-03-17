num = input("What is the Answer to the Great Question of Life, the Universe, and Everything?")

match num:
    case "42"|"forty-two"|"Forty two":
        print("Yes")
    case _:
        print("No")
names = []
while True:
    try:
        name = input("Name:").strip()
        if name:    
            names.append(name)

    except EOFError:
        break

    if len(names) == 1:
        farewell = names[0]
    elif len(names) == 2:
        farewell = names[0] + " and " + names[1]
    else:
        farewell = ",".join(names[:-1]) + f",and {names[-1]}"
    
    print("Adieu,adieu,to",farewell)
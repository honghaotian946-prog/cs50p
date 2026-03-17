x,y,z = (*input("Expression: ").split(),)

x = int(x)
z = int(z)
print(round(eval(f"{x}{y}{z}"),1))
print("""
    *******************
    *** CALCULADORA ***
    *******************
""")

u = int(input("Digite o numero >: "))

for i in range(1, 11):
    print(f"{u} x {i:2} = {i*u}")

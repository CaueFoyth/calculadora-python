print("-=-"*20)
n1 = float(input("Informe o primeiro valor: "))
print("-=-"*20)
operador = str(input("Informe o operador (+, -, *, /): "))
print("-=-"*20)
n2 = float(input("Informe o segundo valor: "))
print("-=-"*20)
if operador == "+":
    print(f"A resposta é {n1+n2}")
elif operador == "-":
    print(f"A resposta é {n1-n2}")
elif operador == "*":
    print(f"A resposta é {n1*n2}")
elif operador == "/":
    print(f"A resposta é {n1/n2}")
print("-=-"*20)
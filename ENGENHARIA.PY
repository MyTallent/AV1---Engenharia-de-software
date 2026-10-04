print("==========CALCULADORA BASICA==========")
numero1 = float(input("Digite o primeiro numero:"))
numero2 = float(input("Digite o segundo numero"))
operacao = input("Digite a operação desejada: +, -, *, /")

if operacao == "+":
    resultado = numero1 + numero2
elif operacao == "-":
    resultado = numero1 - numero2
elif operacao == "*":
    resultado = numero1 * numero2
elif operacao == "/":
    resultado = numero1 / numero2

print("O resultado é:", resultado)


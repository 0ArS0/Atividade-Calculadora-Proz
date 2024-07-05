def calculadora(num1,num2,op):
    if(op == 1):
        return num1 + num2
    elif(op == 2):
        return num1 - num2
    elif(op == 3):
        return num1 * num2
    elif(op == 4):
        return num1 / num2
    else:
        return 0
    
print("--Calculadora--")
num1 = int(input("Digite um numero: "))
num2 = int(input("Digite outro numero: "))

print("\nPosiveis Operações: ")
print("1. Soma\n" + "2. Subtração\n" + "3. Multiplicação\n" + "4. Divisão\n")

opcao = int(input("Qual operação você deseja realizar: "))

print(f"Resultado: {calculadora(num1,num2,opcao)}")




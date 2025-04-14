#calculadora de numeros completos
def suma(a, b):
    return a + b   

def subtrair(a, b):
    return a - b   

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed."
    return a / b
def potencia(a, b):
    return a ** b  
def raiz_quadrada(a):
    if a < 0:
        return "Error: Cannot calculate square root of a negative number."
    return a ** 0.5

def calculadora():
    print("bem-vindo a calculadora de numeros completos")
    print("Selecione a operação:") 
    print("1. Soma")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. Potência")
    print("6. Raiz quadrada")
    print("7. Sair")
    while True:
        escolha = input("Digite sua escolha (1/2/3/4/5/6/7): ")
        if escolha == '7':
            print("Saindo da calculadora.")
            break
        if escolha in ['1', '2', '3', '4']:
            num1 = int(input("Digite o primeiro número: "))
            num2 = int(input("Digite o segundo número: "))

            if escolha == '1':
                print(f"{num1} + {num2} = {suma(num1, num2)}")
            elif escolha == '2':
                print(f"{num1} - {num2} = {subtrair(num1, num2)}")
            elif escolha == '3':
                print(f"{num1} * {num2} = {multiplicar(num1, num2)}")
            elif escolha == '4':
                print(f"{num1} / {num2} = {dividir(num1, num2)}")
        elif escolha == '5':
            num1 = int(input("Digite a base: "))
            num2 = int(input("Digite o expoente: "))
            print(f"{num1} ^ {num2} = {potencia(num1, num2)}")
        elif escolha == '6':
            num = int(input("Digite o número: "))
            print(f"Raiz quadrada de {num} = {raiz_quadrada(num)}")
        else:
            print("Escolha inválida. Tente novamente.")


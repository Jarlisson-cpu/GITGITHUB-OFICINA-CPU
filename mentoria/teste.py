print('ALÔ MUNDO')

# Inicializa uma lista para armazenar os números
numeros = []

print("Digite números (digite 'sair' para terminar):")

while True:
    entrada = input("Digite um número: ")
    
    if entrada.lower() == 'sair':
        break

    try:
        numero = float(entrada)
        numeros.append(numero)
    except ValueError:
        print("Por favor, digite um número válido ou 'sair' para encerrar.")

# Mostra uma mensagem com os números e a soma
if numeros:
    print(f"\nVocê digitou os números: {numeros}")
    print(f"A soma dos números é: {sum(numeros)}")
else:
    print("\nNenhum número foi digitado.")

# Lista para armazenar as 4 notas
notas = []

# Loop para pedir as 4 notas
for i in range(1, 5):
    while True:
        try:
            nota = float(input(f"Digite a {i}ª nota: "))
            if 0 <= nota <= 10:
                notas.append(nota)
                break
            else:
                print("A nota deve estar entre 0 e 10.")
        except ValueError:
            print("Por favor, digite um número válido.")

# Calcula a média
media = sum(notas) / 4

# Mostra a média
print(f"\nAs notas digitadas foram: {notas}")
print(f"A média das notas é: {media:.2f}")

#o produto do dobro
inteiro1 = int(input("Digite o primeiro número inteiro: "))
inteiro2 = int(input("Digite o segundo número inteiro: "))
real = float(input("Digite um número real: "))

real = float(input("Digite um número real: "))

produto = (2 * inteiro1) * (inteiro2 / 2)

print(f"O produto do dobro do primeiro com metade do segundo é: {produto}")

soma = (3 * inteiro1) + real

print(f"A soma do triplo do primeiro com o terceiro é: {soma}")

cubo = real ** 3

print(f"O terceiro número elevado ao cubo é: {cubo}")
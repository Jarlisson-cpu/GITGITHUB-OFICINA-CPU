numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

if numero1 > numero2:
    print("O maior número é:", numero1)
elif numero2 > numero1:
    print("O maior número é:", numero2)
else:
    print("Os dois números são iguais.")

letra = input("Digite o sexo (F/M): ").upper()

if letra == 'F':
    print("Feminino")
elif letra == 'M':
    print("Masculino")
else:
    print("Sexo Inválido")


nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2) / 2

if media >= 7:
    print("Aprovado")
elif media < 5:
    print("Reprovado")
else:
    print("Recuperação")
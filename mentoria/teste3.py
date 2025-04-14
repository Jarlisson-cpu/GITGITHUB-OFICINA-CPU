def pedir_usuario_senha():
    while True:
        usuario = input("Digite o nome de usuário: ")
        senha = input("Digite a senha: ")
        
        if senha == usuario:
            print("Erro: A senha não pode ser igual ao nome de usuário. Tente novamente.")
        else:
            print("Usuário e senha cadastrados com sucesso!")
            break

pedir_usuario_senha()

def calcular_populacao():
    populacao_A = 80000
    populacao_B = 200000
    taxa_crescimento_A = 0,3  # 3% de crescimento
    taxa_crescimento_B = 0,15  # 1,5% de crescimento
    
    anos = 0

    while populacao_A < populacao_B:
        populacao_A += populacao_A * taxa_crescimento_A
        populacao_B += populacao_B * taxa_crescimento_B
        anos += 1

    print(f"A população do país A ultrapassará a do país B em {anos} anos.")

calcular_populacao()


def pedir_nota():
    while True:
        try:
            nota = float(input("Digite uma nota entre 0 e 10: "))
            if 0 <= nota <= 10:
                print("Nota válida:", nota)
                break
            else:
                print("Valor inválido. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Por favor, insira um número.")

pedir_nota()
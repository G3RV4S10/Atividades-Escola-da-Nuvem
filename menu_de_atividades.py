import os

def limpar_tela():
    """Limpa a tela do terminal."""
    os.system('cls' if os.name == 'nt' else 'clear')

while True:
    print("Selecione a Atividade: ")
    print("------------------------")
    print("Atividade 1 (1)")
    print("Atividade 2 (2)")
    print("Atividade 3 (3)")
    print("Sair        (0)")
    print("------------------------")
    
    opcao = input("Selecione a Atividade: ")
    if opcao == "1":
        print("Opção 1 SELECIONADA")
    elif opcao == "2":
        print("Opção 2 SELECIONADA")
    elif opcao == "3":
        print("Opcão 3 SELECIONADA")
    elif opcao == "0":
        print("Sair do programa")
        break
    else:
        print(f"\n'{opcao}' é uma opção Inválida!")

    print("\n") # Apenas para dar espaço
    input("Pressione Enter para voltar ao menu...")
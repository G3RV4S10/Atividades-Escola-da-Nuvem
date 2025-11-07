def calculadora_basica():
    """Calculadora que realiza as quatro operações básicas com tratamento de erros."""
    while True:
        try:
            num1 = float(input("\nDigite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
            operacao = input("Digite a operação (+, -, *, /): ")

            if operacao not in ['+', '-', '*', '/']:
                raise ValueError("Operação inválida. Escolha entre +, -, *, /.")

            if operacao == '+':
                resultado = num1 + num2
            elif operacao == '-':
                resultado = num1 - num2
            elif operacao == '*':
                resultado = num1 * num2
            elif operacao == '/':
                if num2 == 0:
                    raise ZeroDivisionError("Divisão por zero não é permitida.")
                resultado = num1 / num2

            print(f"\nResultado: {num1} {operacao} {num2} = {resultado}")
            break

        except ValueError as ve:
            print(f"Erro: {ve}")
        except ZeroDivisionError as zde:
            print(f"Erro: {zde}")
        except Exception as e:
            print(f"Erro inesperado: {e}")
        print("Tente novamente.\n")


def registrar_notas():
    """Registro de notas com cálculo da média da turma."""
    notas = []
    print("\n=== Registro de Notas ===")
    print("Digite as notas (0 a 10). Digite 'fim' para encerrar.\n")

    while True:
        entrada = input("Informe uma nota: ").strip().lower()
        if entrada == 'fim':
            break
        try:
            nota = float(entrada)
            if 0 <= nota <= 10:
                notas.append(nota)
            else:
                print("Nota inválida. Insira um valor entre 0 e 10.")
        except ValueError:
            print("Entrada inválida. Digite um número ou 'fim'.")

    if notas:
        media = sum(notas) / len(notas)
        print(f"\nMédia da turma: {media:.2f}")
    else:
        print("\nNenhuma nota válida foi registrada.")


def verificar_senha():
    """Verifica se uma senha é forte."""
    print("\n=== Verificador de Senha ===")
    print("A senha deve conter pelo menos 8 caracteres e 1 número.")
    print("Digite 'sair' para encerrar.\n")

    while True:
        senha = input("Digite uma senha: ").strip()
        if senha.lower() == 'sair':
            print("Encerrando verificação de senha.")
            break

        if len(senha) < 8:
            print("Senha muito curta. Deve conter ao menos 8 caracteres.")
            continue

        if not any(char.isdigit() for char in senha):
            print("A senha deve conter pelo menos um número.")
            continue

        print("Senha forte e válida!")
        break


def verificar_pares_impares():
    """Verifica se números inseridos são pares ou ímpares e conta a quantidade."""
    pares = impares = 0
    print("\n=== Verificador de Par ou Ímpar ===")
    print("Digite números inteiros. Digite 'fim' para encerrar.\n")

    while True:
        entrada = input("Digite um número: ").strip().lower()
        if entrada == 'fim':
            break
        try:
            numero = int(entrada)
            if numero % 2 == 0:
                print(f"{numero} é PAR.")
                pares += 1
            else:
                print(f"{numero} é ÍMPAR.")
                impares += 1
        except ValueError:
            print("Entrada inválida. Digite um número inteiro ou 'fim'.")

    print(f"\nQuantidade de pares: {pares}")
    print(f"Quantidade de ímpares: {impares}")


# ====================== MENU PRINCIPAL ======================

while True:
    print("\n===== MENU PRINCIPAL =====")
    print("1 - Calculadora Básica (com tratamento de erros)")
    print("2 - Registro de Notas e Média da Turma")
    print("3 - Verificador de Senha Forte")
    print("4 - Verificador de Números Pares e Ímpares")
    print("0 - Sair")

    opcao = input("\nSelecione uma opção: ")

    if opcao == '0':
        print("\nEncerrando o programa... Até logo!")
        break
    elif opcao == '1':
        calculadora_basica()
    elif opcao == '2':
        registrar_notas()
    elif opcao == '3':
        verificar_senha()
    elif opcao == '4':
        verificar_pares_impares()
    else:
        print("Opcao invalida. Tente novamente!!!")

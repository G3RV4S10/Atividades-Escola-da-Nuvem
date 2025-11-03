while True:
    print("\n===== MENU DE EXERCÍCIOS =====")
    print("1 - Conversor de Moeda")
    print("2 - Calculadora de Desconto")
    print("3 - Calculadora de Média Escolar")
    print("4 - Calculadora de Consumo de Combustível")
    print("5 - Calculadora de Soma com Entrada do Usuário")
    print("6 - Calculadora de Salário por Horas Trabalhadas")
    print("0 - Sair")

    opcao = input("\nSelecione o exercício desejado: ")

    # P ENCERRAR
    if opcao == "0":
        print("Encerrando o programa... Até logo!")
        break

    # EX 1 - CONVERSOR DE MOEDA
    elif opcao == "1":
        valor_reais = 100.00
        taxa_dolar = 5.60
        taxa_euro = 6.60

        valor_dolar = valor_reais / taxa_dolar
        valor_euro = valor_reais / taxa_euro

        print(f"\nConversor de Moeda")
        print(f"Valor em reais: R$ {valor_reais:.2f}")
        print(f"Em dólares: US$ {valor_dolar:.2f}")
        print(f"Em euros: € {valor_euro:.2f}")

    # EX 2 - CALCULADORA DE DESCONTO
    elif opcao == "2":
        nome_produto = "Camiseta"
        preco_original = 50.00
        desconto_percentual = 20

        valor_desconto = preco_original * (desconto_percentual / 100)
        preco_final = preco_original - valor_desconto

        print(f"\nCalculadora de Desconto")
        print(f"Produto: {nome_produto}")
        print(f"Preço original: R$ {preco_original:.2f}")
        print(f"Desconto: {desconto_percentual}%")
        print(f"Valor do desconto: R$ {valor_desconto:.2f}")
        print(f"Preço final: R$ {preco_final:.2f}")

    # EX 3 - CALCULADORA DE MÉDIA ESCOLAR
    elif opcao == "3":
        nota1, nota2, nota3 = 7.5, 8.0, 6.5
        media = (nota1 + nota2 + nota3) / 3

        print(f"\nCalculadora de Média Escolar")
        print(f"Notas: {nota1}, {nota2}, {nota3}")
        print(f"Média final: {media:.2f}")

    # EX 4 - CALCULADORA DE CONSUMO DE COMBUSTÍVEL
    elif opcao == "4":
        distancia = 300  # km
        combustivel = 25  # litros
        consumo_medio = distancia / combustivel

        print(f"\nCalculadora de Consumo de Combustível")
        print(f"Distância percorrida: {distancia} km")
        print(f"Combustível gasto: {combustivel} L")
        print(f"Consumo médio: {consumo_medio:.2f} km/L")

    # EX 5 - CALCULADORA DE SOMA (ENTRADA DO USUÁRIO)
    elif opcao == "5":
        A = int(input("\nDigite o valor de A: "))
        B = int(input("Digite o valor de B: "))
        X = A + B
        print(f"X = {X}")

    # EX 6 - CALCULADORA DE SALÁRIO POR HORAS TRABALHADAS
    elif opcao == "6":
        numero_funcionario = int(input("\nDigite o número do funcionário: "))
        horas_trabalhads = int(input("Digite o número de horas trabalhadas: "))
        valor_p_hora = float(input("Digite o valor recebido por hora: "))

        salario = horas_trabalhads * valor_p_hora
        print(f"\nFuncionário {numero_funcionario}")
        print(f"Salário = R$ {salario:.2f}")

    # OPÇÃO INVÁLIDA
    else:
        print("Opção inválida! Tente novamente.")

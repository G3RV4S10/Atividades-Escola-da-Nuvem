while True:
    print("\n===== MENU DE EXERCÍCIOS =====")
    print("1 - Área da Circunferência")
    print("2 - Classificador de Idade")
    print("3 - Calculadora de IMC")
    print("4 - Conversor de Temperatura")
    print("5 - Verificador de Ano Bissexto")
    print("6 - Calculadora de Comissão")
    print("7 - Calculadora da Média")
    print("0 - Sair")

    opcao = input("\nSelecione o exercício desejado: ")

    # 0 - ENCERRAR
    if opcao == "0":
        print("\nEncerrando o programa... Até logo!")
        break

    # EXERC 1 - ÁREA DA CIRCUNFERÊNCIA
    elif opcao == "1":
        raio = float(input("\nDigite o valor do raio: "))
        pi = 3.14159265
        area = pi * (raio ** 2)
        print(f"A={area:.4f}")

    # EXERC 2 - CLASSIFICADOR DE IDADE
    elif opcao == "2":
        idade = int(input("\nDigite a idade: "))

        if idade < 0:
            print("Idade inválida.")
        elif idade <= 12:
            categoria = "Criança"
        elif idade <= 17:
            categoria = "Adolescente"
        elif idade <= 59:
            categoria = "Adulto"
        else:
            categoria = "Idoso"

        print(f"Classificação: {categoria}")

    # EXERC 3 - CALCULADORA DE IMC
    elif opcao == "3":
        peso = float(input("\nDigite seu peso (kg): "))
        altura = float(input("Digite sua altura (m): "))

        imc = peso / (altura ** 2)

        if imc < 18.5:
            classificacao = "Abaixo do peso"
        elif imc < 25:
            classificacao = "Peso normal"
        elif imc < 30:
            classificacao = "Sobrepeso"
        else:
            classificacao = "Obeso"

        print(f"\nIMC = {imc:.2f}")
        print(f"Classificação: {classificacao}")

    # EXERC 4 - CONVERSOR DE TEMPERATURA
    elif opcao == "4":
        temp = float(input("\nDigite a temperatura: "))
        origem = input("Informe a unidade de origem (C/F/K): ").upper()
        destino = input("Informe a unidade de destino (C/F/K): ").upper()

        resultado = None

        if origem == "C":
            if destino == "F":
                resultado = (temp * 9/5) + 32
            elif destino == "K":
                resultado = temp + 273.15
            else:
                resultado = temp

        elif origem == "F":
            if destino == "C":
                resultado = (temp - 32) * 5/9
            elif destino == "K":
                resultado = (temp - 32) * 5/9 + 273.15
            else:
                resultado = temp

        elif origem == "K":
            if destino == "C":
                resultado = temp - 273.15
            elif destino == "F":
                resultado = (temp - 273.15) * 9/5 + 32
            else:
                resultado = temp

        if resultado is not None:
            print(f"\nResultado: {resultado:.2f}°{destino}")
        else:
            print("Unidade inválida!")

    # EXERC 5 - VERIFICADOR DE ANO BISSEXTO
    elif opcao == "5":
        ano = int(input("\nDigite o ano: "))

        if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
            print(f"{ano} é um ano bissexto.")
        else:
            print(f"{ano} não é um ano bissexto.")

    # EXERC 6 - CALCULADORA DE COMISSÃO
    elif opcao == "6":
        nome = input("\nDigite o nome do vendedor: ")
        salario_fixo = float(input("Digite o salário fixo (R$): "))
        vendas = float(input("Digite o total de vendas (R$): "))

        comissao = vendas * 0.15
        total = salario_fixo + comissao

        print(f"\nVendedor: {nome}")
        print(f"Salário fixo: R$ {salario_fixo:.2f}")
        print(f"Comissão (15%): R$ {comissao:.2f}")
        print(f"Total a receber: R$ {total:.2f}")

    # EXERC 7 - CALCULADORA DA MÉDIA
    elif opcao == "7":
        n1 = float(input("\nDigite N1: "))
        n2 = float(input("Digite N2: "))
        n3 = float(input("Digite N3: "))
        n4 = float(input("Digite N4: "))

        media = (n1 * 2 + n2 * 3 + n3 * 4 + n4 * 1) / 10
        print(f"\nMedia: {media:.1f}")

        if media >= 7.0:
            print("Aluno aprovado.")
        elif media < 5.0:
            print("Aluno reprovado.")
        else:
            print("Aluno em exame.")
            nota_exame = float(input("Nota do exame: "))
            print(f"Nota do exame: {nota_exame:.1f}")

            media_final = (media + nota_exame) / 2

            if media_final >= 5.0:
                print("Aluno aprovado.")
            else:
                print("Aluno reprovado.")

            print(f"Media final: {media_final:.1f}")

    # OPÇÃO INVÁLIDA
    else:
        print("Opção inválida! Tente novamente.")

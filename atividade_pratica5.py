import string
from datetime import datetime

def calcular_gorjeta(valor_conta: float, porcentagem_gorjeta: float) -> float:
    """
    Calcula o valor da gorjeta com base no valor total da conta e na porcentagem desejada.
    
    Parâmetros:
        valor_conta (float): Valor total da conta.
        porcentagem_gorjeta (float): Porcentagem da gorjeta (ex: 15 para 15%).
    
    Retorna:
        float: Valor da gorjeta calculada.
    """
    return valor_conta * (porcentagem_gorjeta / 100)


def verificar_palindromo(texto: str) -> str:
    """
    Verifica se uma palavra ou frase é um palíndromo, ignorando espaços, acentos e pontuação.
    
    Parâmetro:
        texto (str): Palavra ou frase a ser verificada.
    
    Retorna:
        str: "Sim" se for palíndromo, "Não" caso contrário.
    """
    texto_limpo = ''.join(
        c.lower() for c in texto if c.isalnum()
    ) 
    return "Sim" if texto_limpo == texto_limpo[::-1] else "Não"


def calcular_preco_final():
    """
    Calcul o preco final de um produto após aplicar um percentual de desconto.
    Solicita ao usuário o preço original e a porcentagem de desconto.
    """
    try:
        preco = float(input("\nDigite o preço original do produto: R$ "))
        desconto = float(input("Digite o percentual de desconto (%): "))

        valor_desconto = preco * (desconto / 100)
        preco_final = preco - valor_desconto

        print(f"\nValor do desconto: R$ {valor_desconto:.2f}")
        print(f"Preço final: R$ {preco_final:.2f}")
    except ValueError:
        print("Etrada inválida! Digite apenas números.")


def calcular_idade_em_dias(ano_nascimento: int) -> int:
    """
    Calcula a idade aproximada em dias, considerando o year atual.
    
    Parmetro:
        ano_nascimento (int): Ano de nascimento da pessoa.
    
    Retorna:
        int: Idade estimada em dias.
    """
    ano_atual = datetime.now().year
    idade_anos = ano_atual - ano_nascimento
    return idade_anos * 365


# ================== MENU PRINCIPAL ==================

while True:
    print("\n===== MENU DE FUNÇÕES =====")
    print("1 - Calcular Gorjeta")
    print("2 - Verificar Palíndromo")
    print("3 - Calcular Preço com Desconto")
    print("4 - Calcular Idade em Dias")
    print("0 - Sair")

    opcao = input("\nSelecione uma opção: ")

    if opcao == "0":
        print("\nEncerrando o programa... Até logo!")
        break

    elif opcao == "1":
        try:
            conta = float(input("\nDigite o valor total da conta: R$ "))
            porcentagem = float(input("Digite a porcentagem de gorjeta (%): "))
            gorjeta = calcular_gorjeta(conta, porcentagem)
            print(f"\nValor da gorjeta: R$ {gorjeta:.2f}")
        except ValueError:
            print("Entrada inválida. Digite valores numéricos.")

    elif opcao == "2":
        frase = input("\nDigite uma palavra ou frase: ")
        resultado = verificar_palindromo(frase)
        print(f"É palíndromo? {resultado}")

    elif opcao == "3":
        calcular_preco_final()

    elif opcao == "4":
        try:
            ano = int(input("\nDigite seu ano de nascimento: "))
            dias = calcular_idade_em_dias(ano)
            print(f"\nIdade aproximada: {dias} dias")
        except ValueError:
            print("Ano inválido. Digite um valor inteiro (ex: 2001).")

    else:
        print("Opção inválida! Tente novamente.")

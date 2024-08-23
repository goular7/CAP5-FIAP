# Função para calcular o desconto baseado na categoria e quantidade de viajantes
def calcular_desconto(valor_bruto, categoria, qtd_viajantes):
    """
    Calcula o valor do desconto com base na categoria dos assentos e
    na quantidade de viajantes no mesmo grupo.

    Parâmetros:
    valor_bruto (float): Valor total do pacote de viagem antes do desconto.
    categoria (str): Categoria dos assentos (Economica, Executiva, Primeira classe).
    qtd_viajantes (int): Número de viajantes no mesmo grupo e que moram na mesma residência.

    Retorno:
    float: O valor do desconto a ser aplicado.
    """

    # Definindo os percentuais de desconto conforme a categoria e número de viajantes
    descontos = {
        "Economica": {2: 0.03, 3: 0.04, 4: 0.05},  # Descontos para a categoria Econômica
        "Executiva": {2: 0.05, 3: 0.07, 4: 0.08},  # Descontos para a categoria Executiva
        "Primeira classe": {2: 0.10, 3: 0.15, 4: 0.20}  # Descontos para a categoria Primeira Classe
    }

    # Inicializando o desconto a 0 para o caso de haver apenas 1 viajante (sem desconto)
    desconto = 0

    # Verifica o número de viajantes e aplica o desconto correspondente
    if qtd_viajantes >= 4:
        desconto = descontos[categoria][4]  # Desconto para 4 ou mais viajantes
    elif qtd_viajantes == 3:
        desconto = descontos[categoria][3]  # Desconto para 3 viajantes
    elif qtd_viajantes == 2:
        desconto = descontos[categoria][2]  # Desconto para 2 viajantes

    # Calcula o valor absoluto do desconto
    valor_desconto = valor_bruto * desconto
    return valor_desconto


# Entrada de dados fornecida pelo usuário
valor_bruto = float(input("Digite o valor bruto da viagem: R$ "))
categoria = input("Digite a categoria dos assentos (Economica, Executiva, Primeira classe): ").strip()
qtd_viajantes = int(input("Digite a quantidade de viajantes: "))

# Garantindo que a categoria foi digitada corretamente
categoria = categoria.capitalize()  # Capitaliza a primeira letra da categoria para uniformizar

# Verificação adicional para garantir que a categoria inserida é válida
if categoria not in ["Economica", "Executiva", "Primeira classe"]:
    print("Categoria inválida! Por favor, insira 'Economica', 'Executiva', ou 'Primeira classe'.")
else:
    # Cálculo do desconto usando a função previamente definida
    valor_desconto = calcular_desconto(valor_bruto, categoria, qtd_viajantes)

    # Cálculo do valor líquido após o desconto ser aplicado
    valor_liquido = valor_bruto - valor_desconto

    # Cálculo do valor médio por viajante
    valor_medio_por_viajante = valor_liquido / qtd_viajantes

    # Exibição dos resultados com formatação de duas casas decimais
    print(f"\nValor bruto da viagem: R$ {valor_bruto:.2f}")
    print(f"Valor do desconto: R$ {valor_desconto:.2f}")
    print(f"Valor líquido da viagem: R$ {valor_liquido:.2f}")
    print(f"Valor médio por viajante: R$ {valor_medio_por_viajante:.2f}")




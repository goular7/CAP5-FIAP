# Função para calcular o desconto baseado na categoria e quantidade de viajantes
def calcular_desconto(valor_bruto, categoria, qtd_viajantes):
    # Definindo os descontos de acordo com a tabela
    descontos = {
        "Economica": {2: 0.03, 3: 0.04, 4: 0.05},
        "Executiva": {2: 0.05, 3: 0.07, 4: 0.08},
        "Primeira classe": {2: 0.10, 3: 0.15, 4: 0.20}
    }

    # Encontrando o desconto adequado
    desconto = 0
    if qtd_viajantes >= 4:
        desconto = descontos[categoria][4]
    elif qtd_viajantes >= 3:
        desconto = descontos[categoria][3]
    elif qtd_viajantes >= 2:
        desconto = descontos[categoria][2]

    # Calculando o valor do desconto
    valor_desconto = valor_bruto * desconto
    return valor_desconto

# Entrada de dados
valor_bruto = float(input("Digite o valor bruto da viagem: R$ "))
categoria = input("Digite a categoria dos assentos (Economica, Executiva, Primeira classe): ").strip()
qtd_viajantes = int(input("Digite a quantidade de viajantes: "))

# Garantindo que a categoria foi digitada corretamente
categoria = categoria.capitalize()

# Calculando o desconto
valor_desconto = calcular_desconto(valor_bruto, categoria, qtd_viajantes)

# Calculando o valor líquido
valor_liquido = valor_bruto - valor_desconto

# Calculando o valor médio por viajante
valor_medio_por_viajante = valor_liquido / qtd_viajantes

# Exibindo os resultados
print(f"\nValor bruto da viagem: R$ {valor_bruto:.2f}")
print(f"Valor do desconto: R$ {valor_desconto:.2f}")
print(f"Valor líquido da viagem: R$ {valor_liquido:.2f}")
print(f"Valor médio por viajante: R$ {valor_medio_por_viajante:.2f}")


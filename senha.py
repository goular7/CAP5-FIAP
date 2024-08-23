def fatorial(minutos):
    fatorial = 1
    for i in range(1, minutos + 1):
        fatorial *= i
    return fatorial

def senha(minutos):
    palavra = "LIBERDADE"
    fatorial_min = fatorial(minutos)
    senha = f"{palavra}{fatorial_min}"
    return senha

minutos = int(input("Digite os minutos atuais: "))

senha_desbloqueio = senha(minutos)
print(f"Senha: {senha_desbloqueio}")

idade = int(input("Quantos anos você tem? "))
colaboracao = int(input("A quanto tempo você contribui para o Instituto de Seguridade Social? "))

if idade >= 60 and colaboracao >= 15:
    print("Parabéns, você pode se aposentar")
else:
    print("Você não pode se aposentar!")
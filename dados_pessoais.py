nome = input("Qual é o seu nome? ")
idade = int(input("Quantos anos você tem? "))
cidade = input("Qual sua cidade? ")
linguagem = input("Qual sua linguagem de programação favorita? ")

ano_atual = 2026
ano_nascimento = ano_atual - idade

ano_2030 = idade + 4

print(f"\nOlá, {nome}!")
print(f"Você nasceu aproximadamente em {ano_nascimento}.")
print(f"sua liguagem de programação favorita é {linguagem}.")
print(f"você mora na cidade {cidade}.")
print(f"Você terá {ano_2030} em 2030.")
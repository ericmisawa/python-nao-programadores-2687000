data_nascimento = '05-10-1976'
idade_numerica = 46
altura = 1.74

# Descubra o tipo de dado de cada variável acima

print("O tipo da variável 'data_nascimento' é", type(data_nascimento))
print("O tipo da variável 'idade_numerica' é", (type(idade_numerica)))
print("O tipo da variável 'altura' é", type(altura))

# Realize uma operação entre dados do tipo string e inteiro

palavra = "string"
print(palavra*4)

# Realize uma operação entre dados do tipo inteiro e float

preco1 = 1.75
preco2 = 2.5
soma = preco1 + preco2

print(f"A soma de {preco1} com {preco2} é igual a {soma}")

print(f"Arredondando esse valor pra cima, teríamos {round(soma,0)} ou {int(round(soma,0))}.")

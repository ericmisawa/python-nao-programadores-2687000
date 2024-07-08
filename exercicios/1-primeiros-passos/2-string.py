resumo = "Paloma é uma mulher de 46 anos que deseja mudar de profissão, por isso está estudando 'python'."

# Imprima na tela a variável "resumo"

print(resumo)

# Imprima na tela apenas a segunda letra da variável

print("A 2ª letra é", resumo[1])

# Imprima na tela a idade de Paloma (resposta esperada: "46")

print("A idade de Paloma é", resumo[23:25])

# Imprima na tela o trecho final da variável

print("O trecho final é", resumo[31:])

# Converta todos as letras para minúsculo e imprima na tela

print("Com todas as letras minúsculas ficaria assim:", resumo.lower())

# Converta todas as letras para maiúscula e imprima na tela

print("Com todas as letras maiúsculas ficaria assim:", resumo.upper())

# Formate a frase para que a primeira letra de cada palavra seja maiúscula e imprima na tela

print("Com a primeira letra de cada palavra maíuscula ficaria assim:", resumo.title())

# Formate a frase para que apenas a primeira letra da frase seja maiúscula e imprima na tela

print("Com a primeira letra da frase em maiúscula:", resumo.capitalize())

# Imprima na tela uma string utilizando uma variável, usando o recurso string format
idade = 46
linguagem = "'python'"
print(f"Paloma é uma mulher de {idade} que deseja mudar de profissão, por isso está estudando {linguagem}.")

idade = 47
linguagem = "'java'"
print(f"Paloma é uma mulher de {idade} que deseja mudar de profissão, por isso está estudando {linguagem}.")

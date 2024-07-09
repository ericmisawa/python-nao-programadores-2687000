ano_nascimento = 1989
ano_formatura = 2010

# Considerando que as variáveis acima correspondem a 'Gerlaine', descubra a idade dela no ano da sua formatura

idade_formatura = ano_formatura - ano_nascimento

print(f"Gerlaine tinha {idade_formatura} anos quando se formou.")

# Escreva expressões comparativas usando os operadores relacionais >, <= e ==. Imprima na tela as respostas

maior_que = ano_nascimento > ano_formatura
menor_igual = ano_nascimento <= ano_formatura
igual = ano_nascimento == ano_formatura

print(f'''O ano de nascimento é maior que o ano de formatura? {maior_que}
O ano de nascimento é menor ou igual ao ano de formatura? {menor_igual}
O ano de nascimento é igual ao ano de formatura? {igual}
''')

# Crie expressões comparativas mais complexas utilizando operadores lógicos and, or e not. Imprima na tela as respostas

exp_and = 4 == 4 and 3 == 3
exp_or = 5 >= 4 or 4 == 5
exp_not = not 5 != 5

print(f"And fica {exp_and}, pois 4 = 4 e 3 = 3, Or fica {exp_or}, pois 5 >= 4 (mesmo 4 não sendo igual a 5) e Not fica {exp_not}, pois 5 não é diferente de 5.")
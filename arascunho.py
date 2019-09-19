nome = input("Nome: ")
sobrenome = input("Sobrenome: ")
idade = input("Idade: ")
matricula = input("Matricula: ")

#condicionais_idade
if idade > 41:
    print("Maior de 40 anos")

elif idade > 31:
    print("Maior de 30 anos")

elif idade > 21:
    print("Maior de 20 anos")

#condicionais_nome
if len(nome) > 6:
    # troca as letras "A" por nenhuma
    print(f'Nome com mais de 6 letras: {nome.lower().replace("a","")}')

else:
    # troca de duas em duas pra ..
    print(f'Nome com 6 caracteres ou menos: {nome[::2]}{nome[-1]}')

#condicionais_sobrenome
if 'r' in sobrenome.lower():
    print(f'Sobrenome 1,3,5: {sobrenome[::2]}')

else:
    print(f'Sobrenome 2,4,6: {sobrenome[1::2]}')

print(matricula.replace('1','').replace('3','').replace('5',''))

# ''' nova matricula =  '''
for numero in matricula:
    if int(numero) % 2 == 0:
        nova_matricula = nova_matricula + numero

print(f'Matricula: {nova_matricula}')

print(f'Matricula: ["".join(str(x) for x in [par for par in matricula if int(par) %2 == 0])]')

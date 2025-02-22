#Crie uma tupla contendo os nomes de cinco países e exiba toda a tupla. 
#Peça ao usuário para inserir um dos países que foram mostrados a ele e, em seguida, exibir o número de índice (ou seja, posição na lista) desse item na tupla.
paises = ('Brasil','Argentina','Uruguai','Colombia','Chile')
print(paises)
pais = input('Digite um dos paises acima: ')
if pais in paises:
    for i in range(len(paises)):
        if paises[i] == pais:
            print(i)
else:
    print('{} não está na lista.'.format(pais))

print('Matheus Eduardo Souza')
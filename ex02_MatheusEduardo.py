#Faça um programa que o usuario insira 10 produtos numa tupla. Exiba todos os produtos,
#  solicite ao usuário para digitar um nome de produto e exiba a posição dele, em seguida peça para digitar numero entre 0 e 9 e exiba o produto da tupla.
produtos = ()
adicionar_produtos = list(produtos)
for i in range(10):
    produto = input('Insira o {}° produto: '.format(i+1))
    adicionar_produtos.append(produto)
    produtos = tuple(adicionar_produtos)
print(produtos)
nomep = input('Digite o nome de um produto: ')
if nomep in produtos:
    for i in range(len(produtos)):
        if produtos[i] == nomep:
            print('A posição do produto é:', i)
else:
        print('{} não está na lista'.format(nomep))
num = int(input('Digite um número entre 0 e 9: '))
print('O produto dessa posição é: {}'.format(produtos[num]))

print('Matheus Eduardo Souza')



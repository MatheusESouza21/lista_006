"""
Peça ao usuário para inserir os nomes de três pessoas que deseja convidar para uma festa e armazená-las em uma lista. Depois de inserir os três nomes, 
pergunte se deseja adicionar outro. Se o fizer, permita que adicione mais nomes até responder "não". Quando ele responder "não", mostre quantas pessoas ele convidou para a festa,
uma vez que o usuário tenha completado sua lista de nomes, exiba a lista completa e peça que ele digite um dos nomes da lista. Exiba a posição desse nome na lista. 
Pergunte ao usuário se ele ainda deseja que essa pessoa venha à festa. Se ele responder "não", exclua essa entrada da lista e exiba a lista novamente.
"""
nomes = []
adicionar_nomes = list(nomes)

for i in range(3):
    nome = input('Insira o {}° nome: '.format(i+1))
    adicionar_nomes.append(nome)
    nomes = (adicionar_nomes)

confirmacao = input('Deseja adicionar mais um nome? (S ou N) ').upper()

if confirmacao == 'S':
    while confirmacao == 'S':
        nome = input('Insira o nome: ')
        adicionar_nomes.append(nome)
        nomes = (adicionar_nomes)
        confirmacao = input('Deseja adicionar mais um nome? (S ou N): ').upper()

print('Você convidou {} pessoas para a festa'.format(len(nomes)))

print(nomes)
escolhido = input('Digite um dos nomes da lista: ')
if escolhido in nomes:
    for i in range(len(nomes)):
        if nomes[i] == escolhido:

            print('A posição de {} é {}'.format(nomes[i],i))

else:
    print('Esse nome não está na lista.')

confirmacao = input('Você ainda deseja que {} venha a festa? (sim/nao): '.format(escolhido)).lower()
if confirmacao == 'nao':
    nomes.remove(escolhido)

print(nomes)

print('Matheus Eduardo Souza')


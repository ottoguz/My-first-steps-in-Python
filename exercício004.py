#EXERCÍCIO 4: LISTA DE CONTATOS DE TELEFONE EM ORDEM ALFABÉTICA + DICIONARIO DE MAIORES E MENORES DE IDADE

#Função para ordenar a lista de contatos em ordem alfabetica
#printa o nome, idade e o telefone de forma legível ao usuário
def ordena_printa(dado):
    dado = sorted(dado, key=lambda nome: nome[0])
    for i in range(len(dado)):
        print(dado[i][0], dado[i][1], dado[i][2])

#Função para printar os dicionários de maiores e menores de forma legível ao usuário
def printa_dicionario(dicionario):
    for i in range(len(dicionario['nome'])):
        print(dicionario['nome'][i], dicionario['idade'][i], dicionario['telefone'][i])

#Lista para armazenar nome, idade e telefone dos contatos
lista = []

#Dicionários de menores e maiores
menores = {'nome': [], 'idade': [], 'telefone': []}

maiores = {'nome': [], 'idade': [], 'telefone': []}

#Início do ciclo de repetição para a entrada dos dados (nome, idade, telefone)
#O ciclo é interrompido ao printar uma string vazia na vairiavel "v_nome"
while True:
    v_nome = input('Nome:')
    if not v_nome:
        break
    else:
        v_idade = int(input('Idade:'))
        v_telefone = int(input('Telefone'))

        #Armazenamento dos dados nome, idade e telefone nos dicionários menores e maiores
        lista.append([v_nome.title(), v_idade, v_telefone])
        if v_idade < 18:
            menores['nome'].append(v_nome)
            menores['idade'].append(v_idade)
            menores['telefone'].append(v_telefone)


        elif v_idade >= 18:
            maiores['nome'].append(v_nome)
            maiores['idade'].append(v_idade)
            maiores['telefone'].append(v_telefone)

#prints 1) Lista ordenada em ordem alfabetica 2)Dicionário de menores 3) Dicionário de maiores
print('1)Lista ordenada')
ordena_printa(lista)
print()
print('2)dicionário menores')
printa_dicionario(menores)
print()
print('3)dicionário maiores')
printa_dicionario(maiores)




























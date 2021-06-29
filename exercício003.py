#EXERCÍCIO 3: PROGRAMA PARA LER OS DADOS DE N ALUNOS E SE FFORAM APROVADOS OU NÃO

#Biblioteca com listas contendo como chaves o nome, notas 1, 2, 3 e 4 e por fim o status aprovado/reprovado
alunos = {'nome': [], 'nota1': [], 'nota2': [], 'nota3': [], 'nota4': [], 'status': []}


#Cabeçalho
print('CADASTRO DE NOTAS DOS ALUNOS')

#Ciclo de repetição com as entradas de nome e notas individualmente
while True:
    nome = input('Digite o nome do aluno:')
    n1 = float(input('1a Nota:'))
    n2 = float(input('2a Nota:'))
    n3 = float(input('3a Nota:'))
    n4 = float(input('4a Nota:'))

#Condição de aprovação: média 7 do somatório das 4 notas
    if (n1 + n2 + n3 + n4) / 4 >= 7:
        status = 'Aprovado!'
    else:
        status = 'Reprovado!'

#Armazenamento dos dados na biblioteca
    alunos['nome'].append(nome)
    alunos['nota1'].append(n1)
    alunos['nota2'].append(n2)
    alunos['nota3'].append(n3)
    alunos['nota4'].append(n4)
    alunos['status'].append(status)

#Caso tecle "s" você poderá cadastrar outro aluno dentro do número limite estipulado previamente no início do programa
#Caso tecle "n", o programa é encerrado e uma tabela contendo o nome, notas 1, 2, 3, 4 e o status é gerada
    cadastro = input('Gostaria de cadastrar outro aluno? (S/N)')
    if cadastro.upper() in 'N':
        print('Notas dos alunos:')
        print('_________________')
        for i in range(len(alunos['nome'])):
            print('|{}|' .format(alunos['nome'][i]), end=' ')
            print('|{:.1f}| |{:.1f}|' .format((alunos['nota1'][i]), (alunos['nota2'][i])), end=' ')
            print('|{:.1f}| |{:.1f}|:'.format((alunos['nota3'][i]), (alunos['nota4'][i])), end=' ')
            print(alunos['status'][i])
        break

    #Ciclo de repetição para obrigar o susuario a digitar "s" ou "n"
    while cadastro.upper() != 'S':
        print('Digite "S" para SIM ou "N" para NÃO')
        cadastro = input('Gostaria de cadastrar outro aluno? (S/N)')





















































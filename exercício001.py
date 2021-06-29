#EXERCÍCIO 1: ESCREVA UM PROGRAMA QUE LEIA O NOME E O PESO DE UM LUTADOR:

#Cabeçalho para ficar legível para o usuário
menu = 'WRESTLING WORLD TOURNAMENT'
print('{:*^34}' .format(menu))
print('ENTRE COM O NOME E O PESO DO LUTADOR')

#Ciclo de repetição que se inicia verificando se o usuário entrou com um nome válido e o peso mínimo requerido
while True:
    nome_lutador = input('Digite o nome do lutador:')
    while not nome_lutador:
        print('Campo "Nome do lutador" vazio! Digite um nome válido')
        nome_lutador = input('Digite o nome do lutador:')

    peso_kg = float(input('Digite o peso do lutador (Kg):'))
    while peso_kg < 40:
        print('Peso abaixo do mínimo requerido para o evento')
        nome_lutador = input('Digite o nome do lutador:')
        while not nome_lutador:
            print('Campo "Nome do lutador" vazio! Digite um nome válido')
            nome_lutador = input('Digite o nome do lutador:')
        peso_kg = float(input('Digite o peso do lutador (Kg)'))
        while peso_kg < 40:
            print('Peso abaixo do mínimo requerido para o evento')
        continue

    #Caso os requesitos de nome e peso sejam atingidos,
    # uma sequencia de elifs se inicia para enquadrar o lutador na devida categoria
    if (peso_kg < 65):
        categoria = 'Peso Pena'
        print('O nome fornecido foi: {}' .format(nome_lutador))
        print('Peso fornecido: {}' .format(peso_kg))
        print('O lutador {} pesa {}Kg e se enquadra na categoria {}'.format(nome_lutador, peso_kg, categoria))

    elif ((peso_kg >= 65) and (peso_kg < 72)):
        categoria = 'Peso Leve'
        print('O nome fornecido foi: {}'.format(nome_lutador))
        print('Peso fornecido: {}'.format(peso_kg))
        print('O lutador {} pesa {}Kg e se enquadra na categoria {}'.format(nome_lutador, peso_kg, categoria))

    elif ((peso_kg >= 72) and (peso_kg < 79)):
        categoria = 'Peso Ligeiro'
        print('O nome fornecido foi: {}'.format(nome_lutador))
        print('Peso fornecido: {}'.format(peso_kg))
        print('O lutador {} pesa {}Kg e se enquadra na categoria {}'.format(nome_lutador, peso_kg, categoria))

    elif ((peso_kg >= 79) and (peso_kg < 86)):
        categoria = 'Peso Meio-Médio'
        print('O nome fornecido foi: {}'.format(nome_lutador))
        print('Peso fornecido: {}'.format(peso_kg))
        print('O lutador {} pesa {}Kg e se enquadra na categoria {}'.format(nome_lutador, peso_kg, categoria))

    elif ((peso_kg >= 86) and (peso_kg < 93)):
        categoria = 'Peso Médio'
        print('O nome fornecido foi: {}'.format(nome_lutador))
        print('Peso fornecido: {}'.format(peso_kg))
        print('O lutador {} pesa {}Kg e se enquadra na categoria {}'.format(nome_lutador, peso_kg, categoria))

    elif ((peso_kg >= 93) and (peso_kg < 100)):
        categoria = 'Peso Meio-Pesado'
        print('O nome fornecido foi: {}'.format(nome_lutador))
        print('Peso fornecido: {}'.format(peso_kg))
        print('O lutador {} pesa {}Kg e se enquadra na categoria {}'.format(nome_lutador, peso_kg, categoria))

    elif (peso_kg >= 100):
        categoria = 'Peso Pesado'
        print('O nome fornecido foi: {}'.format(nome_lutador))
        print('Peso fornecido: {}'.format(peso_kg))
        print('O lutador {} pesa {}Kg e se enquadra na categoria {}'.format(nome_lutador, peso_kg, categoria))

    #Depois do print do lutador, seu peso e sua categoria,
    #você decide se encerra o programa apertando "s",
    # caso contrário, pressione  "n" para reiniciar o ciclo após a mensagem "Reiniciando..."
    encerrar = input('Gostaria de encerrar o programa? (s/n):')
    if encerrar == 's' or encerrar =='S':
        print('Encerrando o programa...')
        break
    else:
        print('Reiniciando...')
























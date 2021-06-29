#EXERCÍCIO 2: ESCREVA UM PROGRAMA QUE RECEBA DE ENTRADA UM NÚMERO INTEIRO DE 5 DÍGITOS NO INTERVALO [10000, 30000]
#(CÓDIGOS DE PRODUTOS VENDIDOS EM UMA LOJA)

#Função para validar o número do código no parâmetro entre 10000 e 30000
def valida_num_intervalo():
    while True:
        try:
            parametro = int(input('Digite o código do produto:'))
            if (parametro > 10000) and (parametro < 30000):
                print(parametro, end='-')
                return parametro
            else:
                print('Código inválido! Digite um valor entre 10000 e 30000.')
                continue
        except ValueError:
            print('Ooops, algo deu errado!')

#Função para manipular o código e retornar o dígito final
def digito():
    inter_str = str(valida_num_intervalo())
    lista_dig = [inter_str[0], inter_str[1], inter_str[2], inter_str[3], inter_str[4]]
    lista_dig2 = int(inter_str[0]) * 2
    lista_dig3 = int(inter_str[1]) * 3
    lista_dig4 = int(inter_str[2]) * 4
    lista_dig5 = int(inter_str[3]) * 5
    lista_dig6 = int(inter_str[4]) * 6
    lista_dig_final = (lista_dig2 + lista_dig3 + lista_dig4 + lista_dig5 + lista_dig6) % 7
    return lista_dig_final

#programa principal onde se obtém o código do produto e o dígito separado por hifen via teclado
#Na primeira parte do teste usarei os primeiros 5 dígitos meu RU, que está fora do parâmetro estabelecido
#Na segunda parte do teste usarei um código de produto dentro do parâmetro para demonstrar o devido funcionamento
print('{} é o código do produto com o digito de validação.'.format(digito()))



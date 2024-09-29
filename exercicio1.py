print('Bem-vindos a loja da Eduarda da Silva Marcelino')

valorDopedido = float(input('Entre com o valor do pedido: '))
quantidadeParcelas = float(input('Entre com a quantidade de parcelas: '))
#inicializando variável valorParcela com zero
valordaParcela = 0

if ( quantidadeParcelas < 4 ):
    valordaParcela = valorDopedido / quantidadeParcelas

elif ( quantidadeParcelas >= 4 and quantidadeParcelas < 6 ):
    valordaParcela = (valorDopedido * ( 1 + ( 4/100 ) ) ) / quantidadeParcelas
    
elif ( quantidadeParcelas >= 6 and quantidadeParcelas < 9 ):
    valordaParcela = (valorDopedido * ( 1 + ( 8/100 ) ) ) / quantidadeParcelas
    
elif ( quantidadeParcelas >= 9 and quantidadeParcelas < 13 ):
    valordaParcela = (valorDopedido * ( 1 + ( 16/100 ) ) ) / quantidadeParcelas

#caso o valor seja maior ou igual a 13 entrar nesse else
else: 
    valordaParcela = (valorDopedido * ( 1 + ( 32/100 ) ) ) / quantidadeParcelas
    
    
#imprimindo o valor da parcela com arredondamento
print(f' O valor das parcelas é de: R$ {round(valordaParcela, 2)}')
print(f' O valor Total Parcelado é de: R$ { round(valordaParcela * quantidadeParcelas, 2) }')

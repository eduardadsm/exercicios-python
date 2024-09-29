print('Bem vindo a Fábrica de Camisetas da Eduarda da Silva Marcelino')


#total = (modelo * num_camisetas) + frete

#Funcao para retornar um valor de acordo com modelo - funcao escolha_modelo() do enunciado
def definirValorPorModelo(modelo):
    if (modelo == "MCS"):
        return  (1.80)
    elif (modelo == "MLS"):
        return  (2.10)
    elif (modelo == "MCE"):
        return  (2.90)
    elif (modelo == "MLE"):
        return  (3.20)
    else:
        print('Escolha inválida, entre com o modelo novamente.')
        return -1
    
#funcao para calcular o valor com desconto de acordo com o numero de camisetas - funcao num_camisetas() do enunciado
def calcularQuantidadeDeCamisasComDesconto(numeroDeCamisetas):
        if (numeroDeCamisetas < 20):
            return  numeroDeCamisetas 
        elif (numeroDeCamisetas >= 20 and numeroCamisetas < 200):
            numeroDeCamisetas -= ( (5/100) * numeroCamisetas )
            return  numeroDeCamisetas
        elif (numeroDeCamisetas >= 200 and numeroCamisetas < 2000):
            numeroDeCamisetas -= ( (7/100) * numeroCamisetas )
            return  numeroDeCamisetas
        elif (numeroDeCamisetas >= 2000 and numeroCamisetas <= 20000):
            numeroDeCamisetas -= ( (12/100) * numeroCamisetas )
            return  numeroDeCamisetas
        elif (numeroDeCamisetas > 20000):
            print('Ultraspassou a quantidade limite de camisetas.')
            return -1

#funcao para calcular o valor do frete - funcao frete() do enunciado
def calcularValorDoFrete(opcaoFrete):
    if(opcaoFrete == 1):
        return 100
    elif(opcaoFrete == 2):
        return 200
    elif(opcaoFrete == 0):
        return 0
    else:
        print('Escolha inválida, entre com o modelo novamente.')
        return -1
    

#programa principal - comeca aqui

while True:
    print('Entre com o modelo desejado')
    print('MCS - Manga Curta Simples')
    print('MLS - Manga Longa Simples')
    print('MCE - Manga Com Estampa')
    print('MLE- Manga Com Estampa')
    modeloDigitadoPeloUsuario = str(input('>>   '))
    valorPorModelo = definirValorPorModelo(modeloDigitadoPeloUsuario)
    if(valorPorModelo == 1.80 or valorPorModelo == 2.10 or valorPorModelo == 2.90 or valorPorModelo == 3.20):
       break


while True:
    try:
        numeroCamisetas = int(input('Qual numero de camisetas voce deseja ?  '))
        valorSemFrete = calcularQuantidadeDeCamisasComDesconto(numeroCamisetas)
        if(valorSemFrete != -1):
            break
    except:
        print("Voce digitou um valor nao numero, digite um numero valor")


while True:
    opcaoFrete = int(input('Digite a opcao de frete ?  '))
    print("1 - Freete por transportadora - R$ 100.00")
    print("2 - Frete por Sedex - R$ 200.00")
    print("3 - Retirar pedido na fábrica - R$ 0.00")
    valorDoFrete = calcularValorDoFrete(opcaoFrete)
    if(valorDoFrete != -1):
        break

valorTotalDoPedido = valorDoFrete + (valorSemFrete * valorPorModelo)

print(f"Total: R$ {valorTotalDoPedido} (Modelo: {valorPorModelo} * Quantidade(com desconto): {valorSemFrete} + frete: {valorDoFrete}) ")
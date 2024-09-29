print(" ----- Bem vindos a loja de Marmitas da Eduarda da Silva Marcelino -------")
print(" -----------------------------CARDAPIO -----------------------------------")
print("---| TAMANHO | Bife Acebolado (BA) | Filé de Frango (FF) |---")
print("---|    P    |      R$ 16.00       |      R$ 15.00       |---")
print("---|    M    |      R$ 18.00       |      R$ 17.00       |---")
print("---|    G    |      R$ 22.00       |      R$ 21.00       |---")
print("-------------------------------------------------------------")

#inicializando o valor total (acumulador)
valorTotal= 0                      

while True:
    sabor = str(input("\nEntre com o sabor desejado (BA/FF):  "))
    #confere se digitou os sabores validos
    if(sabor == "BA" or  sabor == "FF"):
 
        tam = str(input("Entre com o tamanho desejado (P/M/G):  "))

        #confere se digitou o tamanho valido e os valores das marmitas
        if(tam == "P" or tam == "M" or tam == "G" ): 
            if sabor == "BA" and tam == "P":
                valorTotal = valorTotal + int(16)
                print("Você pediu um Bife Acebolado no tamanho P: R$ 16.00")

            elif sabor == "BA" and tam == "M":
                valorTotal = valorTotal + int(18)
                print("Você pediu um Bife Acebolado no tamanho M: R$ 18.00")

            elif sabor == "BA" and tam == "G":
                valorTotal = valorTotal + int(22)
                print("Você pediu um Bife Acebolado no tamanho G: R$ 22.00")

            elif sabor == "FF" and tam == "P":
                valorTotal = valorTotal + int(15)
                print("Você pediu um Filé de Frango no tamanho P: R$ 15.00")

            elif sabor == "FF" and tam == "M":
                valorTotal= valorTotal + int(17)
                print("Você pediu um Filé de Frango no tamanho M: R$ 17.00")

            elif sabor == "FF" and tam == "G":
                 valorTotal = valorTotal + int(21)
                 print("Você pediu um Filé de Frango no tamanho G: R$ 21.00")

            #implementação do continue se o usuário quiser adicionar mais pedidos
            continuar = str(input("\n Deseja mais alguma coisa? (S/N)  "))
            if continuar == "S":
                continue
            else: 
                break
        # caso o tamanho seja invalido cai aqui 
        else:
            print("Tamanho inválido. Tente novamente ")
    else:
        #se o o sabor digitado for invalido, cai aqui
        print("Sabor inválido. Tente novamente ")
        
     #valor total de um ou mais pedidos
print(f"\nO valor total a ser pago é: R$ {valorTotal}.00 ")
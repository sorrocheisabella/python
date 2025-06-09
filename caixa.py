# saldo inicial 
saldo =1000
#principal do progrma 
while True :
 print ("\n ==== caixa eletrônico====")
 print ("1.ver saldo")
 print ("2.sacar dinheiro")
 print ("3.encerrar")
 #solicita a opção do usuário
 opcao =input ("escolha uma opção(1-3):")
 #ver saldo 
 if opcao =="1":
    print (f"R$ seu saldo atual é:R$ {saldo:.2f}")
    #sacar dinherio
 elif opcao == "2":
    valor_saque = float(input("digite o valor para saque:"))
if valor_saque <+saldo:
    saldo-= valor_saque
    print (f"saque de R$ {valor_saque:.2f}realizaso com sucesso!")    
else:
    print (" saldo insuficiente para esse saque.")
#saldo ecerrar
if opcao == "3":
    print ("ecerrando o programa.obrigado por usar o caixa eletronico")
else:
   print("opçao invalida,por favor, escolha1,2 ou 3.")
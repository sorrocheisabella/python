 
soma__pares =0
soma_impares=0
contagem_pares=0
contagem_impares=0

for i in range(10):
  numero= int(input(f"digite o{i+1}número inteiro"))

if numero % 2==0:
    soma_pares =soma_pares +numero
    quantidade_pares =quantidade_pares +1
else:
    soma__pares=soma_impares +numero
    quantidade_impares =quantidade_impares +1

print (f"\nquantidade de números pares:{contagem_pares}")
print(f"soma total dos números pares:{soma_pares}")
print(f"quantidade de números ímpar:{contagem_ímpar}")
print (f"soam total dos números ímpares:{soma_impares}")
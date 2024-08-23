#Exercício Python 081: Crie um programa que vai ler vários números e colocar em uma lista.      
lnum = []
resp = "Ss"
while True:
    lnum.append(int(input("Digite um valor: ")))
    resp = str(input("Quer continuar? [S/N]: "))
    if resp in "Nn":
        break
print(f"A lista possui {len(lnum)} objetos")
lnum.sort(reverse=True)
print(f"Os valores em ordem decrescente são {lnum}")
elemento = 5 
if elemento in lnum:
    print(f"O número {elemento}, está na lista")
else: 
    print(f"O número {elemento} não está na lista")

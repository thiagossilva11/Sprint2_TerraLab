#Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:                                                                                                    A) Quantas pessoas foram cadastradas.                                                                                                                B) Uma listagem com as pessoas mais pesadas.                                                                                                    
#A) Quantas pessoas foram cadastradas.   
#B) Uma listagem com as pessoas mais pesadas.    
#C) Uma listagem com as pessoas mais leves            

temp = []
princ = []
maior = 0
menor = 0
while True: 
    temp.append(str(input("Digite seu nome:")))
    temp.append(float(input("Digite seu peso: ")))
    if len(princ) == 0: 
        maior = menor = temp[1]
    else: 
        if temp[1] > maior:
            maior = temp[1]
        if temp[1] < menor:
            menor = temp[1]

    princ.append(temp[:])
    temp.clear()
    resp = str(input("Quer continuar? [S/N]: "))
    if resp in "Nn":
        break
print(f"Os dados foram {princ}")
print(f"Ao todo, você cadastrou {len(princ)} pessoas")
print(f"O maior peso foi de {maior} kgs")
for p in princ:
    if p[1] == maior:
        print(f"{p[0]}",end=" ")
print()
print(f"O menor peso foi de {menor} kgs")
for p in princ: 
    if p[1] == menor:
        print(f"{p[0]}",end = " ")


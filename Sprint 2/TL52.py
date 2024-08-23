#Exercício  Python 52: Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
num = int(input("Digite um número: "))
div = 0 
for c in range (1,num +  1) :
    if   num % c == 0: 
        print("\033[33m",end=" ") #Adição de cores
        div = div + 1 
    else:
        print("\033[31m",end=" ")
    print(f"{c}",end=" ")
print(f"\33[mO número {num} foi divisível {div}")
if div == 2:
    print("Por isso ele é primo")
else: 
    print("Por isso ele não é primo")
    
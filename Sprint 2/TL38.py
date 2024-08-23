#Exercício  Python 038: Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: ")) 

if a>b:
    print("O primeiro valor é maior")
elif b>a: 
    print("O segundo valor é maior")
elif a == b:  
    print("Os dois valores são iguais")

       
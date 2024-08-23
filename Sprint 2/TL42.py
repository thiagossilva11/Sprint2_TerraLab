#Exercício  Python 42: Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado
a = int(input("Digite um lado: "))
b= int(input("Digite um lado: "))
c = int(input("Digite o outro lado: "))

#Conferir se as linhas inputadas poderão formar um triângulo

if a < b + c and b < a + c and c <  a + b :
    print("Os lados inputados acima poderão formar um triângulo",end="")
    if a == b == c: 
        print(" Equilátero!")
    
    if a!= b != c !=a:   
        print(" Escaleno!")
    else:
        print (" Isósceles!")

else:
    ("Os valores não podem formar um triângulo")
    

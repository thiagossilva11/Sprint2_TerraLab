#Exercício  Python 53: Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
frase = str(input("Digite uma frase: ")).strip().upper()
palavras = frase.split()
junto = "".join(palavras)
inverso = ""
for letra in range (len(junto)-1, -1,-1): #Fazer a string inversa 
    inverso = inverso + junto[letra]
print(junto, inverso)
if inverso == junto: 
    print("Temos um palídromo!")
else: 
    print("A frase digitada não é palíndromo!")

#Exercício  Python 65: Crie um programa que leia vários números inteiros pelo teclado. No final da execução, 
# mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. 
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores

resp = "Ss"
média = 0
soma = 0
quantidade = 0 
maior = 0
menor = 0
while resp in "Ss": 
    num = int((input("Digite um número: ")))
    soma = soma + num 
    quantidade = quantidade + 1 
    if quantidade == 1:
        maior == menor == num 
    else: 
        if num > maior :
            maior = num
        if num < menor:
            menor = num 
    resp = str(input("Quer continuar? [S ou N]: ")).upper() . strip() [0]
média = soma / quantidade

print(f"Você digitou {quantidade} números e a média foi {média}")
print(f"O maior número foi {maior} e o menor número foi {menor}")

"""🔹 Desafio 5 – Contador de Vogais
Objetivo:
Peça uma palavra e conte quantas vogais ela tem.

Dica: Use in e lower()."""

palavra = input("Digite uma palavra: ")

vogais = ['a','e','i','o','u']

contador = 0

for i in palavra.lower():
    if i in vogais:
        contador += 1
print(f"Tem {contador} vogais na sua palavra")   

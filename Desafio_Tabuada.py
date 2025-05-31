"""🔹 Desafio 4 – Tabuada
Objetivo:
Peça ao usuário um número e exiba a tabuada desse número de 1 a 10."""

num = int(input("Digite um número: "))

for i in range(1,11):

    mult = num * i
    print(f"{num} X {i} = {mult}")

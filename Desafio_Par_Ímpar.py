"""🔹 Desafio 1 – Par ou Ímpar (nível iniciante)
Descrição:
Peça ao usuário que digite um número. Seu programa deve informar se ele é par ou ímpar.

Exemplo de entrada: 7
Saída esperada: O número 7 é ímpar."""

numero = int(input("digite um numero: "))

if numero % 2 == 0:
    print("O número digitado é par")
else:
    print("numero é impar")
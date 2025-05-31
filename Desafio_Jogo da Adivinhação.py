"""🔹 Desafio 3 – Jogo da Adivinhação (nível intermediário/avançado)
Descrição:
O programa deve gerar um número aleatório entre 1 e 100, e o usuário deve tentar adivinhar. 
A cada tentativa, o programa informa se o número é maior ou menor que o chute do usuário. 
O jogo termina quando o número for acertado.

Extras opcionais:
Limitar o número de tentativas
Mostrar quantas tentativas foram feitas"""

from random import *

numero_aleatorio = randrange(0, 101, 2)
print(numero_aleatorio)
#tentativas = 3

while(True):
    chute = int(input("Adivinhe o número: "))
    sub = numero_aleatorio - chute

    if sub > 0:
        print('O numero Aleatorio é maior que seu chute')
    elif sub < 0:
        print('O numero aleatorio é menor que seu chute')
    else:
        print("Acertou!!!")
        break



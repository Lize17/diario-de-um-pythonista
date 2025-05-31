"""🔹 Desafio 2 – Palíndromo (nível intermediário)
Descrição:
Um palíndromo é uma palavra ou frase que pode ser lida da mesma forma de trás pra frente. Verifique se uma palavra digitada é um palíndromo.

Exemplo de entrada: radar
Saída esperada: É um palíndromo.

Dica: Use slicing para inverter strings em Python: palavra[::-1]"""

palavra = input("Digete uma palavra: ")

if palavra == palavra[::-1]:
    print("Palavra é um Palíndromo")
else:
    print(f"A palavra {palavra} não é um Palíndromo")
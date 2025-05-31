"""🔷 Desafio 13 – Validador de senha forte
Objetivo:
Peça uma senha e verifique se ela é forte. Para ser forte, a senha deve:
-Ter pelo menos 8 caracteres
-Ter letras maiúsculas e minúsculas
-Ter números
-Ter pelo menos 1 caractere especial (!@#$%^&* etc)"""

#import getpass
#senha = getpass.getpass("Digite sua senha: ")

print("🔐 Criação de Senha Segura")
print("-----------------------------")
print("A senha deve conter:")
print("✔ Pelo menos 8 caracteres")
print("✔ Letras maiúsculas e minúsculas")
print("✔ Pelo menos 1 número")
print("✔ Pelo menos 1 caractere especial: !@#$%^&*")

senha = input("\nDigite sua senha: ")

tem_min = False
tem_mai = False
tem_num = False
especial = False
tamanho_minimo = 8

for i in senha:
    if i.islower():
        tem_min = True
    if i.isupper():
        tem_mai = True
    if i.isdigit():
        tem_num = True
    if i in '!@#$%^&*':
        especial = True

if len(senha) >= tamanho_minimo and tem_mai and tem_min and tem_num and especial:
    print("Senha forte!")
else:
    print("Senha fraca. Verifique os requisitos.")



#RESTAURANTE DA LAÍSE SOARES
print("Bem-vindos ao restaurante da Laíse Soares!!!")
print("""
===================Restaurante da Soares==================
===Tamanho===Bife Acebolado (BA)===Filé de Frango (FF)===
|------P-----|------R$ 16------|----------R$ 15----------|
|------M-----|------R$ 18------|----------R$ 17----------|
|------G-----|------R$ 22------|----------R$ 21----------|""")
#RECEBENDO O SABOR E TAMANHO DESEJADOS E VALIDANDO-OS
sabor = input("Digite o sabor desejado (BA/FF): ").lower()
while sabor.upper() != "BA" and sabor.upper() != "FF":
    sabor = input("Sabor inválido!Tente novamente: ")
tamanho = input("Digite o tamanho desejado(P/M/G): ").lower()
while tamanho.upper() != "P" and tamanho.upper() != "M"and tamanho.upper() != "G":
    tamanho = input("Tamanho inválido!Tente novamente: ")

#CONSTRUINDO UM APP DE VENDAS DE CAMISETAS
print("Bem-vindos a loja da Laíse Soares!!!!!")
print("""Os juros se aplicam da seguinte maneira:
Se a quantidade de parcelas for menor que 4, o Juros será de 0% (0 / 100);
Se a quantidade de parcelas for igual ou maior que 4 e menor que 6, o Juros será de 4% (4 / 100);
Se a quantidade de parcelas for igual ou maior que 6 e menor que 9, o Juros será de 8% (8 / 100);
Se a quantidade de parcelas for igual ou maior que 9 e menor que 13, o Juros será de 16% (16 / 100);
Se a quantidade de parcelas for igual ou maior que 13, o Juros será de 32% (32 / 100);""")
valordDoPedido = int(input("Digite o valor do seu pedido: "))
quantidadeDeParcelas = int(input("Digite a quantidade de parcelas que você quer: "))
#IMPLEMENTANDO OS JUROS COM BASE NA QUANTIDADE DE PARCELAS
if quantidadeDeParcelas < 4:
    juros = 0
elif 4 <= quantidadeDeParcelas <6:
    juros = 0.04
elif 6 <= quantidadeDeParcelas < 9:
    juros = 0.08
elif 9 <= quantidadeDeParcelas < 13:
    juros = 0.16
else:
    juros = 0.32
#CALCULANDO O VALOR DA PARCELA E DO VALOR TOTAL PARCELADO
valorDaParcela = (valordDoPedido * (1 + juros))/quantidadeDeParcelas
valorTotalParcelado = valorDaParcela * quantidadeDeParcelas
#IMPRIMINDO NA TELA o valor das parcelas e o valor total parcelado
print("O valor das parcelas é de R${}".format(valorDaParcela))
print("O valor do total parcelado é de R${}".format(valorTotalParcelado))
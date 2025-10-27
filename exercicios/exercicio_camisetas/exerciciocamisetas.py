#CONSTRUINDO UM APP DE VENDAS DE CAMISETAS
print("Bem-vindos a loja da Laíse Soares!!!!!")
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


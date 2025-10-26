#CONSTRUINDO UM APP DE VENDAS DE CAMISETAS
print("Bem-vindos a loja da Laíse Soares!!!!!")
valordDoPedido = float(input("Digite o valor do seu pedido: "))
quantidadeDeParcelas = int(input("Digite a quantidade de parcelas que você quer: "))
print("""Os juros se aplicam da seguinte maneira:
Se a quantidade de parcelas for menor que 4, o Juros será de 0% (0 / 100);
Se a quantidade de parcelas for igual ou maior que 4 e menor que 6, o Juros será de 4% (4 / 100);
Se a quantidade de parcelas for igual ou maior que 6 e menor que 9, o Juros será de 8% (8 / 100);
Se a quantidade de parcelas for igual ou maior que 9 e menor que 13, o Juros será de 16% (16 / 100);
Se a quantidade de parcelas for igual ou maior que 13, o Juros será de 32% (32 / 100);""")
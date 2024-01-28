# Você e sua equipe de programadores foram contratados para desenvolver um app de vendas para uma sorveteria. 
# Você ficou com a parte de desenvolver a interface do cliente para retirada do produto.

# A Sorveteria possui seguinte relação:
# •	1 bola de sorvete no sabor tradicional (tr) custa 6 reais, no sabor premium (pr) 7 reais e no especial (es) 8 reais;
# •	2 bolas de sorvete no sabor tradicional (tr) custam 11 reais, no sabor premium (pr) 13 reais e no especial (es) 15 reais;
# •	3 bolas de sorvete no sabor tradicional (tr) custam 15 reais, no sabor premium (pr) 18 reais e no especial (es) 21 reais;

# Elabore um programa em Python que: 
 
# A.	Realizar o print uma mensagem de boas-vindas que apareça o seu nome;  
# B.	Deve-se entrar com o sabor (tr/pr/es) e o número de bolas de sorvete desejado (1/2/3) [EXIGÊNCIA DE CÓDIGO 1 de 6];
# C.	Deve-se executar o print da mensagem de “Quantidade de Bolas de Sorvete Inválida". Se o usuário entrar com a quantidade de bolas de sorvete diferente de 1,2 e 3 repetir a partir do item B [EXIGÊNCIA DE CÓDIGO 2 de 6];
# D.	Deve-se executar o print da mensagem de “Sabor de Sorvete Inválido" se o usuário entrar com um sabor diferente de tr (tradicional), pr (premium) e es (especial). Printar: e repetir a partir do item B; [EXIGÊNCIA DE CÓDIGO 3 de 6];
# E.	Deve-se perguntar se o cliente quer pedir mais alguma coisa. Se sim repetir a partir do item B, senão encerrar o programa printando o valor total [EXIGÊNCIA DE CÓDIGO 4 de 6];
# F.	Deve-se utilizar as estruturas de while, break, continue (todas elas) [EXIGÊNCIA DE CÓDIGO 5 de 6];
# G.	Deve-se fazer comentários no código [EXIGÊNCIA DE CÓDIGO 6 de 6];
# H.	Deve-se colocar na apresentação de saída de console um pedido no qual o usuário errou ao digitar o sabor do sorvete [EXIGÊNCIA DE SAÍDA DE CONSOLE 1 de 3]; 
# I.	Deve-se colocar na apresentação de saída de console um pedido no qual o usuário errou ao digitar o número de bolas de sorvete [EXIGÊNCIA DE SAÍDA DE CONSOLE 2 de 3];
# J.	Deve-se colocar na apresentação de saída de console um pedido com duas opções sabores diferentes com quantidade de bolas diferentes [EXIGÊNCIA DE SAÍDA DE CONSOLE 3 de 3]; 
# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Print para dar boas vindas ao cliente da minha sorveteria
print("Bem-vindo à Sorveteria de Victor Alexandre Oliveira Pádua!\n")

#Função do cardápio
def exibir_cardapio():
    cardapio = [
        ["N° DE BOLAS", "SABOR TRADUCIONAL (tr)", "SABOR PREMIUM (pr)", "SABOR ESPECIAL (es)"],
        [1, "R$ 6,00", "R$ 7,00", "R$ 8,00"],
        [2, "R$ 11,00", "R$ 13,00", "R$ 15,00"],
        [3, "R$ 15,00", "R$ 18,00", "R$ 21,00"]
    ]

    max_col_width = 20

    col_widths = [min(max_col_width, max(len(str(item)) for item in col)) + 2 for col in zip(*cardapio)]
    print(" CARDÁPIO ".center(sum(col_widths) + len(cardapio[0]) + 1, "-"))
    for row in cardapio:
        print("|" + "|".join(str(item).center(col_widths[i]) for i, item in enumerate(row)) + "|")
    line_length = sum(col_widths) + len(cardapio[0]) + 1
    print("-" * line_length)
exibir_cardapio()

#Váriavel que vai armazenar o valor total do pedido
total = 0

while True:
    sabor = input("\nDigite o sabor do sorvete desejado (tr / pr / es): ").lower()
    if sabor not in ["tr", "pr", "es"]:
        print("Sabor inválido. Tente novamente!")
        continue

    quantidade = input("Digite a quantidade de bolas de sorvete desejado (1, 2 ou 3): ")

    if quantidade not in ["1", "2", "3"]:
        print("Número de bolas de sorvete inválido. Tente novamente!")
        continue

    quantidade = int(quantidade)

    if sabor == "tr":
        sabor_completo = "TRADICIONAL"
    elif sabor == "pr":
        sabor_completo = "PREMIUM"
    else:
        sabor_completo = "ESPECIAL"

    #Calcula o preço baseado no sabor e quantidade
    if sabor == "tr":
        if quantidade == 1:
            preco = 6
        elif quantidade == 2:
            preco = 11
        else:
            preco = 15
    elif sabor == "pr":
        if quantidade == 1:
            preco = 7
        elif quantidade == 2:
            preco = 13
        else:
            preco = 18
    else:
        if quantidade == 1:
            preco = 8
        elif quantidade == 2:
            preco = 15
        else:
            preco = 21

    #Apresenta o pedido atual
    print("Você pediu {} bola(s) de sorvete no sabor {}: R$ {:.2f}".format(quantidade, sabor_completo, preco))

    #Atualiza o valor total do pedido
    total += preco

    #Pergunta se o cliente quer pedir mais alguma coisa
    continuar = input("Deseja mais algum sorvete? (S - Para Sim / Qualquer outra tecla - Para NÃO): ")
    if continuar.lower() != "s":
        break

#Print para mostrar ao usuário o valor total do pedido do mesmo
print("\nO valor total do pedido a ser pago é: R$ {:.2f}".format(total))

#FIM!
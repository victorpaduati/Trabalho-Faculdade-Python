# Imagina-se que você é um dos programadores responsáveis pela construção de app de 
# vendas para uma determinada empresa X que vende em atacado. Uma das estratégias de vendas dessa 
# empresa X é dar desconto maiores por unidade as informações abaixo:

# •	Se quantidade for menor que 200 o desconto será de 0%;
# •	Se quantidade for igual ou maior que 200 e menor que 1000 o desconto será de 5%;
# •	Se quantidade for igual ou maior que 1000 e menor que 2000 o desconto será de 10%;
# •	Se quantidade for igual ou maior que 2000 o desconto será de 15%;

# Elabore um programa em Python que:
# A.	Realizar o print uma mensagem de boas-vindas que apareça o seu nome;
# B.	Deve-se entrar com o valor unitário e quantidade do produto [EXIGÊNCIA DE CÓDIGO 1 de 4];
# C.	Deve-se retornar o valor total sem desconto e o valor total com desconto [EXIGÊNCIA DE CÓDIGO 2 de 4];
# D.	Deve-se utilizar as estruturas if, elif e else (todas elas) [EXIGÊNCIA DE CÓDIGO 3 de 4];  
# E.	Deve-se fazer comentários no código [EXIGÊNCIA DE CÓDIGO 4 de 4];
# F.	Deve-se colocar na apresentação de saída de console um pedido recebendo desconto [EXIGÊNCIA DE SAÍDA DE CONSOLE 1 de 1];  
# -------------------------------------------------------------------------------------------------------------------------------

#Print de Boas Vindas à minha loja.
print("Bem-vindo à Loja de Victor Alexandre Oliveira Pádua!")

#Print onde vai solicitar o valor do produto ao usuário e o mesmo vai poder responder.
valor_unitario = float(input("\nEntre com o valor do produto: "))

#Print onde vai solicitar a quantidade do produto que o usuário deseja e o mesmo vai poder responder.
quantidade = int(input("Entre com a quantidade do produto: "))

#Onde vai calcular o valor total sem desconto.
valor_total_sem_desconto = valor_unitario * quantidade

#Estruturas de controle onde verifica se quantidade for x, indica o desconto x. E se a quantidade for y, indica o desconto y.
if quantidade < 200:
    desconto_percentual = 0
elif quantidade >= 200 and quantidade < 1000:
    desconto_percentual = 5
elif quantidade >= 1000 and quantidade < 2000:
    desconto_percentual = 10
else:
    desconto_percentual = 15

#Onde vai calcular o valor do desconto.
desconto = (desconto_percentual / 100) * valor_total_sem_desconto
valor_total_com_desconto = valor_total_sem_desconto - desconto

#Print onde apresenta o valor total SEM desconto ao usuário.
print("\nO valor total SEM desconto é: R$ {:.2f}".format(valor_total_sem_desconto))

#Print onde apresenta o valor total COM desconto ao usuário.
print("O valor total COM desconto de ({}%) é: R$ {:.2f}".format(desconto_percentual, valor_total_com_desconto))

#FIM!
# Você foi contratado para desenvolver um sistema de cobrança de banho para um petshop. Você ficou com a parte de desenvolver a interface com o funcionário.

# O petshop opera da seguinte maneira:
# •	Para cães com peso menor que 3 kg o valor base é de 40 reais;
# •	Para cães com peso igual ou maior que 3 kg e menor que 10 kg o valor base é de 50 reais;
# •	Para cães com peso igual ou maior que 10 kg e menor que 30kg o valor base é de 60 reais;  
# •	Para cães com peso igual ou maior que 30 kg e menor que 50kg o valor base é de 70 reais; 

# 	Para cães com pelo curto (c) o multiplicador é 1;
# 	Para cães com pelo médio (m) o multiplicador é 1.5;
# 	Para cães com pelo longo (l) o multiplicador é 2;

# ♦	Para o adicional de cortar unhas (1) do cachorro é cobrado um valor extra de 10 reais;
# ♦	Para o adicional de escovar os dentes (2) do cachorro é cobrado um valor extra de 12 reais;
# ♦	Para o adicional de limpar as orelhas (3) do cachorro é cobrado um valor extra de 15 reais;
# ♦	Para o adicional de não querer mais nada (0) é cobrado um valor extra de 0 reais;


# O valor final da conta é calculado da seguinte maneira:

# total = base * multiplicador + extra

# Elabore um programa em Python que: 
 
# A.	Realizar o print uma mensagem de boas-vindas que apareça o seu nome;
# B.	Deve-se criar uma função chamada cachorro_peso() em que: [EXIGÊNCIA DE CÓDIGO 1 de 6];
# a.	Pergunta o peso do cachorro;
# b.	Retorna o valor base com base no peso;
# c.	Repete a pergunta do item B.a se peso for igual ou acima 50kg;
# d.	Repete a pergunta do item B.a se digitar um valor não numérico;
# C.	Deve-se criar uma função chamada cachorro_pelo() em que: [EXIGÊNCIA DE CÓDIGO 2 de 6];
# a.	Pergunta o pelo do cachorro;
# b.	Retorna o multiplicador com base nos itens descritos no enunciado;
# c.	Repete a pergunta do item C.a se digitar uma opção diferente de: c/m/l;
# D.	Deve-se criar uma função chamada cachorro_extra() em que: [EXIGÊNCIA DE CÓDIGO 3 de 6];
# a.	Pergunta pelo serviço adicional;
# b.	Acumular o valor extra de cada adicional;
# c.	Repetir a pergunta item D.a enquanto não se digitar opção de: "não querer mais nada (0)";
# d.	Quando digitar o adicional não querer mais nada (0) retornar o valor extra;
# E.	Deve-se calcular o total a pagar na parte do main conforme descrito no enunciado [EXIGÊNCIA DE CÓDIGO 4 de 6];
# F.	Deve-se utilizar try/except [EXIGÊNCIA DE CÓDIGO 5 de 6];
# G.	Deve-se fazer comentários no código [EXIGÊNCIA DE CÓDIGO 6 de 6];
# H.	Deve-se colocar na apresentação de saída de console um pedido no qual o usuário digitou um valor não numérico para o peso [EXIGÊNCIA DE SAÍDA DE CONSOLE 1 de 3];
# I.	Deve-se colocar na apresentação de console um pedido no qual o usuário digitou um valor acima 50 para o peso [EXIGÊNCIA DE SAÍDA DE CONSOLE 2 de 3];
# J.	Deve-se colocar na apresentação de console um pedido no qual o peso e o tipo de pelo sejam válidos e com mais 2 extras [EXIGÊNCIA DE SAÍDA DE CONSOLE 3 de 3];
# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Print para dar boas vindas ao meu sistema
print('Bem-vindo ao sistema desenvolvido pelo Victor Alexandre Oliveira Pádua!')

#Função para perguntar e calcular o valor base com base no peso do cachorro
def cachorro_peso():
    while True:
        try:
            peso = float(input("\nQual é o peso do cachorro (em kg)? "))
            if peso < 3:
                return 40
            elif peso < 10:
                return 50
            elif peso < 30:
                return 60
            elif peso < 50:
                return 70
            else:
                print("Não aceitamos cachorros tão grandes.")
                print("Por favor, entre com o peso do cachorro novamente.")
        except ValueError:
            print("Você digitou um valor não numérico.")
            print("Por favor, entre com o peso do cachorro novamente.")

#Função que pergunta e calcular o multiplicador com base no tipo de pelo do cachorro
def cachorro_pelo():
    while True:
        pelo = input("\nQual é o pelo do seu cachorro? \n"
                     "c - Pelo Curto\n"
                     "m - Pelo Médio\n"
                     "l - Pelo Longo\n").lower()
        if pelo == 'c':
            return 1
        elif pelo == 'm':
            return 1.5
        elif pelo == 'l':
            return 2
        else:
            print("Opção inválida. Escolha c, m ou l.")

#Função que pergunta e calcula o valor extra com base nos serviços adicionais
def cachorro_extra():
    extras = 0
    while True:
        try:
            adicional = int(input("\nDeseja adicionar mais algum serviço? \n"
                                 "1 - Corte de Unhas - R$ 10,00\n"
                                 "2 - Escovar Dentes - R$ 12,00\n"
                                 "3 - Limpeza de Orelhas - R$ 15,00\n"
                                 "0 - Não desejo mais nada.\n"))
            if adicional == 0:
                return extras
            elif adicional == 1:
                extras += 10
            elif adicional == 2:
                extras += 12
            elif adicional == 3:
                extras += 15
            else:
                print("Opção inválida. Escolha um serviço válido.")
        except ValueError:
            print("Por favor, digite um valor numérico válido.")

#Minha função principal
def main():
    base = cachorro_peso()
    multiplicador = cachorro_pelo()
    extras = cachorro_extra()

    total = base * multiplicador + extras

    if extras > 0:
        print("\nValor dos adicionais: R$ {:.2f}".format(extras))

    print("Total a pagar: R$ {:.2f} - (Peso: {} * Pelo: {} + Adicional(ais): {})".format(total, base, multiplicador, extras))

if __name__ == "__main__":
    main()

#FIM!
# Você e sua equipe de programadores foram contratados por pequena empresa para desenvolver o software de gerencialme de pessoas. 
# Este software deve ter o seguinte menu e opções:

# 1)	Cadastrar Colaborador
# 2)	Consultar Colaborador
# 1.	Consultar Todos 
# 2.	Consultar por Id;
# 3.	Consultar por Setor;
# 4.	Retornar ao menu;
# 3)	Remover Colaborador
# 4)	Encerrar Programa

# Elabore um programa em Python que: 
 
# A.	Realizar o print uma mensagem de boas-vindas que apareça o seu nome;
# B.	Deve-se criar uma lista vazia com o nome de lista_colaboradores e a variável id_global com valor inicial igual a 0 [EXIGÊNCIA DE CÓDIGO 1 de 7];
# C.	Deve-se criar uma função chamada cadastrar_colaborador(id) em que: [EXIGÊNCIA DE CÓDIGO 2 de 7];
# a.	Pergunta nome, setor, pagamento do colaborador;
# b.	Armazena o id (este é fornecido via parâmetro da função), nome, setor, salário dentro de um dicionário;
# c.	Copiar o dicionário dentro para dentro da da lista_colaboradores;
# D.	Deve-se criar uma função chamada consultar_colaborador() em que: [EXIGÊNCIA DE CÓDIGO 3 de 7];
# a.	Deve-se pergunta qual opção deseja (1. Consultar Todos / 2. Consultar por Id / 3. Consultar por Setor / 4. Retornar ao menu) e   realizar o print “Opção inválida" se entrar com valor diferente de 1, 2, 3 ou 4:
# i.	Se Consultar Todos, apresentar todos os colaboradores com todos os seus dados cadastrados;
# ii.	Se Consultar por Id, apresentar o colaborador específico com todos os seus dados cadastrados;
# iii.	Se Consultar por Setor, apresentar todos os colaboradores do setor específico com todos os seus dados cadastrados;
# iv.	Se Retornar ao menu, deve-se retornar ao menu principal
# E.	Deve-se criar uma função chamada remover_colaborador() em que: [EXIGÊNCIA DE CÓDIGO 4 de 7];
# a.	Deve-se pergunta pelo id do colaborador a ser removido;
# b.	Remover o colaborador da lista_colaboradores;
# F.	Deve-se criar uma estrutura de menu no main em que: [EXIGÊNCIA DE CÓDIGO 5 de 7];
# a.	Deve-se pergunta qual opção deseja (1. Cadastrar Colaborador / 2. Consultar Colaborador / 3. Remover Colaborador / 4. Encerrar Programa) e realizar o print “Opção inválida" se entrar com valor diferente de 1, 2, 3 ou 4 :
# i.	Se Cadastrar Colaborador, acrescentar em um a variavel id_ global e chamar a função cadastrar_colaborador(id_ global);
# ii.	Se Consultar Colaborador, chamar função consultar_colaborador();
# iii.	Se Remover Colaborador, chamar função remover_colaborador();
# iv.	Se Encerrar Programa, sair do menu (e com isso acabar a execução do código);
# G.	Deve-se utilizar lista de dicionários (uma lista contento dicionários dentro)  [EXIGÊNCIA DE CÓDIGO 6 de 7];
# H.	Deve-se fazer comentários no código [EXIGÊNCIA DE CÓDIGO 7 de 7];
# I.	Deve-se colocar na apresentação de saída de console o cadastro de 3 colaboradores (sendo 2 deles no mesmo setor) [EXIGÊNCIA DE SAÍDA DE CONSOLE 1 de 4];
# J.	Deve-se colocar na apresentação de saída de console a consulta de todos os colaboradores [EXIGÊNCIA DE SAÍDA DE CONSOLE 1 de ];
# K.	Deve-se colocar na apresentação de saída de console a consulta por código de um dos colaboradores [EXIGÊNCIA DE SAÍDA DE CONSOLE 2 de 4];
# L.	Deve-se colocar na apresentação de saída de console a consulta por setor em que 2 colaboradores façam parte [EXIGÊNCIA DE SAÍDA DE CONSOLE 3 de 4];
# M.	Deve-se colocar na apresentação de saída de console a remoção de um dos colaboradores e na sequência a consulta de todos os colaboradores [EXIGÊNCIA DE SAÍDA DE CONSOLE 4 de 4];
# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Print de boas vindas aos usuários do meu sistema
print("\nBem-vindo ao Controle de Colaboradores de Victor Alexandre Oliveira Pádua!")

#Função para cadastrar os colaboradores
def cadastrar_colaborador(id):
    cadastrar = "*" * 74
    print(cadastrar)
    fraseCadastrar = " MENU CADASTRAR COLABORADOR "
    linhaCadastrar = "-" * 23
    resultadoCadastrar = linhaCadastrar + fraseCadastrar + linhaCadastrar
    print(resultadoCadastrar)
    id = int(input('Digite o ID do colaborador: '))
    nome = input("Digite o nome do colaborador: ")
    setor = input("Digite o setor do colaborador: ")
    salario = float(input("Digite o pagamento do colaborador: R$"))

    #dicionário com os dados do colaborador, conforme solicitado no exercicio
    colaborador = {
        "ID": id,
        "Nome": nome,
        "Setor": setor,
        "Pagamento": salario
    }
    #dicionário com lista dos colaboradores
    lista_colaboradores.append(colaborador)

#Função para consultar os colaboradores
def consultar_colaborador():
    consultar = "*" * 74
    print(consultar)
    fraseConsultar = " MENU CONSULTAR COLABORADOR "
    linhaConsultar = "-" * 23
    resultadoConsultar = linhaConsultar + fraseConsultar + linhaConsultar
    print(resultadoConsultar)
    while True:
        opcao = int(input("\nEscolha uma opção: \n"
                          "1. Consultar Todos os Colaboradores\n"
                          "2. Consultar Colaboradores por ID\n"
                          "3. Consultar Colaborado(es) por Setor\n"
                          "4. Retornar\n"))

        if opcao == 1:
            print("\nConsulta de todos os colaboradores:")
            for colaborador in lista_colaboradores:
                print("-" * 22)
                print("ID:", colaborador["ID"])
                print("Nome:", colaborador["Nome"])
                print("Setor:", colaborador["Setor"])
                print("Pagamento:", colaborador["Pagamento"])
            print("-" * 22)
        elif opcao == 2:
            id_busca = int(input("Digite o ID do colaborador: "))
            for colaborador in lista_colaboradores:
                if colaborador["ID"] == id_busca:
                    print("-" * 22)
                    print("ID:", colaborador["ID"])
                    print("Nome:", colaborador["Nome"])
                    print("Setor:", colaborador["Setor"])
                    print("Pagamento:", colaborador["Pagamento"])
                    print("-" * 22)
                    break
            else:
                print("Colaborador não encontrado.")
        elif opcao == 3:
            setor_busca = input("Digite o setor a ser consultado: ")
            print("\nConsulta por setor em que colaboradores fazem parte:")
            for colaborador in lista_colaboradores:
                if colaborador["Setor"] == setor_busca:
                    print("-" * 22)
                    print("ID:", colaborador["ID"])
                    print("Nome:", colaborador["Nome"])
                    print("Setor:", colaborador["Setor"])
                    print("Pagamento:", colaborador["Pagamento"])
        elif opcao == 4:
            return
        else:
            print("Opção inválida.")

#Função para remover os colaboradores
def remover_colaborador():
    remover = "*" * 74
    print(remover)
    fraseRemover = " MENU REMOVER COLABORADOR "
    linhaRemover = "-" * 24
    resultadoRemover = linhaRemover + fraseRemover + linhaRemover
    print(resultadoRemover)
    id_remover = int(input("Digite o ID do colaborador a ser removido: "))
    for colaborador in lista_colaboradores:
        if colaborador["ID"] == id_remover:
            lista_colaboradores.remove(colaborador)
            print("Colaborador removido com sucesso.")
            break
    else:
        print("Colaborador não encontrado.")

#minha função principal
def main():
    id_global = 0

    while True:
        linhaBoasVindas = "*" * 74
        print(linhaBoasVindas)
        fraseMenuPrincipal = " MENU PRINCIPAL "
        linhaMenuPrincipal = "-" * 29
        resultadoMenuPrincipal = linhaMenuPrincipal + fraseMenuPrincipal + linhaMenuPrincipal
        print(resultadoMenuPrincipal)
        opcao = int(input("Escolha uma opção: \n"
                            "1 - Cadastrar Colaborador\n"
                            "2 - Consultar Colaborador(es)\n"
                            "3 - Remover Colaborador\n"
                            "4 - Sair\n"))

        if opcao == 1:
            id_global += 1
            cadastrar_colaborador(id_global)
        elif opcao == 2:
            consultar_colaborador()
        elif opcao == 3:
            remover_colaborador()
        elif opcao == 4:
            print("Encerrando o programa...")
            break
        else:
            print("Opção inválida.")

lista_colaboradores = []

main()

print("\n--- Apresentação de Saída de Console ---")

cadastrar_colaborador(1)
cadastrar_colaborador(2)
cadastrar_colaborador(3)

print("\nConsulta de todos os colaboradores:")
consultar_colaborador()

print("\nConsulta por código de um dos colaboradores:")
consultar_colaborador()

print("\nConsulta por setor em que 2 colaboradores fazem parte:")
consultar_colaborador()

print("\nRemoção de um colaborador e consulta de todos os colaboradores:")
remover_colaborador()
consultar_colaborador()

#FIM!
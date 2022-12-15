"""
44) Desenvolva um programa em que:
a) Criar uma agenda telefônica para o Carlos, ela deve conter 6 contatos com o par nome e telefone
b) Criar uma agenda telefônica para a Karina, ela deve conter 7 contatos com o par nome e telefone
c) Mostre o conteúdo da agenda telefônica do Carlos.
d) Mostre o conteúdo da agenda telefônica da Karina.
e) Criar uma agenda telefônica, que seja a junção das 2 agendas
f) Qual estrutura de dados vc utilizou? Justifique a sua resposta
"""
def adicionar1(listaCarlos):
    contato = {
        "nome": input("Digite o Nome do Contato: "),
        "telefone": input("Digite o Telefone do Contato: ")
    }
    listaCarlos.append(contato)
    print("Contato {} foi Adicionado!\n".format(contato["nome"]))


def adicionar2(listaKarina):
    contato = {
        "nome": input("Digite o Nome do Contato: "),
        "telefone": input("Digite o Telefone do Contato: ")
    }
    listaKarina.append(contato)
    print("Contato {} foi Adicionado!\n".format(contato["nome"]))


def listar1(listaCarlos):
    print("==== Listar Contatos do Carlos ====")
    if len(listaCarlos) > 0:
        for i, contato in enumerate(listaCarlos):
            print("Contato {}:".format(i + 1))
            print("\tNome: {}".format(contato['nome']))
            print("\tTelefone: {}".format(contato['telefone']))


def listar2(listaKarina):
    print("==== Listar Contatos da Karina ====")
    if len(listaKarina) > 0:
        for i, contato in enumerate(listaKarina):
            print("Contato {}:".format(i + 1))
            print("\tNome: {}".format(contato['nome']))
            print("\tTelefone: {}".format(contato['telefone']))


def listarT(listaTodos):
    print("==== Listar Contatos de Todos ====")
    if len(listaTodos) > 0:
        for i, contato in enumerate(listaCarlos + listaKarina):
            print("Contato {}:".format(i + 1))
            print("\tNome: {}".format(contato['nome']))
            print("\tTelefone: {}".format(contato['telefone']))


def principal():
    listaCarlos = []
    listaKarina = []
    listaTodos = [listaCarlos + listaKarina]

    while True:
        print("===== Agenda de Contato ====")
        print("[1] Adicionar Contatos Carlos")
        print("[2] Adicionar Contatos Karina")
        print("[3] Listar Contatos Carlos")
        print("[4] Listar Contatos Karina")
        print("[5] Listar Todos os Contatos")
        print("[6] Sair")
        opcao = int(input("Opção Escolhida: "))

        if opcao == 1:
            adicionar1(listaCarlos)

        elif opcao == 2:
            adicionar2(listaKarina)

        elif opcao == 3:
            listar1(listaCarlos)

        elif opcao == 4:
            listar2(listaKarina)

        elif opcao == 5:
            listarT(listaTodos)

        elif opcao == 6:
            print("Saindo do Programa...")
            break
        else:
            print("Opção Invalida!")


principal()


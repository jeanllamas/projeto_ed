import os
from cliente import Cliente
from agencia import Agencia


def menu_crud():
    opcao = -1
    while opcao != 0:
        os.system("cls")
        print("1. Inserir")
        print("2. Alterar")
        print("3. Consultar")
        print("4. Remover")
        print("5. Exportar em arquivo")
        print("6. Importar de arquivo")
        print("0. Voltar")

        opcao = int(input("\nOpção número: "))
        os.system("cls")
        return opcao


opcao = -1
while opcao != 0:
    try:
        os.system("cls")
        print("| ======== Menu de Cadastros ======== |")
        print("|  1. Cliente                         |")
        print("|  2. Agência                         |")
        print("|  3. Conta corrente e especial       |")
        print("|  4. Movimento                       |")
        print("|  0. Sair                            |")

        opcao = int(input("\nOpção número: "))
        os.system("cls")

        match opcao:
            case 1:
                print("Cliente\n")
                match menu_crud():
                    case 1:
                        print("Inserir Cliente\n")
                        try:
                            nome = input("Nome completo: ")
                            cpf = int(input("CPF: "))
                            data_nasc = int(input("Data de Nascimento: "))
                            endereco = input("Endereço: ")
                            telefone = int(input("Telefone: "))
                            email = input("E-mail: ")
                        except ValueError:
                            print("\nErro! Tente novamente")
                        else:
                            cliente = Cliente(
                                nome, cpf, data_nasc, endereco, telefone, email
                            )
                            Cliente.inserir(cliente)
                    case 2:
                        print("Alterar Cliente\n")
                        try:
                            cpf = int(input("CPF do Cliente: "))
                        except ValueError:
                            input("\nCPF inválido\n")
                        else:
                            if Cliente.verificar_cpf(cpf):
                                nome = input("Nome completo: ")
                                data_nasc = int(input("Data de Nascimento: "))
                                endereco = input("Endereço: ")
                                telefone = int(input("Telefone: "))
                                email = input("E-mail: ")
                                cliente = Cliente(
                                    nome, cpf, data_nasc, endereco, telefone, email
                                )
                                Cliente.alterar(cliente)
                            else:
                                input("\nCPF não encontrado\n")
                                continue
                    case 3:
                        print("Consultar Cliente\n")
                        try:
                            cpf = int(input("CPF do Cliente: "))
                        except ValueError:
                            input("\nCPF inválido\n")
                        else:
                            if Cliente.verificar_cpf(cpf):
                                Cliente.consultar(cpf)
                            else:
                                input("\nCPF não encontrado\n")
                    case 4:
                        print("Remover Cliente\n")
                        try:
                            cpf = int(input("CPF do Cliente: "))
                        except ValueError:
                            input("\nCPF inválido\n")
                        else:
                            if Cliente.verificar_cpf(cpf):
                                Cliente.remover(cpf)
                            else:
                                input("\nCPF não encontrado\n")
                                continue
                    case 0:
                        print()
            case 2:
                print("Agência")
                match menu_crud():
                    case 1:
                        print("Inserir Agência\n")
                        try:
                            nome = input("Nome da Agência: ")
                            cnpj = int(input("CNPJ: "))
                            num_agencia = int(input("Número de Agência: "))
                            num_banco = int(input("Número do Banco: "))
                            endereco = input("Endereço: ")
                            telefone = int(input("Telefone: "))
                            email = input("E-mail: ")
                        except ValueError:
                            print("\nErro! Tente novamente")
                        else:
                            agencia = Agencia(
                                nome,
                                cnpj,
                                num_agencia,
                                num_banco,
                                endereco,
                                telefone,
                                email,
                            )
                            Agencia.alterar(agencia)
                    case 2:
                        print("Alterar Agência\n")
                        try:
                            cnpj = int(input("CNPJ da Agência: "))
                        except ValueError:
                            input("\nCNPJ inválido\n")
                        else:
                            if Agencia.verificar_cnpj(cnpj):
                                nome = input("Nome da Agência: ")
                                num_agencia = int(input("Número de Agência: "))
                                num_banco = int(input("Número do Banco: "))
                                endereco = input("Endereço: ")
                                telefone = int(input("Telefone: "))
                                email = input("E-mail: ")
                                agencia = Agencia(
                                    nome,
                                    cnpj,
                                    num_agencia,
                                    num_banco,
                                    endereco,
                                    telefone,
                                    email,
                                )
                                Agencia.inserir(agencia)
                            else:
                                input("\nCNPJ não encontrado\n")
                                continue
                    case 3:
                        print("Consultar Agência\n")
                        try:
                            cnpj = int(input("CNPJ da Agência: "))
                        except ValueError:
                            input("\nCNPJ inválido\n")
                        else:
                            if Agencia.verificar_cnpj(cnpj):
                                Agencia.consultar(cnpj)
                            else:
                                input("\nCNPJ não encontrado\n")
                    case 4:
                        print("Remover Agência\n")
                        try:
                            cnpj = int(input("CNPJ da Agência: "))
                        except ValueError:
                            input("\nCNPJ inválido\n")
                        else:
                            if Agencia.verificar_cnpj(cnpj):
                                Agencia.remover(cnpj)
                            else:
                                input("\nCNPJ não encontrado\n")
                                continue
                    case 0:
                        print()
            case 3:
                print("Conta corrente e especial")
            case 4:
                print("Movimento")
            case 0:
                print()
            case _:
                print("\nOpção inexistente")
                input()
    except ValueError:
        print("\nErro! Tente novamente")

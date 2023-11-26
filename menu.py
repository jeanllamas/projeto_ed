import os
from cliente import Cliente
from agencia import Agencia
from conta import Conta
from movimento import Movimento


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
        print("|  3. Conta corrente                  |")
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
                            telefone = int(input("Telefone: "))
                            email = input("E-mail: ")
                        except ValueError:
                            print("\nErro! Tente novamente")
                        else:
                            cliente = Cliente(nome, cpf, data_nasc, telefone, email)
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
                                telefone = int(input("Telefone: "))
                                email = input("E-mail: ")
                                cliente = Cliente(nome, cpf, data_nasc, telefone, email)
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
                            cod_agencia = int(input("Código da Agência: "))
                            telefone = int(input("Telefone: "))
                            email = input("E-mail: ")
                        except ValueError:
                            print("\nErro! Tente novamente")
                        else:
                            agencia = Agencia(
                                nome,
                                cod_agencia,
                                telefone,
                                email,
                            )
                            Agencia.inserir(agencia)
                    case 2:
                        print("Alterar Agência\n")
                        try:
                            cod_agencia = int(input("Código da Agência: "))
                        except ValueError:
                            input("\nAgência não encontrada\n")
                        else:
                            if Agencia.verificar_agencia(cod_agencia):
                                nome = input("Nome da Agência: ")
                                telefone = int(input("Telefone: "))
                                email = input("E-mail: ")
                                agencia = Agencia(
                                    nome,
                                    cod_agencia,
                                    telefone,
                                    email,
                                )
                                Agencia.alterar(agencia)
                            else:
                                input("\nAgência não encontrada\n")
                                continue
                    case 3:
                        print("Consultar Agência\n")
                        try:
                            cod_agencia = int(input("Código da Agência: "))
                        except ValueError:
                            input("\nAgência não encontrada\n")
                        else:
                            if Agencia.verificar_agencia(cod_agencia):
                                Agencia.consultar(cod_agencia)
                            else:
                                input("\nAgência não encontrada\n")
                    case 4:
                        print("Remover Agência\n")
                        try:
                            cod_agencia = int(input("Código da Agência: "))
                        except ValueError:
                            input("\nAgência não encontrada\n")
                        else:
                            if Agencia.verificar_agencia(cod_agencia):
                                Agencia.remover(cod_agencia)
                            else:
                                input("\nAgência não encontrada\n")
                                continue
                    case 0:
                        print()
            case 3:
                print("Conta Corrente")
                opcao_conta = -1
                while opcao_conta != 0:
                    os.system("cls")
                    print("1. Criar conta")
                    print("2. Consultar saldo")
                    print("3. Extrato")
                    print("0. Voltar")

                    opcao_conta = int(input("\nOpção número: "))

                    match opcao_conta:
                        case 1:
                            print("Criar conta")
                            cpf = int(input("CPF do Cliente: "))
                            cod_agencia = int(input("Código da Agência: "))
                            tipo = input(
                                "Tipo de Conta (C para Corrente ou E para Especial): "
                            )
                            if tipo == "E":
                                limite_especial = (
                                    float(input("Limite Especial: R$")) * -1
                                )
                            elif tipo == "C":
                                limite_especial = 0.0
                            else:
                                print("Limite inválido")
                            conta = Conta(cpf, cod_agencia, tipo, limite_especial)
                            Conta.inserir(conta)
                        case 2:
                            print("Consultar saldo")
                            cpf = int(input("CPF do Cliente: "))
                            cod_agencia = int(input("Código da Agência: "))
                            Conta.consultar_saldo(cpf, cod_agencia)
                        case 3:
                            print("Extrato")
                            cpf = int(input("CPF do Cliente: "))
                            cod_agencia = int(input("Código da Agência: "))
                            Movimento.extrato(cpf, cod_agencia)

            case 4:
                print("Movimento")
                opcao_movimento = -1
                while opcao_movimento != 0:
                    os.system("cls")
                    print("1. Entrada")
                    print("2. Saída")
                    print("0. Voltar")

                    opcao_movimento = int(input("\nOpção número: "))
                    os.system("cls")

                    match opcao_movimento:
                        case 1:
                            print("Entrada")
                            cpf = int(input("CPF do Cliente: "))
                            cod_agencia = int(input("Código da Agência: "))
                            valor = float(input("Quantia a depositar: R$"))
                            movimento = Movimento(cpf, cod_agencia, valor)
                            Movimento.entrada(movimento)
                        case 2:
                            print("Saída")
                            cpf = int(input("CPF do Cliente: "))
                            cod_agencia = int(input("Código da Agência: "))
                            valor = float(input("Quantia a retirar: R$"))
                            movimento = Movimento(cpf, cod_agencia, valor)
                            Movimento.saida(movimento)

            case 0:
                print()
            case _:
                print("\nOpção inexistente")
                input()
    except ValueError:
        print("\nErro! Tente novamente")

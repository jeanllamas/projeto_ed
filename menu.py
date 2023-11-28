import os
from cliente import Cliente
from agencia import Agencia
from conta import Conta
from movimento import Movimento


def menu_crud():
    opcao = -1
    while opcao != 0:
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
                print("Cliente")
                match menu_crud():
                    case 1:
                        print("Inserir Cliente\n")
                        try:
                            nome = input("Nome completo: ")
                            cpf = input("CPF: ")
                            if Cliente.verificar_cpf(cpf):
                                print("\nCPF já utilizado.")
                                continue
                            if not cpf.isnumeric() or len(cpf) != 11:
                                input("\nCPF inválido.\nDigite apenas 11 dígitos.")
                                continue
                            data_nasc = input("Data de Nascimento: ")
                            if not data_nasc.isnumeric() or (len(data_nasc) != 8):
                                input(
                                    "\nData de nascimento inválida.\nUse o formato DDMMAAAA, sem barras."
                                )
                                continue
                            telefone = input("Telefone: ")
                            if not telefone.isnumeric() or len(telefone) != 11:
                                input(
                                    "\nNúmero de telefone inválido.\nInsira 11 dígitos, incluindo o DDD."
                                )
                                continue
                            email = input("E-mail: ")
                        except ValueError:
                            input("\nErro! Tente novamente")
                        else:
                            cliente = Cliente(nome, cpf, data_nasc, telefone, email)
                            Cliente.inserir(cliente)
                    case 2:
                        print("Alterar Cliente\n")
                        try:
                            cpf = input("CPF do Cliente: ")
                            if not cpf.isnumeric() or len(cpf) != 11:
                                input("\nCPF inválido.\nDigite apenas 11 dígitos.")
                                continue
                        except ValueError:
                            input("\nCPF inválido\n")
                        else:
                            if Cliente.verificar_cpf(cpf):
                                nome = input("Nome completo: ")
                                data_nasc = input("Data de Nascimento: ")
                                if not data_nasc.isnumeric() or (len(data_nasc) != 8):
                                    input(
                                        "\nData de nascimento inválida.\nUse o formato DDMMAAAA, sem barras."
                                    )
                                    continue
                                telefone = input("Telefone: ")
                                if not telefone.isnumeric() or len(telefone) != 11:
                                    input(
                                        "\nNúmero de telefone inválido.\nDigite no máximo 11 dígitos, incluindo o DDD."
                                    )
                                    continue
                                email = input("E-mail: ")
                                cliente = Cliente(nome, cpf, data_nasc, telefone, email)
                                Cliente.alterar(cliente)
                            else:
                                input("\nCliente não encontrado")
                                continue
                    case 3:
                        print("Consultar Cliente\n")
                        try:
                            cpf = input("CPF do Cliente: ")
                            if not cpf.isnumeric() or len(cpf) != 11:
                                input("\nCPF inválido.\nDigite apenas 11 dígitos.")
                                continue
                        except ValueError:
                            input("\nCPF inválido\n")
                        else:
                            if Cliente.verificar_cpf(cpf):
                                Cliente.consultar(cpf)
                            else:
                                input("\nCliente não encontrado\n")
                    case 4:
                        print("Remover Cliente\n")
                        try:
                            cpf = input("CPF do Cliente: ")
                        except ValueError:
                            input("\nCPF inválido\n")
                        else:
                            if Cliente.verificar_cpf(cpf):
                                Cliente.remover(cpf)
                            else:
                                input("\nCPF não encontrado\n")
                                continue
                    case 5:
                        print("Exportar em arquivo\n")
                        Cliente.exportar()
                    case 6:
                        print("Importar de arquivo\n")
                        Cliente.importar()
                    case 0:
                        print()
            case 2:
                print("Agência")
                match menu_crud():
                    case 1:
                        print("Inserir Agência\n")
                        try:
                            nome = input("Nome da Agência: ")
                            cod_agencia = input("Código da Agência: ")
                            if not cod_agencia.isnumeric() or len(cod_agencia) != 4:
                                input(
                                    "\nCódigo de agência inválido.\nDigite apenas 4 dígitos."
                                )
                                continue
                            if Agencia.verificar_agencia(cod_agencia):
                                input("\nCódigo de agência já utilizado.")
                                continue
                            telefone = input("Telefone: ")
                            if not telefone.isnumeric() or len(telefone) != 11:
                                input(
                                    "\nNúmero de telefone inválido.\nInsira 11 dígitos, incluindo o DDD."
                                )
                                continue
                            email = input("E-mail: ")
                        except ValueError:
                            input("\nErro! Tente novamente")
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
                            cod_agencia = input("Código da Agência: ")
                            if not cod_agencia.isnumeric() or len(cod_agencia) != 4:
                                input(
                                    "\nCódigo de agência inválido.\nDigite apenas 4 dígitos."
                                )
                                continue
                        except ValueError:
                            input("\nAgência não encontrada\n")
                        else:
                            if Agencia.verificar_agencia(cod_agencia):
                                nome = input("Nome da Agência: ")
                                telefone = input("Telefone: ")
                                if not telefone.isnumeric() or len(telefone) != 11:
                                    input(
                                        "\nNúmero de telefone inválido.\nInsira 11 dígitos, incluindo o DDD."
                                    )
                                    continue
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
                            cod_agencia = input("Código da Agência: ")
                            if not cod_agencia.isnumeric() or len(cod_agencia) != 4:
                                input(
                                    "\nCódigo de agência inválido.\nDigite apenas 4 dígitos."
                                )
                                continue
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
                            cod_agencia = input("Código da Agência: ")
                            if not cod_agencia.isnumeric() or len(cod_agencia) != 4:
                                input(
                                    "\nCódigo de agência inválido.\nDigite apenas 4 dígitos."
                                )
                                continue
                        except ValueError:
                            input("\nAgência não encontrada\n")
                        else:
                            if Agencia.verificar_agencia(cod_agencia):
                                Agencia.remover(cod_agencia)
                            else:
                                input("\nAgência não encontrada\n")
                                continue
                    case 5:
                        print("Exportar em arquivo\n")
                        Agencia.exportar()
                    case 6:
                        print("Importar de arquivo\n")
                        Agencia.importar()
                    case 0:
                        print()
            case 3:
                opcao_conta = -1
                while opcao_conta != 0:
                    os.system("cls")
                    print("Conta Corrente")
                    print("1. Criar conta")
                    print("2. Consultar saldo")
                    print("3. Extrato")
                    print("4. Exportar em arquivo")
                    print("5. Importar de arquivo")
                    print("0. Voltar")

                    opcao_conta = int(input("\nOpção número: "))
                    os.system("cls")

                    match opcao_conta:
                        case 1:
                            print("Criar conta\n")
                            cpf = input("CPF do Cliente: ")
                            if not Cliente.verificar_cpf(cpf):
                                input("\nCliente não encontrado")
                                continue
                            if not cpf.isnumeric() or len(cpf) != 11:
                                input("\nCPF inválido.\nDigite apenas 11 dígitos.")
                                continue
                            cod_agencia = input("Código da Agência: ")
                            if not Agencia.verificar_agencia(cod_agencia):
                                input("\nAgência não encontrada")
                                continue
                            if not cod_agencia.isnumeric() or len(cod_agencia) != 4:
                                input(
                                    "\nCódigo de agência inválido.\nDigite apenas 4 dígitos."
                                )
                                continue
                            tipo = input(
                                "Tipo de Conta (C para Corrente ou E para Especial): "
                            ).upper()
                            if tipo == "E":
                                try:
                                    limite_especial = (
                                        float(input("Limite Especial: R$")) * -1
                                    )
                                    conta = Conta(
                                        cpf, cod_agencia, tipo, limite_especial
                                    )
                                    Conta.inserir(conta)
                                except ValueError:
                                    input("\nErro! Tente novamente")
                            elif tipo == "C":
                                limite_especial = 0.0
                                conta = Conta(cpf, cod_agencia, tipo, limite_especial)
                                Conta.inserir(conta)
                            else:
                                input("\nTipo inválido")
                        case 2:
                            print("Consultar saldo\n")
                            cpf = input("CPF do Cliente: ")
                            if not Cliente.verificar_cpf(cpf):
                                input("\nCliente não encontrado")
                                continue
                            if not cpf.isnumeric() or len(cpf) != 11:
                                input("\nCPF inválido.\nDigite apenas 11 dígitos.")
                                continue
                            cod_agencia = input("Código da Agência: ")
                            if not Agencia.verificar_agencia(cod_agencia):
                                input("\nAgência não encontrada")
                                continue
                            if not cod_agencia.isnumeric() or len(cod_agencia) != 4:
                                input(
                                    "\nCódigo de agência inválido.\nDigite apenas 4 dígitos."
                                )
                                continue
                            if f"{cpf}_{cod_agencia}" not in Conta.bd_conta:
                                input("\nConta não encontrada")
                                continue
                            Conta.consultar_saldo(cpf, cod_agencia)
                        case 3:
                            print("Extrato\n")
                            cpf = input("CPF do Cliente: ")
                            if not Cliente.verificar_cpf(cpf):
                                input("\nCliente não encontrado")
                                continue
                            if not cpf.isnumeric() or len(cpf) != 11:
                                input("\nCPF inválido.\nDigite apenas 11 dígitos.")
                                continue
                            cod_agencia = input("Código da Agência: ")
                            if not Agencia.verificar_agencia(cod_agencia):
                                input("\nAgência não encontrada")
                                continue
                            if not cod_agencia.isnumeric() or len(cod_agencia) != 4:
                                input(
                                    "\nCódigo de agência inválido.\nDigite apenas 4 dígitos."
                                )
                                continue
                            if f"{cpf}_{cod_agencia}" not in Movimento.bd_movimento:
                                input("\nNenhum movimento encontrado")
                            else:
                                print()
                                Movimento.extrato(cpf, cod_agencia)
                        case 4:
                            print("Exportar em arquivo\n")
                            Conta.exportar()
                        case 5:
                            print("Importar de arquivo\n")
                            Conta.importar()
                        case 0:
                            print()
                        case _:
                            input("\nOpção inexistente")
            case 4:
                opcao_movimento = -1
                while opcao_movimento != 0:
                    os.system("cls")
                    print("Movimento")
                    print("1. Entrada")
                    print("2. Saída")
                    print("3. Exportar em arquivo")
                    print("4. Importar de arquivo")
                    print("0. Voltar")

                    opcao_movimento = int(input("\nOpção número: "))
                    os.system("cls")

                    match opcao_movimento:
                        case 1:
                            print("Entrada\n")
                            cpf = input("CPF do Cliente: ")
                            if not Cliente.verificar_cpf(cpf):
                                input("\nCliente não encontrado")
                                continue
                            if not cpf.isnumeric() or len(cpf) != 11:
                                input("\nCPF inválido.\nDigite apenas 11 dígitos.")
                                continue
                            cod_agencia = input("Código da Agência: ")
                            if not Agencia.verificar_agencia(cod_agencia):
                                input("\nAgência não encontrada")
                                continue
                            if not cod_agencia.isnumeric() or len(cod_agencia) != 4:
                                input(
                                    "\nCódigo de agência inválido.\nDigite apenas 4 dígitos."
                                )
                                continue
                            if f"{cpf}_{cod_agencia}" not in Conta.bd_conta:
                                input("\nConta não encontrada.")
                                continue
                            valor = float(input("\nQuantia a depositar: R$"))
                            movimento = Movimento(cpf, cod_agencia, valor)
                            Movimento.entrada(movimento)
                        case 2:
                            print("Saída\n")
                            cpf = input("CPF do Cliente: ")
                            if not Cliente.verificar_cpf(cpf):
                                input("\nCliente não encontrado")
                                continue
                            if not cpf.isnumeric() or len(cpf) != 11:
                                input("\nCPF inválido.\nDigite apenas 11 dígitos.")
                                continue
                            cod_agencia = input("Código da Agência: ")
                            if not Agencia.verificar_agencia(cod_agencia):
                                input("\nAgência não encontrada")
                                continue
                            if not cod_agencia.isnumeric() or len(cod_agencia) != 4:
                                input(
                                    "\nCódigo de agência inválido.\nDigite apenas 4 dígitos."
                                )
                                continue
                            if f"{cpf}_{cod_agencia}" not in Conta.bd_conta:
                                input("\nConta não encontrada.")
                                continue
                            valor = float(input("\nQuantia a retirar: R$"))
                            movimento = Movimento(cpf, cod_agencia, valor)
                            Movimento.saida(movimento)
                        case 3:
                            print("Exportar em arquivo\n")
                            Movimento.exportar()
                        case 4:
                            print("Importar de arquivo\n")
                            Movimento.importar()
                        case 0:
                            print()
                        case _:
                            print("\nOpção inexistente")
                            input()

            case 0:
                print()
            case _:
                print("\nOpção inexistente")
                input()
    except ValueError:
        print("\nErro! Tente novamente")

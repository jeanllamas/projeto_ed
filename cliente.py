import json


class Cliente:
    bd_cliente = {}

    def __init__(self, nome, cpf, data_nasc, telefone, email):
        self.nome = nome
        self.cpf = cpf
        self.data_nasc = data_nasc
        self.telefone = telefone
        self.email = email

    def dict_cliente(self):
        self.cliente = {
            "nome": self.nome,
            "cpf": self.cpf,
            "data_nasc": self.data_nasc,
            "telefone": self.telefone,
            "email": self.email,
        }
        return self.cliente

    def inserir(self):
        self.bd_cliente[self.cliente["cpf"]] = self.dict_cliente()
        return input("\nCliente registrado com sucesso.")

    @classmethod
    def verificar_cpf(cls, cpf):
        return cpf in cls.bd_cliente

    def alterar(self):
        self.update_cliente = self.dict_cliente()
        self.bd_cliente[self.update_cliente["cpf"]].update(self.update_cliente)
        return input("\nDados do cliente foram atualizados.")

    @classmethod
    def consultar(cls, cpf):
        cpf_formatado = f"{cls.bd_cliente[cpf]["cpf"][:3]}.{cls.bd_cliente[cpf]["cpf"][3:6]}.{cls.bd_cliente[cpf]["cpf"][6:9]}-{cls.bd_cliente[cpf]["cpf"][9:]}"
        dia = cls.bd_cliente[cpf]["data_nasc"][:2]
        mes = cls.bd_cliente[cpf]["data_nasc"][2:4]
        ano = cls.bd_cliente[cpf]["data_nasc"][4:]
        data_formatada = f"{dia}/{mes}/{ano}"
        telefone_formatado = f"({cls.bd_cliente[cpf]["telefone"][:2]}) {cls.bd_cliente[cpf]["telefone"][2:7]}-{cls.bd_cliente[cpf]["telefone"][7:]}"

        print(f"\nNome: {cls.bd_cliente[cpf]["nome"]}")
        print(f"CPF: {cpf_formatado}")
        print(f"Data de Nascimento: {data_formatada}")
        print(f"Telefone: {telefone_formatado}")
        print(f"E-mail: {cls.bd_cliente[cpf]["email"]}")
        input()

    @classmethod
    def remover(cls, cpf):
        cls.bd_cliente.pop(cpf)
        input("\nCliente removido.")

    @classmethod
    def exportar(cls):
        with open("clientes.json", "w") as arquivo:
            json.dump(cls.bd_cliente, arquivo, indent=4)
        input("Dados exportados com sucesso.")

    @classmethod
    def importar(cls):
        try:
            with open("clientes.json", "r") as arquivo:
                cls.bd_cliente = json.load(arquivo)
            input("Dados importados com sucesso.")
        except FileNotFoundError:
            input("O arquivo 'clientes.json' não foi encontrado.")

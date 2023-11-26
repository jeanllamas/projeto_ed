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
        return input(self.bd_cliente)

    @classmethod
    def verificar_cpf(cls, cpf):
        if cpf in cls.bd_cliente:
            return True

    def alterar(self):
        self.update_cliente = self.dict_cliente()
        self.bd_cliente[self.update_cliente["cpf"]].update(self.update_cliente)
        return input(self.bd_cliente)

    @classmethod
    def consultar(cls, cpf):
        input(f"{cls.bd_cliente[cpf]}\n")

    @classmethod
    def remover(cls, cpf):
        cls.bd_cliente.pop(cpf)

    @classmethod
    def salvar_no_arquivo(cls):
        with open("clientes.json", "w") as arquivo:
            json.dump(cls.bd_cliente, arquivo, indent=2, default=int)

    @classmethod
    def carregar_do_arquivo(cls):
        try:
            with open("clientes.json", "r") as arquivo:
                cls.bd_cliente = {int(k): v for k, v in json.load(arquivo).items()}
            input("Dados carregados com sucesso.")
        except FileNotFoundError:
            input("O arquivo 'clientes.json' não foi encontrado.")

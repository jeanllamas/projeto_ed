import json


class Conta:
    bd_conta = {}

    def __init__(self, cpf, cod_agencia, tipo, limite_especial):
        self.cpf = cpf
        self.cod_agencia = cod_agencia
        self.tipo = tipo
        self.limite_especial = limite_especial
        self.saldo = 0

    def dict_conta(self):
        self.conta = {
            "cpf": self.cpf,
            "cod_agencia": self.cod_agencia,
            "tipo": self.tipo,
            "limite_especial": self.limite_especial,
            "saldo": self.saldo,
        }
        return self.conta

    def inserir(self):
        chave = f"{self.cpf}_{self.cod_agencia}"
        self.bd_conta[chave] = self.dict_conta()
        return input("\nConta registrada com sucesso.")

    @classmethod
    def consultar_saldo(cls, cpf, cod_agencia):
        chave = f"{cpf}_{cod_agencia}"
        input(f"\nSaldo da conta: R${cls.bd_conta[chave]["saldo"]:,.2f}")

    @classmethod
    def exportar(cls):
        with open("contas.json", "w") as arquivo:
            json.dump(cls.bd_conta, arquivo, indent=4)
        input("Dados exportados com sucesso.")

    @classmethod
    def importar(cls):
        try:
            with open("contas.json", "r") as arquivo:
                cls.bd_conta = json.load(arquivo)
            input("Dados importados com sucesso.")
        except FileNotFoundError:
            input("O arquivo 'contas.json' não foi encontrado.")

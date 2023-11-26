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
        return input(self.bd_conta)

    @classmethod
    def consultar_saldo(cls, cpf, cod_agencia):
        chave = f"{cpf}_{cod_agencia}"
        input(cls.bd_conta[chave]["saldo"])

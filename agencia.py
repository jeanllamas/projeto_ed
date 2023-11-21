class Agencia:
    bd_agencia = {}

    def __init__(self, nome, cnpj, num_agencia, num_banco, endereco, telefone, email):
        self.nome = nome
        self.cnpj = cnpj
        self.num_agencia = num_agencia
        self.num_banco = num_banco
        self.endereco = endereco
        self.telefone = telefone
        self.email = email

    def dict_agencia(self):
        self.agencia = {
            "nome": self.nome,
            "cnpj": self.cnpj,
            "num_agencia": self.num_agencia,
            "num_banco": self.num_banco,
            "endereco": self.endereco,
            "telefone": self.telefone,
            "email": self.email,
        }
        return self.agencia

    def inserir(self):
        self.bd_agencia[self.agencia["cnpj"]] = self.dict_agencia()
        return input(self.bd_agencia)

    @classmethod
    def verificar_cnpj(cls, cnpj):
        if cnpj in cls.bd_agencia:
            return True

    def alterar(self):
        self.update_agencia = self.dict_agencia()
        self.bd_agencia[self.update_agencia["cnpj"]].update(self.update_agencia)
        return input(self.bd_agencia)

    @classmethod
    def consultar(cls, cnpj):
        input(f"{cls.bd_agencia[cnpj]}\n")

    @classmethod
    def remover(cls, cnpj):
        cls.bd_agencia.pop(cnpj)

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

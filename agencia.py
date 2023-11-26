class Agencia:
    bd_agencia = {}

    def __init__(self, nome, cod_agencia, telefone, email):
        self.nome = nome
        self.cod_agencia = cod_agencia
        self.telefone = telefone
        self.email = email

    def dict_agencia(self):
        self.agencia = {
            "nome": self.nome,
            "cod_agencia": self.cod_agencia,
            "telefone": self.telefone,
            "email": self.email,
        }
        return self.agencia

    def inserir(self):
        self.bd_agencia[self.agencia["cod_agencia"]] = self.dict_agencia()
        return input(self.bd_agencia)

    @classmethod
    def verificar_agencia(cls, cod_agencia):
        if cod_agencia in cls.bd_agencia:
            return True

    def alterar(self):
        self.update_agencia = self.dict_agencia()
        self.bd_agencia[self.update_agencia["cod_agencia"]].update(self.update_agencia)
        return input(self.bd_agencia)

    @classmethod
    def consultar(cls, cod_agencia):
        input(f"{cls.bd_agencia[cod_agencia]}\n")

    @classmethod
    def remover(cls, cod_agencia):
        cls.bd_agencia.pop(cod_agencia)

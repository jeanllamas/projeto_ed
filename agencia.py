import json


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
        return cod_agencia in cls.bd_agencia

    def alterar(self):
        self.bd_agencia[self.cod_agencia].update(self.dict_agencia())
        return self.bd_agencia

    @classmethod
    def consultar(cls, cod_agencia):
        # input(f"{cls.bd_agencia[cod_agencia]}\n")
        agencia = cls.bd_agencia.get(cod_agencia)
        if agencia:
            input(f"Agência {cod_agencia}:\n{agencia}")
        else:
            input(f"Agência com código {cod_agencia} não encontrada.")

    @classmethod
    def remover(cls, cod_agencia):
        cls.bd_agencia.pop(cod_agencia, None)

    @classmethod
    def salvar_no_arquivo(cls):
        with open("agencias.json", "w") as arquivo:
            json.dump(cls.bd_agencia, arquivo, indent=2, default=int)

    @classmethod
    def carregar_do_arquivo(cls):
        try:
            with open("agencias.json", "r") as arquivo:
                cls.bd_agencia = {int(k): v for k, v in json.load(arquivo).items()}
            input("Dados carregados com sucesso.")
        except FileNotFoundError:
            input("O arquivo 'agencias.json' não foi encontrado.")

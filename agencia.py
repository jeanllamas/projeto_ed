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
        return input("\nAgência registrada com sucesso.")

    @classmethod
    def verificar_agencia(cls, cod_agencia):
        return cod_agencia in cls.bd_agencia

    def alterar(self):
        self.bd_agencia[self.cod_agencia].update(self.dict_agencia())
        return input("\nDados da agência foram atualizados.")

    @classmethod
    def consultar(cls, cod_agencia):
        telefone_formatado = f"({cls.bd_agencia[cod_agencia]["telefone"][:2]}) {cls.bd_agencia[cod_agencia]["telefone"][2:7]}-{cls.bd_agencia[cod_agencia]["telefone"][7:]}"

        print(f"\nNome: {cls.bd_agencia[cod_agencia]["nome"]}")
        print(f"Código de Agência: {cls.bd_agencia[cod_agencia]["cod_agencia"]}")
        print(f"Telefone: {telefone_formatado}")
        print(f"E-mail: {cls.bd_agencia[cod_agencia]["email"]}")
        input()

    @classmethod
    def remover(cls, cod_agencia):
        cls.bd_agencia.pop(cod_agencia)
        input("\nAgência removida.")

    @classmethod
    def exportar(cls):
        with open("agencias.json", "w") as arquivo:
            json.dump(cls.bd_agencia, arquivo, indent=4)
        input("Dados exportados com sucesso.")

    @classmethod
    def importar(cls):
        try:
            with open("agencias.json", "r") as arquivo:
                cls.bd_agencia = json.load(arquivo)
            input("Dados importados com sucesso.")
        except FileNotFoundError:
            input("O arquivo 'agencias.json' não foi encontrado.")

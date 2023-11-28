from conta import Conta
from datetime import datetime
import json


class Movimento:
    bd_movimento = {}

    def __init__(self, cpf, cod_agencia, valor):
        self.cpf = cpf
        self.cod_agencia = cod_agencia
        self.valor = valor

    def entrada(self):
        chave = f"{self.cpf}_{self.cod_agencia}"
        saldo = Conta.bd_conta[chave]["saldo"]

        saldo_novo = saldo + self.valor

        Conta.bd_conta[chave]["saldo"] = saldo_novo

        data = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

        if chave not in self.bd_movimento:
            self.bd_movimento[chave] = {}

        self.bd_movimento[chave][data] = {
            "data": data,
            "operacao": "Entrada",
            "valor": self.valor,
            "saldo_anterior": saldo,
            "saldo": saldo_novo,
        }

    def saida(self):
        chave = f"{self.cpf}_{self.cod_agencia}"
        saldo = Conta.bd_conta[chave]["saldo"]
        limite_especial = Conta.bd_conta[chave]["limite_especial"]

        saldo_novo = saldo - self.valor

        if chave not in self.bd_movimento:
            self.bd_movimento[chave] = {}

        if saldo_novo >= limite_especial:
            Conta.bd_conta[chave]["saldo"] = saldo_novo
            data = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            self.bd_movimento[chave][data] = {
                "data": data,
                "operacao": "Saída",
                "valor": self.valor,
                "saldo_anterior": saldo,
                "saldo": saldo_novo,
            }
        else:
            input("\nSaldo insuficiente")

    @classmethod
    def extrato(cls, cpf, cod_agencia):
        chave = f"{cpf}_{cod_agencia}"

        for data, movimento in cls.bd_movimento[chave].items():
            operacao = movimento["operacao"]
            valor = movimento["valor"]
            saldo_anterior = movimento["saldo_anterior"]
            saldo = movimento["saldo"]

            valor_formatado = f"R${valor:,.2f}"
            saldo_anterior_formatado = f"R${saldo_anterior:,.2f}"
            saldo_formatado = f"R${saldo:,.2f}"

            print(
                f"{data} - {operacao}: {valor_formatado} - Saldo antes: {saldo_anterior_formatado} - Saldo depois: {saldo_formatado}"
            )
        input()

    @classmethod
    def exportar(cls):
        with open("movimentos.json", "w") as arquivo:
            json.dump(cls.bd_movimento, arquivo, indent=4)
        input("Dados exportados com sucesso.")

    @classmethod
    def importar(cls):
        try:
            with open("movimentos.json", "r") as arquivo:
                cls.bd_movimento = json.load(arquivo)
            input("Dados importados com sucesso.")
        except FileNotFoundError:
            input("O arquivo 'movimentos.json' não foi encontrado.")

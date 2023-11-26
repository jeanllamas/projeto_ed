from conta import Conta
from datetime import datetime


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

        if saldo_novo >= limite_especial:
            Conta.bd_conta[chave]["saldo"] = saldo_novo
        else:
            print("Saldo insuficiente")

        data = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

        if chave not in self.bd_movimento:
            self.bd_movimento[chave] = {}

        self.bd_movimento[chave][data] = {
            "data": data,
            "operacao": "Saída",
            "valor": self.valor,
            "saldo_anterior": saldo,
            "saldo": saldo_novo,
        }

    @classmethod
    def extrato(cls, cpf, cod_agencia):
        chave = f"{cpf}_{cod_agencia}"

        for data, movimento in cls.bd_movimento[chave].items():
            operacao = movimento["operacao"]
            valor = movimento["valor"]
            saldo_anterior = movimento["saldo_anterior"]
            saldo = movimento["saldo"]

            print(
                f"{data} - {operacao}: R${valor} - Saldo antes: R${saldo_anterior} - Saldo depois: R${saldo}"
            )
        input()

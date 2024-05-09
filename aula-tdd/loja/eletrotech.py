from datetime import date

class FuncionarioEletroTech:
    def __init__(self, nome, data_nascimento, salario, cargo):
        self._nome = nome
        self._data_nascimento = data_nascimento
        self._salario = salario
        self._cargo = cargo

    @property
    def nome(self):
        return self._nome

    def idade(self): # "27/03/1983"
        data_nasc_em_partes = self._data_nascimento.split('/')
        ano_nasc = int(data_nasc_em_partes[-1])
        ano_atual = date.today().year
        return ano_atual - ano_nasc

    @property
    def salario(self):
        return self._salario

    def cargo(self):
        return self._salario

    # PRIMEIRO CALCULA PREMIAÇÃO
    def calcular_premiacao_por_desempenho(self):  # Método para calcular o bônus do funcionário
        valor = self._salario * 0.10  # Calcula o valor do bônus (10% do salário)
        if valor >= 1000:  # Verifica se o valor do bônus é maior que 1000
            valor = 0
        return valor  # Retorna o valor da premiacao

    def __str__(self):
        """Função que retorna as informações completas do objeto"""
        return f'FuncionarioEletroTech({self._nome}, {self._data_nascimento}, {self._salario}, {self._cargo})'
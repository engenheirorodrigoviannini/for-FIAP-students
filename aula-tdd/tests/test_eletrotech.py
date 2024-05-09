import pytest
from pytest import mark
from loja.eletrotech import FuncionarioEletroTech

class TestClassFuncionarioEletroTech:
    def test_idade_27_marco_1983_retorna_41(self):
        # GIVEN (contexto)
        entrada = '27/03/1983'
        esperado = 41

        funcionario = FuncionarioEletroTech('Teste', entrada, 0, 'cargo')
        # WHEN (quando)
        resultado = funcionario.idade()

        # THEN (resultado)
        assert resultado == esperado # assert é um metodo do pytest que verifica se é verdade ou não

    @mark.calcular_premiacao_por_desempenho
    def test_calcular_premiacao_salario_1000_recebe_100(self):
        entrada_salario = 1000  # Given
        esperado = 100
        funcionario_teste = FuncionarioEletroTech("Teste", '11/05/2000', entrada_salario, 'cargo')
        resultado = funcionario_teste.calcular_premiacao_por_desempenho()  # When

        assert resultado # Then

    @mark.calcular_premiacao_por_desempenho
    def test_calcular_premiacao_salario_100000_recebe_100(self):
        entrada_salario = 100000  # Given
        esperado = 100
        funcionario_teste = FuncionarioEletroTech("Teste", '11/05/2000', entrada_salario, 'cargo')
        resultado = funcionario_teste.calcular_premiacao_por_desempenho()  # When

        assert resultado  # Then
from loja.eletrotech import FuncionarioEletroTech

# rodrigo = FuncionarioEletroTech('rodrigo', "27/03/1983", 10000, "Desenvolvedor")
# print(rodrigo.idade())

#Teste Automatizado
def teste_idade(): #teste unitario
    func_teste = FuncionarioEletroTech('teste', "27/03/1994", 10000, "Desenvolvedor")
    print(f'Teste >>> {func_teste}')

teste_idade()
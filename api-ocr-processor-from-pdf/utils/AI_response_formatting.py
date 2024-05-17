import re

def extract_fields(text):
    # Remover números seguidos de "-" e " "
    response = re.sub(r'\d+-\s+', '', text)

    # Dividir o texto em linhas
    linhas = response.strip().split('\n')

    # Lista para armazenar os valores
    valores = []

    # Iterar sobre as linhas e extrair os valores
    for linha in linhas:
        valor = linha.split(': ')[1]
        valores.append(valor)

    # Variáveis para armazenar os valores
    nome = ''
    cpf_cnpj = ''
    endereco = ''
    cep = ''
    tipo_fornecimento = ''
    leitura_anterior = ''
    leitura_atual = ''
    n_dias_entre_leituras = ''
    proxima_leitura = ''
    total_a_pagar = ''
    info_fiscais = ''
    kWh = ''
    data_vencimento = ''

    # Percorrendo a lista e salvando os itens nas variáveis correspondentes
    for i, item in enumerate(valores):
        if i == 0:
            nome = item
        elif i == 1:
            cpf_cnpj = item
        elif i == 2:
            endereco = item
        elif i == 3:
            cep = item
        elif i == 4:
            tipo_fornecimento = item
        elif i == 5:
            leitura_anterior = item
        elif i == 6:
            leitura_atual = item
        elif i == 7:
            n_dias_entre_leituras = item
        elif i == 8:
            proxima_leitura = item
        elif i == 9:
            total_a_pagar = item
        elif i == 10:
            info_fiscais = item
        elif i == 11:
            kWh = item
        elif i == 12:
            data_vencimento = item

    # Montando a lista de campos
    fields = [{
        'nome': nome,
        'cpf_cnpj': cpf_cnpj,
        'endereco': endereco,
        'cep': cep,
        'tipo_fornecimento': tipo_fornecimento,
        'leitura_anterior': leitura_anterior,
        'leitura_atual': leitura_atual,
        'n_dias_entre_leituras': n_dias_entre_leituras,
        'proxima_leitura': proxima_leitura,
        'total_a_pagar': total_a_pagar,
        'info_fiscais': info_fiscais,
        'kWh': kWh,
        'data_vencimento': data_vencimento,
    }]

    return fields
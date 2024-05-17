import json
from openai import OpenAI

def send_message_to_gpt4(text, prompt):
    response = None
    # Lê a chave da API do arquivo de configuração
    with open('config') as config_file:
        config_data = json.load(config_file)
        openai_api_key = config_data.get('openai_api_key')

    client = OpenAI(api_key=openai_api_key)

    # Envie a mensagem para o GPT-4
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "user", "content": text},                   # Enviamos o texto fornecido
            {"role": "assistant", "content": prompt},           # O prompt continua sendo fornecido pelo usuário
        ],
        temperature=0,          # Aumentar a temperatura para tornar as respostas mais diversificadas
        max_tokens=800,         # Reduzir o número máximo de tokens para limitar o tamanho das respostas
        top_p=0,                # Aumentar o valor de 'top_p' para gerar respostas mais diversificadas
        frequency_penalty=0,    # Aumentar o valor de 'frequency_penalty' para evitar respostas repetitivas
        presence_penalty=1,     # Ajustar o valor de 'presence_penalty' para equilibrar a geração de respostas,
        stop=None               # stop=["."] Parar a geração de texto quando encontrar um ponto final
    )

    # Obtenha a resposta gerada pelo GPT-4
    gpt4_response = response.choices[0].message.content

    return gpt4_response

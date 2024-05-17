from fastapi import FastAPI, UploadFile, File

from utils.AI_response_formatting import extract_fields
from utils.chatgpt import send_message_to_gpt4
from utils.ocr_extraction import OCRProcessor
import os

app = FastAPI()
ocr_processor = OCRProcessor()

@app.get("/")
async def root():
    """
        Rota raiz. Retorna a URL da documentação.
    """
    return {"url": "http://127.0.0.1:8000/docs"}


@app.post("/extract-text-from-pdf/")
async def extract_text_from_pdf(pdf_file: UploadFile = File(...)):
    """
       Rota para extrair texto de um arquivo PDF.
    """

    # Salve o arquivo temporariamente
    with open(pdf_file.filename, "wb") as buffer:
        buffer.write(pdf_file.file.read())

    # Extraia o texto do PDF usando o OCRProcessor
    text = ocr_processor.extract_text_from_pdf(pdf_file.filename)

    # ChatGPT
    answers = f'Leia o texto referente a uma conta de luz, e extraia somente as informações solicitadas: 1-nome completo do cliente; 2-numero de cpf ou cnpj; 3-endereço completo; 4-cep; 5-Tipo de fornecimento; 6-Datas de leitura anterior; 7-Datas de leitura atual; 8-Número de dias entre leituras; 9-Próxima leitura; 10-Total a pagar; 11-Informações fiscais; 12-Consumo de kWh; 13-Data de vencimento.'
    response = send_message_to_gpt4(text, answers)
    print(f'return_read_script_1 >>> {response}')

    # AI Response Formatting
    json = extract_fields(response)

    # Remova o arquivo temporário
    os.remove(pdf_file.filename)

    return {"fields": json}




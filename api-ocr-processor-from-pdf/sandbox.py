from utils.AI_response_formatting import extract_fields
from utils.chatgpt import send_message_to_gpt4
from utils.ocr_extraction import OCRProcessor

class DocumentProcessor:
    def __init__(self):
        self.ocr_processor = OCRProcessor()

    def process_document(self, pdf_path):
        # Extrai texto do PDF usando OCR
        ocr_text = self.ocr_processor.extract_text_from_pdf(pdf_path)

        # Defina suas perguntas e respostas para o ChatGPT
        questions = 'Leia o texto referente a uma conta de luz, e extraia somente as informações solicitadas: 1-nome completo do cliente; 2-numero de cpf ou cnpj; 3-endereço completo; 4-cep; 5-Tipo de fornecimento; 6-Datas de leitura anterior; 7-Datas de leitura atual; 8-Número de dias entre leituras; 9-Próxima leitura; 10-Total a pagar; 11-Informações fiscais; 12-Consumo de kWh; 13-Data de vencimento.'

        # Envie a pergunta e obtenha a resposta do ChatGPT
        response = send_message_to_gpt4(ocr_text, questions)

        # Formate a resposta em um formato de JSON com campos específicos
        extracted_fields = extract_fields(response)

        return {"fields": extracted_fields}

if __name__ == "__main__":
    # Inicialize o processador de documentos
    document_processor = DocumentProcessor()

    # Caminho para o arquivo PDF
    file_path = "files/enel_ficticia.pdf"

    # Processar o documento e obter os campos extraídos
    extracted_fields = document_processor.process_document(file_path)

    # Imprimir os campos extraídos
    print(extracted_fields)




from paddleocr import PaddleOCR

# Inicializa o objeto PaddleOCR
ocr = PaddleOCR()

class OCRProcessor:
    def __init__(self, use_angle_cls=True, lang='en'):
        self.use_angle_cls = use_angle_cls
        self.lang = lang

    # Função para extrair texto OCR de um PDF
    def extract_text_from_pdf(self, pdf_path):
        # Use o método `ocr.ocr()` para extrair texto de uma imagem
        extract_ocr = ocr.ocr(pdf_path, cls=self.use_angle_cls)  # Removido o argumento `lang`

        # Concatene todas as palavras detectadas em uma única string
        result = ''
        for line in extract_ocr:
            for word in line:
                result += word[1][0] + ' '  # O índice 0 representa o texto da palavra
            result += '\n'  # Adicione uma nova linha após cada linha de texto
        return result



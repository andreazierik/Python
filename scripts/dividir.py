from PyPDF2 import PdfFileWriter, PdfFileReader
import time

def dividirPDF():
  caminho = input("Digite o caminho do arquivo para dividir: ")
  separados = 'C:\\Projetos\\Python\\documentos\\Artigos_Separados'

  pdf_reader = PdfFileReader(caminho)
  pdf_writer = PdfFileWriter()

  for cada_pagina in range(pdf_reader.getNumPages()):
    pdf_writer.addPage(pdf_reader.getPage(cada_pagina))

    if cada_pagina % 2 == 1 or (pdf_reader.getNumPages() - 1) == cada_pagina:
      novos_arquivos = f'{separados}{cada_pagina}.pdf'
      with open(novos_arquivos, 'wb') as arquivo:
        pdf_writer.write(arquivo)
        print("Dividindo o arquivo " + caminho + ", em vários arquivos com duas páginas cada")
      pdf_writer = PdfFileWriter()
      time.sleep(2)
      print("Arquivos dividos!")
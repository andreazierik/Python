# CONVERTER PDF PARA WORD.
# NECESSÁRIO RODAR EM UMA MÁQUINA ONDE O WORD (OFFICE) ESTÁ INSTALADO. UTILIZAÇÃO DE BIBLIOTECAS DO WORD PARA A CONVERSÃO

# pip install pywin32

import win32com.client
import os
import time

def pdfToWord():
    word=win32com.client.Dispatch("word.Application")
    word.visible=0

    doc_pdf= input("Selecione o arquivo que será convertido: ")
    input_file=os.path.abspath(doc_pdf)

    wb=word.Documents.Open(input_file)
    outpub_file=os.path.abspath(doc_pdf[0:-4] + "".format())
    wb.SaveAs2(outpub_file,FileFormat=16)
    print("Convertendo o arquivo para .docx")
    time.sleep(2)
    print("PDF para DOCX finalizado!")
	
    wb.Close()

    word.Quit()

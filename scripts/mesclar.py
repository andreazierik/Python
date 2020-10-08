from PyPDF2 import PdfFileWriter, PdfFileReader, PdfFileMerger
import time

def mesclarPDF():

  documento1 = input("Digite o caminho do arquivo 1: ")
  documento2 = input("Digite o caminho do arquivo 2: ")

  caminhos = [documento1,documento2]

  documentos_unificados = 'C:\\Projetos\\Python\\documentos\\Artigos_Unificados.pdf'
  
  merger = PdfFileMerger(caminhos)
  
  for documentos in caminhos:
    merger.append(PdfFileReader(documentos, 'rb'))
  
  merger.write(documentos_unificados)
  print("Mesclando os arquivos " + documento1 + " e " + documento2 + "!")
  time.sleep(2)
  print("Arquivos mesclados!")

#mesclar = mesclarPDF()
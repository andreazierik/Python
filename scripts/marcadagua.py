from pdfrw import PdfReader, PdfWriter, PageMerge
import time

def marcaDagua():
    caminho = input("Caminho do arquivo original: ")
    marcadagua = input("Caminho do aquivo marca D'água: ")

    output_file = "C:\\projetos\\python\\documentos\\Artigo_marcadagua.pdf"

    # define the reader and writer objects
    reader_input = PdfReader(caminho)
    writer_output = PdfWriter()
    watermark_input = PdfReader(marcadagua)
    watermark = watermark_input.pages[0]

    # go through the pages one after the next
    for current_page in range(len(reader_input.pages)):
        merger = PageMerge(reader_input.pages[current_page])
        merger.add(watermark).render()

    # write the modified content to disk
    print("Gerando um novo arquivo com marca d'água")
    writer_output.write(output_file, reader_input)
    time.sleep(2)
    print("Arquivo gerado!")
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
import io
import time

def pdf2txt(inPDFfile, outTXTFile):
    inFile = open(inPDFfile, 'rb')
    resMgr = PDFResourceManager()
    retData = io.StringIO()
    TxtConverter = TextConverter(resMgr, retData, laparams=LAParams())
    interpreter = PDFPageInterpreter(resMgr, TxtConverter)

    for page in PDFPage.get_pages(inFile):
        interpreter.process_page(page)

    txt = retData.getvalue()

    with open(outTXTFile, 'w', encoding='utf8') as f:
        print("Convertendo PDF para TXT.\n")
        f.write(txt)
        time.sleep(2)
        print("Arquivo convertido para TXT!\n")

inPDFfile = 'C:\\projetos\\python\\documentos\\artigo1.pdf'
outTXTFile = 'C:\\projetos\\python\\documentos\\artigo1.txt'
pdf2txt(inPDFfile, outTXTFile)
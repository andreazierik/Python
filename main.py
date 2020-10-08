import scripts.marcadagua
import scripts.mesclar
import scripts.dividir
import scripts.pdfparaword

print('*'*60)
print("\n")
print("1: Verificar quantas vezes aparece um determinado termo em um arquivo pdf")
print("2: Verificar quantas vezes aparecem a combinação de duas palavras em um arquivo pdf")
print("3: Inserir uma marca d’agua em vários arquivos pdf")
print("4: Realizar um merge (junção) de dois ou mais arquivos em pdf")
print("5: Realizar a separação de 2 em 2 páginas em um arquivo em pdf")
print("6: Realizar a conversão de vários arquivos em pdf para word (lote).")
print("7: Encerrar laço de repetição")
print("\n")
print('*'*60)
print("\n")

choice = ""

while True:
    try:
        choice = int(input('Escolha um número da lista a cima: '))
    except:
        print("Caractere invalido!\n")
    if choice == 1:
        print("Em desenvolvimento!\n")
    elif choice == 2:
        print("Em desenvolvimento!\n")
    elif choice == 3:
        scripts.marcadagua.marcaDagua()
    elif choice == 4:
        scripts.mesclar.mesclarPDF()
        print("\n")
    elif choice == 5:
        scripts.dividir.dividirPDF()
        print("\n")
    elif choice == 6:
        scripts.pdfparaword.pdfToWord()
        print("\n")
    elif choice == 7:
        print("SAINDO!\n")
        break
    else:
        print("ERRO: Escolha um número da lista a cima!\n")

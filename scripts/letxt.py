def contador(filename, listapalavras):
    try:
        file = open(filename, "r", encoding='utf8')
        read = file.readlines()
        file.close()
        for word in listapalavras:
            lower = word.lower()
            count = 0
            for sentence in read:
                line = sentence.split()
                for each in line:
                    line2 = each.lower()
                    line2 = line2.strip("!@#$%^&*(()_+=")
                    if lower == line2:
                        count += 1
            print(lower, ":", count)
    except FileExistsError:
        print("Arquivo não encontrado!")

#contador("C:\\projetos\\python\\documentos\\artigo1.txt", ['engenharia'])
contador("C:\\projetos\\python\\documentos\\artigo1.txt", [input("Palavras a ser encontrada: ")])
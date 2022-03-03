from sys import argv

script, filename = argv
# para abrir um arquivo de nome .txt usamos open
txt = open(filename)

print(f"Here's your file {filename}:")
# Para imprimir o conteúdo de um arquivo usa o
# comando neste caso print(txt.read())
print(txt.read())

print("Type the filename again:")
# input vc coloca o nome do texto criado e salvo .txt
file_again = input("nome do texto ")
# para abrir um arquivo de nome .txt usamos open
txt_again = open(file_again)
# Para imprimir o conteúdo de um arquivo usa o
# comando neste caso print(txt_again.read())
print(txt_again.read())
txt_again.close()
# read Lê o conteúdo do arquivo. Você pode atribuir o resultado a uma variável.

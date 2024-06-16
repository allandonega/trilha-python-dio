path_relativo_arquivo="trilha-python-dio/05 - Manipulação de arquivos"
nome_arquivo="lorem.txt"

# Lembre-se de alterar o caminho do arquivo, para o caminho completo da sua máquina!

#arquivo = open(path_relativo_arquivo + "/"+ nome_arquivo, "r")
#print(arquivo.read())
#arquivo.close()


path_completo_arquivo = "/Users/allandonega/workspace/scripts/src-scripts/trilha-python-dio/05 - Manipulação de arquivos"
arquivo = open(path_completo_arquivo + "/"+ nome_arquivo, "r")
print(arquivo.readline())
arquivo.close()

arquivo = open(path_completo_arquivo + "/"+ nome_arquivo, "r")

# tip
while len(linha := arquivo.readline()):
    print(f"Iterando:, {linha}")

arquivo.close()

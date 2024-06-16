from datetime import datetime
path_relativo_arquivo="trilha-python-dio/05 - Manipulação de arquivos"
path_completo_arquivo = "/Users/allandonega/workspace/scripts/src-scripts/trilha-python-dio/05 - Manipulação de arquivos"
nome_arquivo="operacao_escrita.txt"
arq = path_completo_arquivo + "/" + nome_arquivo 
arquivo = open(path_completo_arquivo + "/"+ nome_arquivo, "w")


arquivo.write("Escrevendo dados em um novo arquivo.")
arquivo.writelines(["\n",str(datetime.today()),"\n", "escrevendo", "\n", "um", "\n", "novo", "\n", "texto"])
print(f"Fechando o arquivo {nome_arquivo}")
arquivo.close()

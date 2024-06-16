import os
import shutil
from pathlib import Path

ROOT_PATH = Path(__file__).parent
print(f"ROOT_PATH: {ROOT_PATH}")

print(f"Criando novo diretorio")
os.mkdir(ROOT_PATH / "novo-diretorio")

print(f"Escrevendo arquivo novo.txt [ w ]")
arquivo = open(ROOT_PATH / "novo.txt", "w")
arquivo.close()

print(f"Renomeando o arquivo novo.txt para alterado.txt")
os.rename(ROOT_PATH / "novo.txt", ROOT_PATH / "alterado.txt")

print(f"Removendo o arquivo alterado.txt")
os.remove(ROOT_PATH / "alterado.txt")

print(f"Movendo o arquivo ROOT_PATH / novo.txt para ROOT_PATH / novo-diretorio / novo.txt")
shutil.move(ROOT_PATH / "novo.txt", ROOT_PATH / "novo-diretorio" / "novo.txt")

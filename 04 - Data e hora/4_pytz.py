from datetime import datetime

import pytz

data = datetime.now(pytz.timezone("Europe/Oslo"))
data2 = datetime.now(pytz.timezone("America/Sao_Paulo"))

print(data)
print(data2)

############################
# Criar ambiente virtual
# para executar o pytz
############################
# python3 -m venv .env
#  source .env/bin/activate
#  pip install pytz

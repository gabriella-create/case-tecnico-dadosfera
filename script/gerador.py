import pandas as pd
import random
from faker import Faker

fake = Faker(['pt_BR'])

def gerar_dados_case(n=100000):
    data = []
    for i in range(n):
        data.append({
            "id": i,
            "produto": f"Produto {fake.word()}",
            "descricao": f"Descrição completa do item {fake.sentence()}. Material de {fake.word()}.",
            "preco": round(random.uniform(10, 5000), 2),
            "data": fake.date_this_year()
        })
    df = pd.DataFrame(data)
    df.to_csv("dados_ecommerce.csv", index=False)
    print("Base de 100 mil registros criada!")

if _name_ == "_main_":
    gerar_dados_case()

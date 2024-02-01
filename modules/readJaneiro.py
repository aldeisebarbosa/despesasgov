# importando as bibliotecas necessárias para o projeto
import pandas as pd #para ler e visualizar os dados
import numpy as np 

# le"ndo os csv's

dados=pd.read_csv('despesasgov\janeiro.csv')
print(dados.head())

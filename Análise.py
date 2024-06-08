
#importanto  bibliotecas 

import streamlit as st 
import pandas as pd
import matplotlib 
import seaborn 

#carregando o arquivo 

base = pd.read_csv("Vendas.csv")
base.head()
base.dtypes
base.info()

# 1- começando as analises 
# 2- Analisando o produto mais caro

produtos_mais_vendidos = base.groupby('sku')['quantity'].sum().sort_values(ascending= False)
produtos_mais_vendidos = produtos_mais_vendidos.head(5)
produtos_mais_vendidos.head(5)

from pandas import value_counts


produtos_mais_vendidos = base.groupby('sku')['revenue'].sum().sort_values(ascending= False)
produtos_mais_caros = produtos_mais_vendidos.head(5)
produtos_mais_caros.head(5)

total_de_vendas = base.revenue.sum()
total_de_vendas.head()

receita_media = base.groupby('order_id')['revenue'].sum()
receita_media = receita_media.mean()
receita_media.head()

preço_medio = base.groupby('sku')['unit_price'].mean()
print(f" O preço médio é: ${preço_medio}")

base['order_date'] = pd.to_datetime(base['order_date'])
base['order_moth'] = base['order_date'].dt.to_period ('M')
Receita_mensal = base.groupby('order_moth')['revenue'].sum()


melhor_cor= base[['color','size']].value_counts().head(5)
melhor_cor.head ()

pedidos_por_clientes = base['order_id'].value_counts()
pedido_unico = pedidos_por_clientes [pedidos_por_clientes == 1]
pedido_unico.head()

base.describe()


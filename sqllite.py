import sqlite3
import pandas as pd
import streamlit as st

con = sqlite3.connect('cap12_dsa.db')
cursor = con.cursor()

query = 'SELECT * FROM tb_vendas_dsa'
cursor.execute(query)

dados = cursor.fetchall()

df = pd.DataFrame(dados,columns=['ID_Pedido',
                                 'ID_Cliente',
                                 'Nome_Produto',
                                 'Valor_Unitario',
                                 'Unidades_Vendidas',
                                 'Custo'])

st.set_page_config(page_title=" Portfolio de Analises de dados", layout="wide")

st.dataframe(df)
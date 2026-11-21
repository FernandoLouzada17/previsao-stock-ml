import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from sklearn.linear_model import LinearRegression
import datetime

# 1. Configuração da Página
st.set_page_config(page_title="Previsão de Stock Inteligente", layout="wide")
st.title("🤖 Dashboard de Previsão de Procura (Machine Learning)")
st.markdown("Antecipe ruturas de stock utilizando algoritmos preditivos baseados no histórico de vendas.")

# 2. Carregar os Dados
@st.cache_data
def carregar_dados():
    df = pd.read_csv('historico_vendas.csv')
    df['data'] = pd.to_datetime(df['data'])
    return df

df = carregar_dados()

# 3. Menu Lateral (Filtros)
st.sidebar.header("Configurações")
produto_selecionado = st.sidebar.selectbox("Selecione o Produto:", df['produto'].unique())
stock_atual = st.sidebar.number_input("Stock Atual no Armazém (Unidades):", min_value=0, value=500, step=50)

# Filtrar dados pelo produto
df_produto = df[df['produto'] == produto_selecionado].copy()

# 4. Preparar Dados para Machine Learning
# A Regressão Linear precisa de números em vez de datas. Vamos converter as datas.
df_produto['dia_numerico'] = df_produto['data'].map(datetime.datetime.toordinal)

X = df_produto[['dia_numerico']] # Variável independente (Tempo)
y = df_produto['vendas_diarias'] # Variável dependente (Vendas)

# 5. Treinar o Modelo
modelo = LinearRegression()
modelo.fit(X, y)

# 6. Fazer Previsões para os próximos 30 dias
ultima_data = df_produto['data'].max()
datas_futuras = pd.date_range(start=ultima_data + pd.Timedelta(days=1), periods=30)
df_futuro = pd.DataFrame({'data': datas_futuras})
df_futuro['dia_numerico'] = df_futuro['data'].map(datetime.datetime.toordinal)

# Prever as vendas futuras
previsoes = modelo.predict(df_futuro[['dia_numerico']])
# Arredondar para não termos "meias unidades" vendidas e evitar números negativos
df_futuro['vendas_previstas'] = np.maximum(0, np.round(previsoes))

# 7. Visualização (Gráfico)
fig = go.Figure()

# Linha do Histórico Real
fig.add_trace(go.Scatter(x=df_produto['data'], y=df_produto['vendas_diarias'], 
                         mode='lines', name='Vendas Reais (Histórico)', line=dict(color='blue')))

# Linha da Previsão (Machine Learning)
fig.add_trace(go.Scatter(x=df_futuro['data'], y=df_futuro['vendas_previstas'], 
                         mode='lines', name='Previsão (Próximos 30 dias)', line=dict(color='red', dash='dash')))

fig.update_layout(title=f'Histórico e Previsão de Vendas - {produto_selecionado}',
                  xaxis_title='Data', yaxis_title='Unidades Vendidas')

st.plotly_chart(fig, use_container_width=True)

# 8. Lógica de Negócio: Alerta de Stock
st.subheader("⚠️ Análise de Risco de Rutura de Stock")

# Calcular quanto vamos vender nos próximos 30 dias
procura_total_30_dias = int(df_futuro['vendas_previstas'].sum())

col1, col2, col3 = st.columns(3)
col1.metric("Stock Atual", f"{stock_atual} un")
col2.metric("Procura Prevista (30 dias)", f"{procura_total_30_dias} un")

# Decisão automática
saldo_projetado = stock_atual - procura_total_30_dias
col3.metric("Saldo Projetado no Final do Mês", f"{saldo_projetado} un")

if saldo_projetado < 0:
    st.error(f"🚨 **ALERTA CRÍTICO:** O stock vai acabar antes do fim do mês! Precisa de encomendar pelo menos {abs(saldo_projetado)} unidades para cobrir a procura.")
elif saldo_projetado < (procura_total_30_dias * 0.2): # Margem de segurança de 20%
    st.warning("⚠️ **AVISO:** O stock cobrirá a procura, mas ficará perigosamente baixo (abaixo do stock de segurança). Considere reabastecer em breve.")
else:
    st.success("✅ **STOCK SAUDÁVEL:** Tem stock suficiente para os próximos 30 dias sem risco de rutura.")
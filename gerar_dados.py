import pandas as pd
import numpy as np

# Configurar a semente aleatória para resultados consistentes
np.random.seed(42)

# Simular 365 dias de vendas (1 ano de histórico)
datas = pd.date_range(start="2025-01-01", periods=365)
produtos = ['Smartphone (Curva A)', 'Capa Protetora (Curva B)', 'Aquecedor (Sazonal)']

dados = []

for produto in produtos:
    for data in datas:
        mes = data.month
        
        # Lógica de vendas consoante o tipo de produto
        if 'Curva A' in produto:
            # Produto estrela: Vende bastante todos os dias
            vendas = np.random.poisson(lam=45) 
        elif 'Curva B' in produto:
            # Produto de curva B: Vendas moderadas
            vendas = np.random.poisson(lam=12) 
        else:
            # Produto sazonal: Vende muito mais nos meses de Inverno (Novembro a Fevereiro)
            if mes in [11, 12, 1, 2]:
                vendas = np.random.poisson(lam=30)
            else:
                vendas = np.random.poisson(lam=3)
                
        dados.append([data, produto, vendas])

# Criar o DataFrame e exportar para CSV
df = pd.DataFrame(dados, columns=['data', 'produto', 'vendas_diarias'])
df.to_csv('historico_vendas.csv', index=False)

print("Base de dados 'historico_vendas.csv' gerada com sucesso!")
# 🤖 Previsão de Procura e Alertas de Stock (Machine Learning)

Este projeto é uma aplicação interativa que utiliza **Inteligência Artificial (Regressão Linear)** para analisar o histórico de vendas de uma empresa e prever a procura futura de produtos. O objetivo principal é ajudar o setor de Logística e Supply Chain a evitar ruturas de stock e otimizar o inventário.

## 🎯 Problema de Negócio Resolvido
Em Supply Chain, o excesso de stock gera custos de armazenamento (dinheiro parado), enquanto a falta de stock gera perda de vendas e insatisfação do cliente. Este dashboard resolve o problema criando projeções matemáticas para os próximos 30 dias com base no comportamento de vendas do passado (produtos de curva A, curva B e sazonais).

## 🛠️ Tecnologias Utilizadas
* **Python** (Linguagem principal)
* **Scikit-learn** (Modelo de Machine Learning - Regressão Linear)
* **Pandas & NumPy** (Manipulação de Dados e Matemática)
* **Streamlit** (Criação do Dashboard Web interativo)
* **Plotly** (Visualização gráfica dos dados e tendências)

## 💡 Principais Funcionalidades
1. **Previsão de 30 Dias:** Algoritmo que projeta as vendas futuras com base nos dados históricos.
2. **Alertas Inteligentes:** O sistema cruza o stock atual com a procura prevista e emite alertas visuais (Crítico, Aviso ou Saudável) caso o stock não seja suficiente para terminar o mês.
3. **Filtros Dinâmicos:** Simulação em tempo real alterando o produto e a quantidade de stock no armazém.

## 🚀 Como Executar o Projeto na Sua Máquina

1. Clone este repositório:
```bash
git clone [https://github.com/FernandoLouzada17/previsao-stock-ml.git](https://github.com/FernandoLouzada17/previsao-stock-ml.git)
cd previsao-stock-ml
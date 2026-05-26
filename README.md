# 🦠 PySUS: Centro Inteligente de Monitoramento Epidemiológico

[![Python Version](https://img.shields.io/badge/Python-3.9%2B-blue?style=for-the-badge&logo=python)](https://www.python.org)
[![Pandas](https://img.shields.io/badge/Pandas-2.0%2B-darkblue?style=for-the-badge&logo=pandas)](https://pandas.pydata.org)
[![Plotly](https://img.shields.io/badge/Plotly-Interactive-vividpurple?style=for-the-badge&logo=plotly)](https://plotly.com)
[![Apache Parquet](https://img.shields.io/badge/Data_Storage-Parquet-FF6F20?style=for-the-badge&logo=apache)](https://parquet.apache.org)

Um ecossistema modular desenvolvido em Python focado em Engenharia e Análise Avançada de Dados para o monitoramento de surtos epidemiológicos (ênfase em Dengue). O projeto simula o ciclo completo de inteligência de dados de saúde: desde a modelagem estatística de variáveis climáticas e demográficas, passando por um pipeline robusto de ETL, criação de KPIs regulatórios, geração de relatórios gráficos profissionais e automação de sistemas de alertas críticos, concluindo com exportações otimizadas para ambientes de Big Data.

---

## 📌 Diferenciais Técnicos & Arquitetura
Este projeto foi desenhado sob as melhores práticas de Data Science para portfólio corporativo, evidenciando:
* **Pipeline de ETL Estruturado:** Normalização de colunas, tipagem estrita de objetos temporais (`datetime64`), mapeamento categórico indexado e engenharia de novos atributos (*feature engineering*).
* **Dualidade de Visualização:** Gráficos estáticos de alta resolução (`matplotlib` + `seaborn`) estruturados para relatórios médicos tradicionais, em paralelo a painéis interativos modernos (`plotly`) orientados a decisões executivas.
* **Otimização de Armazenamento:** Implementação de exportação híbrida em formatos legados (`.csv` com codificação adequada) e modernos de alta performance computacional (`.parquet`), ideais para integração com Data Lakes corporativos.
* **Regra de Negócio Dinâmica:** Sistema automatizado de alerta epidemiológico baseado em taxas de mortalidade flutuantes.

---

## 🛠️ Tecnologias e Ferramentas Utilizadas
* **Linguagem Core:** Python 3.x
* **Manipulação e Engenharia de Dados:** `pandas`, `numpy`
* **Visualização de Dados:** `seaborn`, `matplotlib`, `plotly.express`, `plotly.graph_objects`
* **Gerenciamento de Arquivos:** `os`, `warnings`

---

## 🏗️ O Pipeline de Dados (Passo a Passo)

### 1. Geração de Massa de Dados Estocástica
Para mimetizar um cenário real do SUS sem infringir LGPD com dados sensíveis de pacientes, foi modelado um gerador estatístico com as seguintes características epidemiológicas:
* **Casos:** 5.000 registros distribuídos ao longo de todo o ano de 2023.
* **Geografia:** Focado em municípios estratégicos do estado de São Paulo (*Ribeirão Preto, Campinas, São Paulo, Santos, Franca e Araraquara*).
* **Variáveis Climáticas Avançadas:**
    * *Temperatura:* Modelada através de uma **Distribuição Normal** ($\mu = 29^\circ\text{C}$, $\sigma = 3$) simulando picos tropicais.
    * *Pluviosidade (Chuva):* Modelada através de uma **Distribuição Gamma** ($\alpha = 2, \beta = 10$), ideal para capturar a assimetria positiva de eventos de precipitação meteorológica.

### 2. Processamento e Engenharia de Atributos (ETL)
* **Padronização Corporativa:** Conversão sistemática de todas as colunas para *UPPERCASE*.
* **Sanitização Temporal:** Conversão do campo `DT_NOTIFIC` em formato nativo de data.
* **Mapeamento Categórico:** Tradução de códigos de desfecho clínico do DATASUS baseados em dicionário oficial (ex: `10` $\rightarrow$ Dengue, `12` $\rightarrow$ Dengue Grave).
* **Feature Engineering:** Extração automática de dimensões analíticas de tempo: `ANO`, `MES`, `MES_NOME` e `SEMANA` epidemiológica (`isocalendar`).

---

## 📊 Análise Analítica & Visualizações Geradas

Os artefatos gráficos do projeto são armazenados automaticamente na pasta `./exports` com resolução de **300 DPI**, garantindo fidelidade visual para apresentações e relatórios executivos.

### 📐 Análises Estatísticas e Demográficas (Matplotlib / Seaborn)
1.  **Distribuição por Sexo (`sexo.png`):** Avaliação de frequência absoluta e volumetria por gênero biológico identificando possíveis vieses de notificação.
2.  **Distribuição por Faixa Etária (`faixa_etaria.png`):** Gráfico de barras ordenador por densidade de incidência por grupo de idade.
3.  **Histograma de Idade com Densidade (`histograma_idade.png`):** Análise de distribuição contínua da idade combinando barras clássicas com curva de estimativa de densidade kernel (KDE).
4.  **Boxplot de Dispersão Idade vs Sexo (`boxplot_idade.png`):** Identificação visual de outliers, mediana, quartis e variabilidade etária entre gêneros.
5.  **Análise de Classificação Final (`classificacao.png`):** Gráfico de setores (pizza) demonstrando a proporção de severidade dos casos notificados.
6.  **Evolução Temporal dos Casos (`serie_temporal.png`):** Gráfico de linha detalhando as oscilações diárias de surtos durante o ano corrente.
7.  **Volumetria por Município (`municipios.png`):** Gráfico de barras verticais mapeando a distribuição espacial da doença por cidade-foco.
8.  **Mapa de Calor de Correlação Linear (`heatmap.png`):** Matriz de correlação de Pearson mapeando interações numéricas entre idade, temperatura, pluviosidade e óbitos.
9.  **Dispersão Chuva x Idade (`chuva_idade.png`):** Gráfico de dispersão (*scatterplot*) estratificado por sexo, isolando comportamento de variáveis de interesse biológico.

### 📈 Dashboards Interativos Avançados (Plotly)
* **`dashboard_interativo.html`:** Histograma empilhado interativo cruzando faixas etárias e segmentação de cores por sexo, permitindo zoom dinâmico e tooltips sob demanda.
* **`serie_temporal_interativa.html`:** Linha de tendência temporal contínua e interativa, ideal para acompanhamento em tempo real de salas de situação de saúde pública.

---

## ⚙️ Regras de Alerta Epidemiológico e Output
Ao final do processamento, os KPIs consolidados são submetidos a uma função condicional que monitora a gravidade do cenário analítico atual:

$$\text{Taxa de Mortalidade} = \left( \frac{\text{Total Óbitos}}{\text{Total Casos}} \right) \times 100$$

* `Taxa > 5%`: 🛑 **ALERTA CRÍTICO**
* `Taxa entre 2% e 5%`: ⚠️ **ALERTA MODERADO**
* `Taxa < 2%`: ✅ **Situação controlada**

### Armazenamento Otimizado
O pipeline consolida os resultados na pasta final entregando dois ecossistemas de dados estruturados para o usuário:
1.  **`dengue_tratado_2023.csv`:** Codificado em `utf-8-sig` para compatibilidade cross-platform instantânea (evitando quebras de caracteres acentuados no Microsoft Excel).
2.  **`dengue_tratado_2023.parquet`:** Arquivo colunar otimizado com compressão interna nativa para alta performance em consultas SQL e pipelines de Big Data.

---

## 💻 Código Fonte Completo do Projeto

```python
"""
PySUS - Centro Inteligente de Monitoramento Epidemiológico
Autor: André Luiz Magalhães de Oliveira
Contexto: Portfólio Profissional de Data Science & Engenharia de Dados
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
import warnings
import os

# Configurações de Supressão e Estilo Visual
warnings.filterwarnings("ignore")
plt.style.use("ggplot")
sns.set_theme(style="whitegrid", palette="deep")

# Definição de Variáveis Globais de Ambiente
ANO_ANALISE = 2023
PASTA_EXPORT = "./exports"
os.makedirs(PASTA_EXPORT, exist_ok=True)
ARQUIVO_SAIDA = f"{PASTA_EXPORT}/dengue_tratado_{ANO_ANALISE}.csv"

# ==========================================
# 1. MODELAGEM E GERAÇÃO DA MASSA DE DADOS (STOCHASTIC GENERATION)
# ==========================================
np.random.seed(42)
TOTAL_REGISTROS = 5000

datas = pd.date_range(start=f"{ANO_ANALISE}-01-01", end=f"{ANO_ANALISE}-12-31", freq="D")
municipios = ["Ribeirao Preto", "Campinas", "Sao Paulo", "Santos", "Franca", "Araraquara"]
sexos = ["M", "F"]
faixas_etarias = ["0-10", "11-20", "21-30", "31-40", "41-50", "51-60", "60+"]

df = pd.DataFrame({
    "DT_NOTIFIC": np.random.choice(datas, TOTAL_REGISTROS),
    "SEXO": np.random.choice(sexos, TOTAL_REGISTROS),
    "FAIXA_ETARIA": np.random.choice(faixas_etarias, TOTAL_REGISTROS),
    "MUNICIPIO": np.random.choice(municipios, TOTAL_REGISTROS),
    # Códigos DATASUS: 10:Dengue, 11:Sinais Alerta, 12:Grave, 13:Descartado
    "CLASSI_FIN": np.random.choice([10, 11, 12, 13], TOTAL_REGISTROS, p=[0.60, 0.20, 0.10, 0.10]),
    # Evolução: 1:Cura, 2:Óbito
    "EVOLUCAO": np.random.choice([1, 2], TOTAL_REGISTROS, p=[0.96, 0.04]),
    "IDADE": np.random.randint(1, 90, TOTAL_REGISTROS),
    "TEMPERATURA": np.random.normal(29, 3, TOTAL_REGISTROS),
    "CHUVA": np.random.gamma(2, 10, TOTAL_REGISTROS)
})

# ==========================================
# 2. PIPELINE DE EXTRAÇÃO, TRANSFORMAÇÃO E CARGA (ETL)
# ==========================================
print("=" * 70)
print("INICIANDO ETAPA ETL (EXTRACT, TRANSFORM, LOAD)")
print("=" * 70)

# Padronização de Schema e Tipagem Estrita
df.columns = df.columns.str.upper()
df["DT_NOTIFIC"] = pd.to_datetime(df["DT_NOTIFIC"])

# Engenharia de Novas Features (Derivação Temporal)
df["ANO"] = df["DT_NOTIFIC"].dt.year
df["MES"] = df["DT_NOTIFIC"].dt.month
df["MES_NOME"] = df["DT_NOTIFIC"].dt.month_name()
df["SEMANA"] = df["DT_NOTIFIC"].dt.isocalendar().week

# Mapeamento de Regras de Negócio e Variáveis Alvo
df["OBITO"] = df["EVOLUCAO"].apply(lambda x: 1 if x == 2 else 0)

mapa_classificacao = {
    10: "Dengue",
    11: "Dengue com sinais",
    12: "Dengue grave",
    13: "Descartado"
}
df["CLASSIFICACAO"] = df["CLASSI_FIN"].map(mapa_classificacao)

print("Transformações concluídas com sucesso.\n")

# ==========================================
# 3. CONSOLIDAÇÃO DE KPIS EPIDEMIOLÓGICOS
# ==========================================
print("=" * 70)
print("KPIS EPIDEMIOLÓGICOS CONSOLIDADOS")
print("=" * 70)
total_casos = len(df)
total_obitos = df["OBITO"].sum()
taxa_obito = (total_obitos / total_casos) * 100

print(f"Total Casos Analisados: {total_casos:,}")
print(f"Total Óbitos Confirmados: {total_obitos:,}")
print(f"Taxa de Letalidade/Mortalidade: {taxa_obito:.2f}%")
print()

print("=" * 70)
print("SUMÁRIO ESTATÍSTICO DESCRITIVO")
print("=" * 70)
print(df.describe(include="all"))
print()

# ==========================================
# 4. DATA VISUALIZATION - VISÕES GRÁFICAS ESTÁTICAS
# ==========================================
print("Gerando visualizações estáticas (Alta Resolução)...")

# Gráfico 1: Volumetria por Sexo
plt.figure(figsize=(8, 5))
sns.countplot(data=df, x="SEXO")
plt.title("Distribuição Absoluta de Notificações por Gênero")
plt.savefig(f"{PASTA_EXPORT}/sexo.png", dpi=300, bbox_inches="tight")
plt.close()

# Gráfico 2: Volumetria por Faixa Etária
plt.figure(figsize=(12, 5))
ordem_etaria = df["FAIXA_ETARIA"].value_counts().index
sns.countplot(data=df, x="FAIXA_ETARIA", order=ordem_etaria)
plt.xticks(rotation=45)
plt.title("Distribuição de Notificações por Faixa Etária")
plt.savefig(f"{PASTA_EXPORT}/faixa_etaria.png", dpi=300, bbox_inches="tight")
plt.close()

# Gráfico 3: Histograma com Curva de Densidade (KDE)
plt.figure(figsize=(10, 5))
sns.histplot(data=df, x="IDADE", bins=20, kde=True)
plt.title("Histograma de Idade dos Pacientes Notificados")
plt.savefig(f"{PASTA_EXPORT}/histograma_idade.png", dpi=300, bbox_inches="tight")
plt.close()

# Gráfico 4: Boxplot de Distribuição de Idades por Sexo
plt.figure(figsize=(10, 5))
sns.boxplot(data=df, x="SEXO", y="IDADE")
plt.title("Boxplot de Variabilidade: Idade vs Gênero")
plt.savefig(f"{PASTA_EXPORT}/boxplot_idade.png", dpi=300, bbox_inches="tight")
plt.close()

# Gráfico 5: Proporcionalidade de Diagnósticos Finais
plt.figure(figsize=(8, 8))
classificacao_counts = df["CLASSIFICACAO"].value_counts()
plt.pie(classificacao_counts, labels=classificacao_counts.index, autopct="%1.1f%%", startangle=140)
plt.title("Proporção Analítica da Classificação Clínica Final")
plt.savefig(f"{PASTA_EXPORT}/classificacao.png", dpi=300, bbox_inches="tight")
plt.close()

# Gráfico 6: Linha de Evolução Temporal
plt.figure(figsize=(14, 6))
casos_tempo = df.groupby("DT_NOTIFIC").size().reset_index(name="CASOS")
sns.lineplot(data=casos_tempo, x="DT_NOTIFIC", y="CASOS")
plt.title("Evolução Temporal Diária dos Casos Notificados")
plt.xlabel("Data da Notificação")
plt.ylabel("Volume de Casos")
plt.savefig(f"{PASTA_EXPORT}/serie_temporal.png", dpi=300, bbox_inches="tight")
plt.close()

# Gráfico 7: Distribuição Geográfica de Casos por Município
plt.figure(figsize=(10, 5))
municipios_top = df["MUNICIPIO"].value_counts()
municipios_top.plot(kind="bar", color="skyblue")
plt.title("Incidência de Casos por Município-Foco")
plt.ylabel("Quantidade Absoluta")
plt.xticks(rotation=45)
plt.savefig(f"{PASTA_EXPORT}/municipios.png", dpi=300, bbox_inches="tight")
plt.close()

# Gráfico 8: Matriz de Correlação Linear (Heatmap)
plt.figure(figsize=(10, 8))
corr = df.select_dtypes(include=["int64", "float64"]).corr()
sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f", linewidths=.5)
plt.title("Matriz de Correlação de Pearson")
plt.savefig(f"{PASTA_EXPORT}/heatmap.png", dpi=300, bbox_inches="tight")
plt.close()

# Gráfico 9: Dispersão Cruzada - Climatologia x Demografia
plt.figure(figsize=(10, 5))
sns.scatterplot(data=df, x="CHUVA", y="IDADE", hue="SEXO", alpha=0.6)
plt.title("Análise Multivariada: Precipitação Combinada vs Idade e Gênero")
plt.savefig(f"{PASTA_EXPORT}/chuva_idade.png", dpi=300, bbox_inches="tight")
plt.close()

# ==========================================
# 5. DATA VISUALIZATION - INTERATIVIDADE (PLOTLY)
# ==========================================
print("Construindo Dashboards Dinâmicos Interativos...")

# Dashboard 1: Distribuição Demográfica Customizada
fig = px.bar(df, x="FAIXA_ETARIA", color="SEXO", title="Painel Interativo: Distribuição de Faixa Etária por Gênero")
fig.write_html(f"{PASTA_EXPORT}/dashboard_interativo.html")

# Dashboard 2: Série Temporal Dinâmica
fig2 = px.line(casos_tempo, x="DT_NOTIFIC", y="CASOS", title="Painel Interativo: Série Temporal de Monitoramento Contínuo")
fig2.write_html(f"{PASTA_EXPORT}/serie_temporal_interativa.html")

# ==========================================
# 6. ENGENHARIA DE ALERTAS EPIDEMIOLÓGICOS E PERSISTÊNCIA DOS DADOS (LOAD)
# ==========================================
print("\n" + "=" * 70)
print("SISTEMA DE ALERTA EPIDEMIOLÓGICO DE SAÚDE PÚBLICA")
print("=" * 70)
if taxa_obito > 5.0:
    print("🚨 STATUS: ALERTA CRÍTICO - PLANO DE CONTINGÊNCIA IMEDIATO REQUERIDO")
elif taxa_obito > 2.0:
    print("⚠️ STATUS: ALERTA MODERADO - INTENSIFICAR FISCALIZAÇÃO E BUSCA ATIVA")
else:
    print("✅ STATUS: SITUAÇÃO CONTROLADA - MONITORAMENTO DE ROTINA")
print("=" * 70)

# Exportação Segura para Data Lakes e Camadas Corporativas
print("\nSalvando arquivos de saída nas partições alvo...")
df.to_csv(ARQUIVO_SAIDA, index=False, encoding="utf-8-sig")
print(f" Flat File persistido com sucesso em: {ARQUIVO_SAIDA}")

arquivo_parquet = f"{PASTA_EXPORT}/dengue_tratado_{ANO_ANALISE}.parquet"
try:
    df.to_parquet(arquivo_parquet, index=False)
    print(f" File Colunar Parquet persistido com sucesso em: {arquivo_parquet}")
except ImportError:
    print(" Nota: Instale 'pyarrow' ou 'fastparquet' para gerar o arquivo compilado em formato Parquet.")

print("\nPipeline de dados executado e finalizado com sucesso absoluto.")

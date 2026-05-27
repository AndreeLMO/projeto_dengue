# ============================================================
# CENTRO INTELIGENTE DE MONITORAMENTO EPIDEMIOLÓGICO - AVALIAÇÃO DE CASOS DE DENGUE
# PROJETO OTIMIZADO - PYTHON
# ============================================================
# Autor: André Luiz Magalhães de Oliveira
# Formação: Físico Médico | Especialista em Data Science & Analytics
# Universidade de São Paulo
# ============================================================

import os
import warnings
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

warnings.filterwarnings("ignore")
plt.style.use("ggplot")
sns.set(style="whitegrid", palette="deep")

# ============================================================
# CONFIGURAÇÕES
# ============================================================

ANO_ANALISE = 2023
PASTA_EXPORT = "./exports"
os.makedirs(PASTA_EXPORT, exist_ok=True)

ARQUIVO_SAIDA = f"{PASTA_EXPORT}/dengue_tratado_{ANO_ANALISE}.csv"

# ============================================================
# DADOS EXEMPLO
# ============================================================

np.random.seed(42)
datas = pd.date_range("2023-01-01", "2023-12-31", freq="D")

df = pd.DataFrame({
    "DT_NOTIFIC": np.random.choice(datas, 5000),
    "SEXO": np.random.choice(["M", "F"], 5000),
    "FAIXA_ETARIA": np.random.choice(["0-10","11-20","21-30","31-40","41-50","51-60","60+"], 5000),
    "MUNICIPIO": np.random.choice(["Ribeirao Preto","Campinas","Sao Paulo","Santos","Franca","Araraquara"], 5000),
    "CLASSI_FIN": np.random.choice([10,11,12,13], 5000, p=[0.60,0.20,0.10,0.10]),
    "EVOLUCAO": np.random.choice([1,2], 5000, p=[0.96,0.04]),
    "IDADE": np.random.randint(1, 90, 5000),
    "TEMPERATURA": np.random.normal(29, 3, 5000),
    "CHUVA": np.random.gamma(2, 10, 5000)
})

# ============================================================
# ETL
# ============================================================

df.columns = df.columns.str.upper()
df["DT_NOTIFIC"] = pd.to_datetime(df["DT_NOTIFIC"])
df = df.drop_duplicates()

# ============================================================
# FEATURES & CLASSIFICAÇÃO
# ============================================================

df["OBITO"] = (df["EVOLUCAO"] == 2).astype(int)
df["CLASSIFICACAO"] = df["CLASSI_FIN"].map({
    10: "Dengue", 11: "Dengue com sinais", 12: "Dengue grave", 13: "Descartado"
})
df["ANO"] = df["DT_NOTIFIC"].dt.year
df["MES"] = df["DT_NOTIFIC"].dt.month
df["MES_NOME"] = df["DT_NOTIFIC"].dt.month_name()
df["SEMANA"] = df["DT_NOTIFIC"].dt.isocalendar().week

# ============================================================
# KPIs
# ============================================================

total_casos = len(df)
total_obitos = df["OBITO"].sum()
taxa_obito = (total_obitos / total_casos) * 100

print(f"Total Casos: {total_casos:,}")
print(f"Total Óbitos: {total_obitos:,}")
print(f"Taxa Mortalidade: {taxa_obito:.2f}%")

# ============================================================
# FUNÇÕES DE PLOT
# ============================================================

def salvar_plot(fig, nome):
    fig.savefig(f"{PASTA_EXPORT}/{nome}.png", dpi=300, bbox_inches="tight")
    plt.close(fig)

# Exemplos de gráficos
salvar_plot(sns.countplot(data=df, x="SEXO").figure, "sexo")
salvar_plot(sns.countplot(data=df, x="FAIXA_ETARIA", order=df["FAIXA_ETARIA"].value_counts().index).figure, "faixa_etaria")
salvar_plot(sns.histplot(data=df, x="IDADE", bins=20, kde=True).figure, "histograma_idade")

# ============================================================
# DASHBOARD INTERATIVO
# ============================================================

px.bar(df, x="FAIXA_ETARIA", color="SEXO", title="Faixa Etária por Sexo") \
    .write_html(f"{PASTA_EXPORT}/dashboard_interativo.html")

px.line(df.groupby("DT_NOTIFIC").size().reset_index(name="CASOS"),
        x="DT_NOTIFIC", y="CASOS", title="Série Temporal Interativa") \
    .write_html(f"{PASTA_EXPORT}/serie_temporal_interativa.html")

# ============================================================
# ALERTA EPIDEMIOLÓGICO
# ============================================================

if taxa_obito > 5:
    print("ALERTA CRÍTICO")
elif taxa_obito > 2:
    print("ALERTA MODERADO")
else:
    print("Situação controlada")

# ============================================================
# EXPORTAÇÃO
# ============================================================

df.to_csv(ARQUIVO_SAIDA, index=False, encoding="utf-8-sig")
df.to_excel(f"{PASTA_EXPORT}/dengue_tratado_{ANO_ANALISE}.xlsx", index=False)

try:
    df.to_parquet(f"{PASTA_EXPORT}/dengue_tratado_{ANO_ANALISE}.parquet", index=False)
except:
    print("Instale pyarrow para exportar em parquet.")

print("Arquivos gerados com sucesso em:", PASTA_EXPORT)

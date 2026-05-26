# ============================================================
# CENTRO INTELIGENTE DE MONITORAMENTO EPIDEMIOLÓGICO
# PROJETO COMPLETO - PYTHON
# ============================================================

# ============================================================
# IMPORTS
# ============================================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
import warnings
import os

warnings.filterwarnings("ignore")

# ============================================================
# CONFIGURAÇÃO VISUAL
# ============================================================

plt.style.use("ggplot")

sns.set(
    style="whitegrid",
    palette="deep"
)

# ============================================================
# CONFIGURAÇÕES
# ============================================================

ANO_ANALISE = 2023

PASTA_EXPORT = "./exports"

os.makedirs(
    PASTA_EXPORT,
    exist_ok=True
)

ARQUIVO_SAIDA = (
    f"{PASTA_EXPORT}/dengue_tratado_{ANO_ANALISE}.csv"
)

# ============================================================
# DADOS EXEMPLO
# TROQUE PELO SEU DATASET REAL
# ============================================================

np.random.seed(42)

datas = pd.date_range(
    start="2023-01-01",
    end="2023-12-31",
    freq="D"
)

municipios = [
    "Ribeirao Preto",
    "Campinas",
    "Sao Paulo",
    "Santos",
    "Franca",
    "Araraquara"
]

sexos = ["M", "F"]

faixas = [
    "0-10",
    "11-20",
    "21-30",
    "31-40",
    "41-50",
    "51-60",
    "60+"
]

df = pd.DataFrame({

    "DT_NOTIFIC": np.random.choice(
        datas,
        5000
    ),

    "SEXO": np.random.choice(
        sexos,
        5000
    ),

    "FAIXA_ETARIA": np.random.choice(
        faixas,
        5000
    ),

    "MUNICIPIO": np.random.choice(
        municipios,
        5000
    ),

    "CLASSI_FIN": np.random.choice(
        [10,11,12,13],
        5000,
        p=[0.60,0.20,0.10,0.10]
    ),

    "EVOLUCAO": np.random.choice(
        [1,2],
        5000,
        p=[0.96,0.04]
    ),

    "IDADE": np.random.randint(
        1,
        90,
        5000
    ),

    "TEMPERATURA": np.random.normal(
        29,
        3,
        5000
    ),

    "CHUVA": np.random.gamma(
        2,
        10,
        5000
    )
})

# ============================================================
# ETL
# ============================================================

print("="*70)
print("ETAPA ETL")
print("="*70)

df.columns = df.columns.str.upper()

df["DT_NOTIFIC"] = pd.to_datetime(
    df["DT_NOTIFIC"]
)

df = df.drop_duplicates()

# ============================================================
# INDICADOR DE ÓBITO
# ============================================================

df["OBITO"] = df["EVOLUCAO"].apply(
    lambda x: 1 if x == 2 else 0
)

# ============================================================
# CLASSIFICAÇÃO
# ============================================================

mapa_classificacao = {

    10: "Dengue",
    11: "Dengue com sinais",
    12: "Dengue grave",
    13: "Descartado"
}

df["CLASSIFICACAO"] = (
    df["CLASSI_FIN"]
    .map(mapa_classificacao)
)

# ============================================================
# FEATURES
# ============================================================

df["ANO"] = (
    df["DT_NOTIFIC"]
    .dt.year
)

df["MES"] = (
    df["DT_NOTIFIC"]
    .dt.month
)

df["MES_NOME"] = (
    df["DT_NOTIFIC"]
    .dt.month_name()
)

df["SEMANA"] = (
    df["DT_NOTIFIC"]
    .dt.isocalendar()
    .week
)

# ============================================================
# KPI
# ============================================================

print()
print("="*70)
print("KPIs EPIDEMIOLÓGICOS")
print("="*70)

total_casos = len(df)

total_obitos = df["OBITO"].sum()

taxa_obito = (
    total_obitos / total_casos
) * 100

print(f"Total Casos: {total_casos:,}")

print(f"Total Óbitos: {total_obitos:,}")

print(f"Taxa Mortalidade: {taxa_obito:.2f}%")

print()

# ============================================================
# ESTATÍSTICAS
# ============================================================

print("="*70)
print("ESTATÍSTICAS")
print("="*70)

print(
    df.describe(include="all")
)

print()

# ============================================================
# DISTRIBUIÇÃO SEXO
# ============================================================

print("="*70)
print("DISTRIBUIÇÃO SEXO")
print("="*70)

print(
    df["SEXO"]
    .value_counts()
)

plt.figure(figsize=(8,5))

sns.countplot(
    data=df,
    x="SEXO"
)

plt.title(
    "Distribuição por Sexo"
)

plt.savefig(
    f"{PASTA_EXPORT}/sexo.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

# ============================================================
# FAIXA ETÁRIA
# ============================================================

plt.figure(figsize=(12,5))

sns.countplot(
    data=df,
    x="FAIXA_ETARIA",
    order=df["FAIXA_ETARIA"]
    .value_counts()
    .index
)

plt.xticks(rotation=45)

plt.title(
    "Distribuição Faixa Etária"
)

plt.savefig(
    f"{PASTA_EXPORT}/faixa_etaria.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

# ============================================================
# HISTOGRAMA IDADE
# ============================================================

plt.figure(figsize=(10,5))

sns.histplot(
    data=df,
    x="IDADE",
    bins=20,
    kde=True
)

plt.title(
    "Histograma de Idade"
)

plt.savefig(
    f"{PASTA_EXPORT}/histograma_idade.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

# ============================================================
# BOXPLOT
# ============================================================

plt.figure(figsize=(10,5))

sns.boxplot(
    data=df,
    x="SEXO",
    y="IDADE"
)

plt.title(
    "Boxplot Idade por Sexo"
)

plt.savefig(
    f"{PASTA_EXPORT}/boxplot_idade.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

# ============================================================
# CLASSIFICAÇÃO FINAL
# ============================================================

classificacao = (
    df["CLASSIFICACAO"]
    .value_counts()
)

plt.figure(figsize=(8,8))

plt.pie(
    classificacao,
    labels=classificacao.index,
    autopct="%1.1f%%"
)

plt.title(
    "Classificação Final"
)

plt.savefig(
    f"{PASTA_EXPORT}/classificacao.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

# ============================================================
# SÉRIE TEMPORAL
# ============================================================

casos_tempo = (

    df.groupby("DT_NOTIFIC")
    .size()
    .reset_index(name="CASOS")
)

plt.figure(figsize=(14,6))

sns.lineplot(
    data=casos_tempo,
    x="DT_NOTIFIC",
    y="CASOS"
)

plt.title(
    "Evolução Temporal dos Casos"
)

plt.xlabel("Data")

plt.ylabel("Casos")

plt.savefig(
    f"{PASTA_EXPORT}/serie_temporal.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

# ============================================================
# CASOS POR MUNICÍPIO
# ============================================================

municipios_top = (

    df["MUNICIPIO"]
    .value_counts()
)

plt.figure(figsize=(10,5))

municipios_top.plot(
    kind="bar"
)

plt.title(
    "Casos por Município"
)

plt.ylabel("Quantidade")

plt.savefig(
    f"{PASTA_EXPORT}/municipios.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

# ============================================================
# HEATMAP
# ============================================================

corr = df.select_dtypes(
    include=[
        "int64",
        "float64"
    ]
).corr()

plt.figure(figsize=(10,8))

sns.heatmap(
    corr,
    annot=True,
    cmap="coolwarm"
)

plt.title(
    "Mapa de Correlação"
)

plt.savefig(
    f"{PASTA_EXPORT}/heatmap.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

# ============================================================
# CHUVA X CASOS
# ============================================================

plt.figure(figsize=(10,5))

sns.scatterplot(
    data=df,
    x="CHUVA",
    y="IDADE",
    hue="SEXO"
)

plt.title(
    "Relação Chuva x Idade"
)

plt.savefig(
    f"{PASTA_EXPORT}/chuva_idade.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

# ============================================================
# DASHBOARD INTERATIVO PLOTLY
# ============================================================

fig = px.bar(

    df,

    x="FAIXA_ETARIA",

    color="SEXO",

    title="Faixa Etária por Sexo"
)

fig.write_html(
    f"{PASTA_EXPORT}/dashboard_interativo.html"
)

fig.show()

# ============================================================
# PLOTLY TEMPORAL
# ============================================================

fig2 = px.line(

    casos_tempo,

    x="DT_NOTIFIC",

    y="CASOS",

    title="Série Temporal Interativa"
)

fig2.write_html(
    f"{PASTA_EXPORT}/serie_temporal_interativa.html"
)

fig2.show()

# ============================================================
# ALERTA EPIDEMIOLÓGICO
# ============================================================

print()
print("="*70)
print("SISTEMA DE ALERTA")
print("="*70)

if taxa_obito > 5:

    print("ALERTA CRÍTICO")

elif taxa_obito > 2:

    print("ALERTA MODERADO")

else:

    print("Situação controlada")

print()

# ============================================================
# EXPORTAÇÃO CSV
# ============================================================

df.to_csv(

    ARQUIVO_SAIDA,

    index=False,

    encoding="utf-8-sig"
)

print(
    f"CSV salvo em: {ARQUIVO_SAIDA}"
)

# ============================================================
# EXPORTAÇÃO PARQUET
# ============================================================

arquivo_parquet = (
    f"{PASTA_EXPORT}/dengue_tratado_{ANO_ANALISE}.parquet"
)

try:

    df.to_parquet(
        arquivo_parquet,
        index=False
    )

    print(
        f"PARQUET salvo em: {arquivo_parquet}"
    )

except Exception as e:

    print(
        "Erro ao salvar parquet."
    )

    print(
        "Instale pyarrow:"
    )

    print(
        "pip install pyarrow"
    )

# ============================================================
# EXPORTAÇÃO EXCEL
# ============================================================

arquivo_excel = (
    f"{PASTA_EXPORT}/dengue_tratado_{ANO_ANALISE}.xlsx"
)

df.to_excel(
    arquivo_excel,
    index=False
)

print(
    f"Excel salvo em: {arquivo_excel}"
)

# ============================================================
# TABELAS RESUMO
# ============================================================

tabela_sexo = (

    df.groupby("SEXO")
    .agg({

        "OBITO":"sum",

        "IDADE":"mean"
    })
)

print()
print("="*70)
print("TABELA RESUMO SEXO")
print("="*70)

print(tabela_sexo)

# ============================================================
# TOP MUNICÍPIOS
# ============================================================

top_municipios = (

    df["MUNICIPIO"]
    .value_counts()
    .head(10)
)

print()
print("="*70)
print("TOP MUNICÍPIOS")
print("="*70)

print(top_municipios)

# ============================================================
# FINALIZAÇÃO
# ============================================================

print()
print("="*70)
print("PROCESSO FINALIZADO COM SUCESSO")
print("="*70)

print()

print("Arquivos gerados:")

print()

print("- CSV")

print("- Excel")

print("- Parquet")

print("- Heatmaps")

print("- Histogramas")

print("- Dashboard HTML")

print("- Série Temporal")

print("- KPIs")

print("- Gráficos PNG")

print()

print(f"Todos os arquivos estão em: {PASTA_EXPORT}")
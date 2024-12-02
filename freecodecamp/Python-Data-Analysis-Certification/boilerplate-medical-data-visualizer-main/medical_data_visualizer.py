import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
df = pd.read_csv("medical_examination.csv")

# 2
df["overweight"] = np.where((df["weight"] / (df["height"]**2)) > 25, 1, 0)

# 3
def normalizeBinaries(colToNormalize):
    df[colToNormalize] = np.where(df[colToNormalize] == 1, 0, 1)


normalizeBinaries("cholesterol")
normalizeBinaries("gluc")


# 4
def draw_cat_plot():
    # 5
    df_cat = pd.melt(df, id_vars=["cardio"], value_vars=["cholesterol", "gluc", "smoke", "alco", "active", "overweight"])


    # 6
    df_cat["total"] = 1
    df_cat = df_cat.groupby(["cardio", "variable", "value"], as_index=False).count()
    

    # 7
    plot = sns.catplot(x="variable", 
            y="total", 
            col="cardio",
            data=df_cat,
            kind="bar",
            hue="value")


    # 8
    fig = plot


    # 9
    fig.savefig('catplot.png')
    return fig


# 10
def draw_heat_map():
    # 11
    filterDiastolic = df['ap_lo'] <= df['ap_hi']
    filterHeightL = df['height'] >= df['height'].quantile(0.025)
    filterHeightM = df['height'] <= df['height'].quantile(0.975)
    filterWeightL = df['weight'] >= df['weight'].quantile(0.025)
    filterWeightM = df['weight'] <= df['weight'].quantile(0.975)
    filters = filterDiastolic & filterHeightL & filterHeightM & filterWeightL & filterWeightM

    df_heat = df[filters]

    # 12
    corr = df_heat.corr()

    # 13
    mask = np.triu(corr)

    # 14
    fig, ax = plt.subplots(figsize=(12, 12))

    # 15
    sns.heatmap(data=corr, annot=True, mask=mask, linewidths=1, square=True, fmt=".1f", center=0.08, cbar_kws={"shrink": 0.5})

    # 16
    fig.savefig('heatmap.png')
    return fig

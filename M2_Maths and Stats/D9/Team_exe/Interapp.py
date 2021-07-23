import streamlit as st
import pandas as pd
import plotly
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
st.set_option('deprecation.showPyplotGlobalUse', False)

st.title("Getting Drunk Exercise, by Team 1")
st.image('Types-of-Beer-Glasses-Mugs-from-Homebrew-Academy.jpg')

df = pd.read_csv("C:\\Users\\Walid Lakouader\\Documents\\GitHub\\ai_jun21\\M1-Python\\04. Strings and Files\\ai_jun21\\M2-Maths and Stats\\D7\data\\beers.csv")

corr = df.corr()
plt.figure(figsize=(10, 10))
HM = sns.heatmap(corr,annot=True,fmt=".2",cmap= 'coolwarm',linewidths=2,square = True)
st.subheader("Figuring out the relationships at first")
st.pyplot()



Beers_count = df["style"].value_counts(dropna=False) / len(df["style"])*100

Brewers = df["brewery_id"].value_counts(dropna=False)

AVG_BSB = Brewers.median() # Average Beer Styles / Brewere

Beer_Popularity = df["style"].value_counts() / len(df["style"])

Beer_Popularity = Beer_Popularity[0:20]

BPF = go.Figure(data=[go.Pie(labels=Beer_Popularity.index.to_list(), values=Beer_Popularity.to_list())])

st.subheader("Beer Popularity by Style")
st.plotly_chart(BPF)

#Slider Elements
Beers = Beers_count[0:20].index.to_list()
Beer  = st.selectbox('Slide Beer Style', options=Beers)

Brewers = Brewers[0:20].index.to_list()

Abv_Beer = df[df["style"] == Beer]["abv"]

Mean_Abv = Abv_Beer.mean() *100
Min_Abv = Abv_Beer.min() *100
Max_Abv = Abv_Beer.max() *100

IBU_Beer = df[df["style"] == Beer]["ibu"]
Mean_IBU = IBU_Beer.median()
Min_IBU = IBU_Beer.min()
Max_IBU = IBU_Beer.max()

st.subheader("ABV (Alcohol by Volume): ")
st.write(f"The average ABV for the **{Beer}** style beer is arround **{Mean_Abv:.2f}%**. However it can vary from **{Min_Abv:.2f}%** Up to **{Max_Abv:.2f}%**.")

y0 = df["abv"]*100
y1 = Abv_Beer*100

fig_abv = go.Figure()
fig_abv.add_trace(go.Box(y=y0,name="Beer in General"))
fig_abv.add_trace(go.Box(y=y1,name=Beer))
fig_abv.update_xaxes(title="Beers")
fig_abv.update_yaxes(title="Alcohol %")
st.plotly_chart(fig_abv)


st.subheader("IBU (International Bitterness Units): ")
st.write(f"The average ABV for the **{Beer}** style beer is arround **{Mean_IBU:.2f}**. However it can vary from **{Min_IBU}** Up to **{Max_IBU}**.")

y2 = df["ibu"]
y3 = IBU_Beer

fig_ibu = go.Figure()
fig_ibu.add_trace(go.Box(y=y2,name="Beer in General"))
fig_ibu.add_trace(go.Box(y=y3,name=Beer))
fig_ibu.update_xaxes(title="Beers")
fig_ibu.update_yaxes(title="IBU")
st.plotly_chart(fig_ibu)


st.subheader("Popularity: ")
Popularity = len(df[df["style"] == Beer]["ounces"]) / len(df["style"])

a = len(df[df["style"] == Beer]["ounces"])
b = len(df["style"])

fig2 = go.Figure(data=[go.Pie(labels=[Beer,"The rest"], values=[a,b])])

fig2.update_layout(title_text=f"Can popularity for the {Beer} style")
st.plotly_chart(fig2)
ounces_data = df[df["style"] == Beer]["ounces"].value_counts()

fig = go.Figure(data=[go.Pie(labels=ounces_data.index.to_list(), values=ounces_data.to_list())])
fig.update_layout(title_text=f"Can popularity for the {Beer} style")

st.plotly_chart(fig)

Companies_Beer = df[df["style"] == Beer]["brewery_id"].value_counts()

fig1 = go.Figure(data=[go.Pie(labels=Companies_Beer[0:5].index.to_list(), values=Companies_Beer[0:5].to_list())])
fig1.update_layout(title_text=f"TOP 5 Companies in the {Beer} Style Niche")

st.plotly_chart(fig1)

#fig = go.Figure(data=go.Bar(x = Comp_Rev.comp,y =Comp_Rev.rev))
#fig.write_html('first_figure.html', auto_open=True)
#fig.update_layout(title_text="Revenue By Company in USD")

#t.plotly_chart(fig)

#st.selectbox('Brewer', options=Brewers)
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import plotly.express as px
import csv
from bokeh.plotting import figure
import altair as alt

def load_data():
    df = pd.read_csv('top5_leagues_player.csv')
    return df

df=load_data()
max_prices = df.groupby('league')['price'].max().reset_index()

st.title('Highest Price Player in League')
st.write("In this visualization, it showcases the highest-priced players across the top 5 football leagues, using data sourced from the 'top5_leagues_player.csv' CSV file, which contains players' price information across different leagues. By analyzing this data within a DataFrame, the code determines the maximum player price within each league. The resulting bar chart offers a comparative view of the highest-priced player in each league, shedding light on the financial dynamics and player valuations prevalent in these prominent football leagues. However, it's essential to note that while the visualization identifies the highest-valued player in a specific league, it doesn't imply that the league itself is the richest. Rather, it signifies the presence of the most valued player within that league, providing a nuanced understanding of player transfers and market values within the football industry.")
fig = px.bar(max_prices, x='league', y='price')
st.plotly_chart(fig)


def plot_bar_chart(data):
    league_prices = data.groupby('league')['price'].sum().reset_index()
    chart = alt.Chart(league_prices).mark_bar().encode(
        x='league',
        y='price',
        tooltip=['league', 'price']
    ).properties(
        title='Total Price by League',
        width=700,
        height=400
    ).interactive()

    return chart

# Load data from CSV file
data = load_data()
# Display the data table

st.write("In this visualization, it's evident that the Premier League emerges as the richest league, surpassing League 1 in player valuations. Contrary to initial expectations, League 1 doesn't rank among the top three in terms of player values; instead, La Liga and the Bundesliga take those spots. This observation highlights the top-heavy nature of League 1, where player valuations are largely influenced by standout individuals like Kylian Mbappe. The visualization provides a compelling glimpse into the financial disparities and player valuation trends across these leagues, emphasizing the unique dynamics that shape the football industry's economic landscape.")
# Plot the bar chart
st.altair_chart(plot_bar_chart(data))

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
# Group data by outfitter and count unique clubs
st.title("Kit Landscape: Exploring Outfitter Distribution Across Top 5 Leagues")
clubs_per_outfitter = df.groupby('outfitter')['club'].nunique().reset_index()
clubs_per_outfitter_sorted = clubs_per_outfitter.sort_values(by='club', ascending=False)
st.write("This visualization depicts the distribution of outfitters across clubs, providing insights into the prevalence of different kit manufacturers within the top 5 leagues. Notably, Nike emerges as the dominant outfitter, with the highest number of clubs sporting their kits. Following closely behind are Adidas and Puma, contributing significantly to the clubs' apparel landscape. It's worth noting that this analysis encompasses a total of 15 distinct companies involved in producing kits for clubs across these premier leagues.")

# Create bar chart
fig = px.bar(clubs_per_outfitter_sorted, x='outfitter', y='club', title='Number of Clubs per Outfitter (Descending Order)',
             category_orders={'outfitter': clubs_per_outfitter_sorted['outfitter']})
st.plotly_chart(fig)

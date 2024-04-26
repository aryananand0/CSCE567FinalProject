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

st.title("Left Foot Vs Right Foot Market Value")
st.write("This visualization provides a comparative analysis of the market values between attacking central midfielders with left-footed and right-footed attributes. Upon examining the graph, it becomes apparent that right-footed players exhibit a higher density and overall market value compared to their left-footed counterparts. However, the gap between left-footed and right-footed players is not substantial, indicating a relatively competitive market for both types of players. One plausible explanation for the higher market value of right-footed players could be attributed to their greater representation and denser distribution within the dataset. The higher density of right-footed players contributes to a perception of higher market value, whereas the lower density of left-footed players may slightly skew the results. However, it's essential to note that left-footed players are not far behind in terms of market value, suggesting that they still hold significant value in the football market.")
st.write("Overall, this visualization offers valuable insights into the market dynamics and valuation trends for attacking central midfielders based on their dominant foot. It highlights the nuanced interplay between player attributes, market demand, and perceived value within the football industry.")
def foot_comparison_plot(Top_five_leagues_players):
    left_footed = Top_five_leagues_players[(Top_five_leagues_players['position'] == 'midfield - Attacking Midfield') & (Top_five_leagues_players['foot'] == 'left')]
    right_footed = Top_five_leagues_players[(Top_five_leagues_players['position'] == 'midfield - Attacking Midfield') & (Top_five_leagues_players['foot'] == 'right')]
    
    # Create the KDE plot
    fig, ax = plt.subplots()
    sns.kdeplot(left_footed['price'], label='Left-footed', fill=True, ax=ax)
    sns.kdeplot(right_footed['price'], label='Right-footed', fill=True, ax=ax)

    ax.set_xlabel('Market Value in Million')
    ax.set_ylabel('Density')
    ax.set_title('Market Value Comparison: Left-footed vs. Right-footed Attacking Central Midfielders')
    ax.legend()

    # Display the plot using Streamlit
    st.pyplot(fig)

# Load data from CSV file
Top_five_leagues_players = load_data()

# Call the function to plot and show statistics
foot_comparison_plot(Top_five_leagues_players)

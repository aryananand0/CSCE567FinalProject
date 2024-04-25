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
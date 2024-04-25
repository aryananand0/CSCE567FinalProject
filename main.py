import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import plotly.express as px
import csv
from bokeh.plotting import figure
import altair as alt
import pydeck as pdk
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error


st.title("Exploring Player Profiles in Europe's Top Football Leagues")
 
def load_data():
    df = pd.read_csv('top5_leagues_player.csv')
    return df

df=load_data()
st.write("## Scatter Plot from CSV")
st.write(df)

max_prices = df.groupby('league')['price'].max().reset_index()


fig = px.bar(max_prices, x='league', y='price', title=f'Highest Price Player in League')
st.plotly_chart(fig)
# Calculate the number of clubs for each outfitter
clubs_per_outfitter = df.groupby('outfitter')['club'].nunique().reset_index()

# Sidebar for outfitter selection

# Interactive pie chart for clubs by outfitter
fig = px.pie(clubs_per_outfitter, values='club', names='outfitter', title=f'Clubs per Outfitter')
st.plotly_chart(fig)




target_leagues = ['EPL', "LaLiga","Bundesliga","SerieA","Ligue1","Other"]

def average_age(name):
    target_df = df[df['league'] == name]
    average_age_target_league = target_df['age'].mean()
    average_age_one_decimal = round(average_age_target_league, 1)
    return average_age_one_decimal
ages_of_top_5_league =[]

for i in target_leagues:
    ages_of_top_5_league.append(average_age(i))
    


data = {'league': target_leagues,
        'age': ages_of_top_5_league}
df = pd.DataFrame(data)

# Create scatter plot
fig = px.scatter(df, x='league', y='age', text='age', title='Average Player Age Across Top 5 Leagues')

# Update text position
fig.update_traces(textposition='top center')

# Display the scatter plot
st.plotly_chart(fig)





with open('/Users/aryananand/Documents/CSCE567FinalProject/top5_leagues_player.csv', mode='r') as file:
    csv_reader = csv.DictReader(file)
    price_list=[]
    age_list=[]
    for row in csv_reader:
        # Debug print to check the row being processed
        
        # Extract the values for price and age from the row
        price = row['price']
        age = row['age']
        
        # Debug print to check the extracted values
        # Append the values to their respective lists
        price_list.append(price)
        age_list.append(age)

# Print the lists to see the data
df=load_data()
st.title('Average Price by age')

if 'age' in df.columns and 'price' in df.columns and df['age'].dtype in [int, float] and df['price'].dtype in [int, float]:
    # Create line plot using seaborn with hover information
    fig, ax = plt.subplots()
    sns.lineplot(data=df, x='age', y='price', ax=ax, markers=True, dashes=False)
    ax.set_title('Price vs Age')
    ax.set_xlabel('Age')
    ax.set_ylabel('Price')

    # Add hover information
    hover_data = {
        'Age': df['age'],
        'Price': df['price']
    }
    for line in ax.lines:
        line.set_picker(True)
    ax.format_xdata = lambda x: f'Age: {x:.2f}'
    ax.format_ydata = lambda y: f'Price: {y:.2f}'
    ax.legend(labels=['Price vs Age'], loc='upper left')

    # Display the plot using st.pyplot()
    st.pyplot(fig)
else:
    st.write('Error: Unable to plot. Check column names and data types.')
# Display the plot using st.pyplot()

df=load_data()
st.title('Average Price by Position')

avg_prices = df.groupby('position')['price'].mean().reset_index()

# Display bar chart using Streamlit
st.bar_chart(avg_prices.set_index('position'))

# Display title

df = load_data()

# Group by Nationality and League Affiliation and count the number of players
player_counts = df.groupby(['nationality', 'league']).size().reset_index(name='count')

# Create scatter plot with hover information
fig = px.scatter(player_counts, x='nationality', y='league', size='count', color='count',
                 hover_name='nationality', hover_data={'league': True, 'count': True},
                 title='Distribution of Players by Nationality and League Affiliation')

# Set axis labels
fig.update_xaxes(title_text='Nationality')
fig.update_yaxes(title_text='League')

# Show plot
st.plotly_chart(fig)


df = load_data()

# Calculate player counts by position
position_counts = df['position'].value_counts().reset_index()
position_counts.columns = ['Position', 'Count']

# Create bar chart for position distribution with hover information
fig = px.bar(position_counts, x='Position', y='Count',
             title='Position Distribution of Players',
             hover_data={'Position': True, 'Count': True})

# Set axis labels
fig.update_xaxes(title_text='Position')
fig.update_yaxes(title_text='Count')

# Show plot with hover information
st.plotly_chart(fig)


df = load_data()


# Create scatter plot for nationality vs. market value
fig = px.scatter(df, x='nationality', y='price',
                 title='Relationship between Player Nationality and Market Value',
                 hover_name='name', hover_data={'nationality': True, 'price': ':$,.0f'})

# Set axis labels
fig.update_xaxes(title_text='Nationality')
fig.update_yaxes(title_text='Market Value')

# Show plot
st.plotly_chart(fig)

df = load_data()
st.set_option('deprecation.showPyplotGlobalUse', False)

def foot_comparison_plot(df):
    midfield_players = df[df['position'].str.contains('midfield - Attacking Midfield')]
    left_footed = midfield_players[midfield_players['foot'] == 'left']
    right_footed = midfield_players[midfield_players['foot'] == 'right']

    sns.kdeplot(left_footed['price'], label='Left-footed', fill=True)
    sns.kdeplot(right_footed['price'], label='Right-footed', fill=True)

    plt.xlabel('Market Value in Million')
    plt.ylabel('Density')
    plt.title('Market Value Comparison: Left-footed vs. Right-footed Attacking Central Midfielders')
    plt.legend()
    st.pyplot()

# Load data
df = load_data()

# Call foot_comparison_plot function with Top_five_leagues_players DataFrame
foot_comparison_plot(df)

df = load_data()
st.write("This is demo for price vs age")
max_prices = df.groupby('age')['price'].max().reset_index()
st.line_chart(max_prices.set_index('age'))



data = load_data()
min_height = data['height'].min()
max_height = data['height'].max()
min_price = data['price'].min()
max_price = data['price'].max()

st.write("## Scatter Plot")
st.write("Height vs. Price")
filtered_data = data[(data['height'] >= min_height) & (data['height'] <= max_height) &
                     (data['price'] >= min_price) & (data['price'] <= max_price)]
st.scatter_chart(data=filtered_data, x='height', y='price')

def plot_bar_chart(data, selected_leagues):
    filtered_data = data[data['league'].isin(selected_leagues)]
    chart = alt.Chart(filtered_data).mark_bar().encode(
        x='club',
        y=alt.Y('price', title='Market Value'),
        tooltip=['club', 'price']
    ).properties(
        title='Club Market Value Comparison',
        width=700,
        height=400
    ).interactive()

    return chart

# Load data from CSV file
data = load_data()

# Display the data table
st.title('Club Market Value Comparison')


# Sidebar for selecting leagues
selected_leagues = st.sidebar.multiselect('Select Leagues', data['league'].unique())

# Plot the bar chart
st.write("## Vertical Bar Chart")
st.altair_chart(plot_bar_chart(data, selected_leagues))







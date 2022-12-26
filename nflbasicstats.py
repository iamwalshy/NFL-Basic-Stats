import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load the data into a Pandas DataFrame
df = pd.read_csv('Basic_Stats.csv')

# Group the data by team and sum the touchdowns column
df_grouped = df.groupby('team').sum()['touchdowns']

# Create the bar chart
plt.bar(df_grouped.index, df_grouped.values)
plt.xlabel('Team')
plt.ylabel('Touchdowns')

# Display the bar chart using Streamlit's st.pyplot function
st.pyplot()

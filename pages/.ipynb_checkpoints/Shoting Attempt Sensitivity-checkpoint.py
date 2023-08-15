import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

data = pd.read_csv('shotsensitivity.csv', delimiter=';')

positions = data['Position'].unique()

st.title('Shooting Attempt per Goal')
selected_position = st.selectbox('Select Position', positions)
filtered_data = data[data['Position'] == selected_position]

# Define a list of strong colors
strong_colors = ['red', 'blue', 'black', 'gray', 'yellow', 'orange']

# Create a colormap from the list of strong colors
color_map = plt.cm.colors.ListedColormap(strong_colors)

# Line graph
fig, ax = plt.subplots()
for i, col in enumerate(filtered_data.columns[2:]):
    ax.plot(filtered_data['Attempt'], filtered_data[col], label=col, color=color_map(i))

ax.set_xlabel('Shooting Attempt')
ax.set_ylabel('Predicted Goal')
ax.set_title(f'Shot Attempt Sensitivity for {selected_position}')
ax.legend()

st.pyplot(fig)

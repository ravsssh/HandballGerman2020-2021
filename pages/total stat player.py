import pandas as pd
import streamlit as st

st.subheader("Player Statistic In 2021-2022 Season :trophy:")
totalplayer_df = pd.read_csv('totalplayer_df.csv')
sort_column = st.selectbox('Sort By Descending Value:', totalplayer_df.columns)
sorted_df = totalplayer_df.sort_values(sort_column, ascending=False)
st.dataframe(sorted_df, width=None)
st.subheader("Player Specific Statistic Selection :man-playing-handball:")
selected_player = st.selectbox('Select Player:', sorted_df['Player Name'])
selected_player_df = sorted_df[sorted_df['Player Name'] == selected_player]
st.dataframe(selected_player_df, width=None)

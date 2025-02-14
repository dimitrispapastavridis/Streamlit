import streamlit as st
import pandas as pd
import plotly.express as px
import altair as alt

df = pd.read_csv('df.csv')

#st.markdown(# OB Streem Routes Dashboard)

st.markdown(
    '''
    :blue-background[OB Streem Routes Dashboard]
    '''
)

month_options = ['All'] + list(df['months'].unique())

col1, col2, col3 = st.columns(3)

selected_bu = col1.selectbox("Select BU:", df['BusinessUnit'].unique())
selected_year = col2.selectbox("Select Year:", df['years'].unique())
selected_month = col3.selectbox("Select Month:", month_options)


filtered_df = df.copy()

if selected_month != 'All':
    filtered_df = filtered_df[filtered_df["months"] == selected_month]

filtered_df = filtered_df[(filtered_df['BusinessUnit'] == selected_bu) &
                          (filtered_df['years'] == selected_year)]


filtered_df_melted = filtered_df.melt(id_vars=["months"],
                                      value_vars=["budget_routes", "actual_routes"],
                                      var_name="Type", value_name="Routes")

st.bar_chart(data=filtered_df_melted,
             x="months",
             x_label = 'Months',
             y="Routes",
             color="Type",
             use_container_width=True,
             stack=False,
             horizontal=False)

fig = px.bar(filtered_df_melted,
             x="months",
             y="Routes",
             color="Type",
             barmode='group',
             text='Routes')

fig.update_traces(textposition='outside')

st.plotly_chart(fig, use_container_width=True)



import streamlit as st
import pandas as pd

def small_header(text):
    st.markdown(f"<h4 style='text-align: center;'>{text}</h4>", unsafe_allow_html=True)

def centered_metric(label, value):
    st.markdown(
        f"""
        <div style='display: flex; justify-content: center; align-items: center; font-size: 24px;font-weight:bold'>
        <div>{value}</div>
        </div>
        """, unsafe_allow_html=True
    )

def render_metrics(filtered_df, months, month):
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        small_header('📊 Total Incidents')
        centered_metric("", filtered_df.shape[0])
    with col2:
        small_header('🏷️ Brands')
        centered_metric("", filtered_df['Brand'].nunique())
    with col3:
        small_header('📍 Countries')
        centered_metric("", filtered_df['Country'].nunique())
    with col4:
        small_header('🤝 Contact Ways') 
        centered_metric("", filtered_df['Contact Way'].nunique())

    st.markdown("<hr>", unsafe_allow_html=True)

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        small_header('📞 Total Cases')
        total_cases = filtered_df[filtered_df['Type'] == 'Cases']['Number'].sum()
        centered_metric("", total_cases)
    with col2:
        small_header('⚠️ Total Complaints')
        total_complaints = filtered_df[filtered_df['Type'] == 'Complaints']['Number'].sum()
        centered_metric("", total_complaints)
    with col3:
        small_header('🗂️ Avg. Cases/Quarter')
        # Get actual quarters present in the filtered data for cases
        cases_df = filtered_df[filtered_df['Type'] == 'Cases']
        if not cases_df.empty:
            quarterly_cases = cases_df.groupby('Quarter')['Number'].sum()
            # Calculate average based on actual number of quarters with data
            avg_cases_quarter = quarterly_cases.mean() if not quarterly_cases.empty else 0
        else:
            avg_cases_quarter = 0
        centered_metric("", int(avg_cases_quarter))
    with col4:
        small_header('📢 Avg. Complaints/Quarter')
        # Get actual quarters present in the filtered data for complaints
        complaints_df = filtered_df[filtered_df['Type'] == 'Complaints']
        if not complaints_df.empty:
            quarterly_complaints = complaints_df.groupby('Quarter')['Number'].sum()
            # Calculate average based on actual number of quarters with data
            avg_complaints_quarter = quarterly_complaints.mean() if not quarterly_complaints.empty else 0
        else:
            avg_complaints_quarter = 0
        centered_metric("", int(avg_complaints_quarter))


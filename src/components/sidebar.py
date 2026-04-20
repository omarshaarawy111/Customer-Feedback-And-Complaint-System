import streamlit as st

def sidebar_style():
    st.markdown(
        """
        <style>
            .st-emotion-cache-16txtl3 {
                padding: 3.0rem 1.5rem !important;
            }
        </style>
        """, unsafe_allow_html=True
    )

def render_sidebar(df, months, quarters):
    sidebar_style()
    st.sidebar.title('Filters')
    show_data = st.sidebar.checkbox('Show All Data', key=1)
    st.sidebar.title('Method')
    method = st.sidebar.radio('', ['Summation', 'Percentage %'], key=2)
    st.sidebar.title('Year')
    year = st.sidebar.multiselect('', sorted(df['Year'].unique()), key=10)
    st.sidebar.title('Quarter')
    quarter = st.sidebar.multiselect('', quarters, key=3)
    st.sidebar.title('Month')
    month = st.sidebar.multiselect('', months, key=4)
    st.sidebar.title('Brand')
    brand = st.sidebar.multiselect('', sorted(df['Brand'].unique()), key=5)
    st.sidebar.title('Country')
    country = st.sidebar.multiselect('', sorted(df['Country'].unique()), key=9)
    st.sidebar.title('Type')
    type_cc = st.sidebar.multiselect('', ['Cases', 'Complaints'], key=6)
    st.sidebar.title('Type Detail')
    type_detail = st.sidebar.multiselect('', sorted(df['Type Detail'].unique()), key=7)
    st.sidebar.title('Contact Way')
    contact_way = st.sidebar.multiselect('', sorted(df['Contact Way'].unique()), key=8)
    
    return show_data, method, year, quarter, month, brand, country, type_cc, type_detail, contact_way
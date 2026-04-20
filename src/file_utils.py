import pandas as pd
import chardet
from datetime import datetime
import streamlit as st

def load_and_combine_files(uploaded_files):
    dfs = []
    for uploaded_file in uploaded_files:
        try:
            if uploaded_file.name.endswith('.csv'):
                try:
                    df = pd.read_csv(uploaded_file, encoding='latin1')
                except UnicodeDecodeError:
                    raw_data = uploaded_file.read()
                    result = chardet.detect(raw_data)
                    encoding = result['encoding']
                    uploaded_file.seek(0)
                    df = pd.read_csv(uploaded_file, encoding=encoding)
            elif uploaded_file.name.endswith(('.xlsx', '.xls')):
                df = pd.read_excel(uploaded_file)
            else:
                st.warning(f"Unsupported file format: {uploaded_file.name}")
                continue
            dfs.append(df)
        except Exception as e:
            st.warning(f"Could not read file {uploaded_file.name}: {str(e)}")
            continue

    if dfs:
        combined_df = pd.concat(dfs, ignore_index=True)
        combined_df = combined_df.dropna(how='all').reset_index(drop=True)
        return combined_df
    return pd.DataFrame()

def preprocess_data(df):
    na_columns = ['Year', 'Quarter', 'Month', 'Number']
    for i in na_columns:
        df = df.dropna(subset=i)

    na_columns = ['Brand', 'Type', 'Type Detail', 'Contact Way', 'Country', 'Explanation', 'VERBATIM']
    for i in na_columns:
        df[i] = df[i].fillna('Other')
    
    months = ["January", "February", "March", "April", "May", "June",
              "July", "August", "September", "October", "November", "December"]
    quarters = ['Q1', 'Q2', 'Q3', 'Q4']
    df = df[
        df['Month'].str.lower().isin([m.lower() for m in months]) &
        df['Quarter'].str.upper().isin([q.upper() for q in quarters]) &
        df['Year'].between(2000, datetime.now().year) &
        df['Number'].apply(lambda x: isinstance(x, (int, float)) and x > 0)
    ]
    
    df['Year'] = df['Year'].astype(int)
    df['Quarter'] = df['Quarter'].astype(str).str.strip()
    df['Month'] = df['Month'].astype(str).str.strip()
    df['Brand'] = df['Brand'].astype(str).str.strip()
    df['Type'] = df['Type'].astype(str).str.strip()
    df['Type Detail'] = df['Type Detail'].astype(str).str.strip()
    df['Contact Way'] = df['Contact Way'].astype(str).str.strip()
    df['Country'] = df['Country'].astype(str).str.strip()
    df['Explanation'] = df['Explanation'].astype(str).str.strip()
    df['VERBATIM'] = df['VERBATIM'].astype(str).str.strip()
    df['Number'] = df['Number'].astype(int)
    df.drop_duplicates(inplace=True)
    df.drop(['Image 1', 'Image 2'], axis=1, errors='ignore', inplace=True)
    
    return df
import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime
import plotly.graph_objects as go

def render_visualizations(filtered_df, months, quarters, color_scheme, method="Summation"):
    # Extract visual settings from color_scheme
    # Default to transparent background
    bg_color = color_scheme.get('bg_color', 'rgba(0,0,0,0)')

    common_layout = dict(
        plot_bgcolor=bg_color,  # Only the plot grid area
        paper_bgcolor='rgba(0,0,0,0)',  # Always transparent paper background
        font=dict(size=14, family="Arial", color='black', weight='bold'),
        xaxis=dict(
            showgrid=False,
            tickfont=dict(size=12, color='black', weight='bold'),
            title_font=dict(size=14, color='black', weight='bold'),
        ),
        yaxis=dict(
            showgrid=False,
            tickfont=dict(size=14, color='black', weight='bold'),
            title_font=dict(size=16, color='black', weight='bold'),
        ),
        legend=dict(
            font=dict(size=12, color='black', weight='bold'),
            bgcolor='rgba(0,0,0,0)'  # Transparent legend background
        )
    )

    # Layout for timeline charts WITH grid lines and no background
    timeline_layout = dict(
        plot_bgcolor='rgba(0,0,0,0)',  # Transparent background
        paper_bgcolor='rgba(0,0,0,0)',  # Always transparent paper background
        font=dict(size=14, family="Arial", color='black', weight='bold'),
        xaxis=dict(
            showgrid=True,  # Show grid for timeline
            gridcolor='rgba(128,128,128,0.2)',  # Light grid color
            tickfont=dict(size=12, color='black', weight='bold'),
            title_font=dict(size=14, color='black', weight='bold'),
        ),
        yaxis=dict(
            showgrid=True,  # Show grid for timeline
            gridcolor='rgba(128,128,128,0.2)',  # Light grid color
            tickfont=dict(size=12, color='black', weight='bold'),
            title_font=dict(size=14, color='black', weight='bold'),
        ),
        legend=dict(
            font=dict(size=12, color='black', weight='bold'),
            bgcolor='rgba(0,0,0,0)'  # Transparent legend background
        )
    )

    # Helper function for percentage within group (e.g., within Month)
    def calculate_within_group_percentage(df, group_col, value_col='Number'):
        grouped = df.groupby([group_col, 'Type'])[value_col].sum().reset_index()
        group_totals = grouped.groupby(group_col)[value_col].transform('sum')
        grouped['Percentage'] = (grouped[value_col] / group_totals) * 100
        grouped['Percentage'] = grouped['Percentage'].round(0).astype(int)
        return grouped

    # Determine y-axis values based on method
    if method == 'Percentage %':
        # Monthly: Incidents by Month and Type (Percentage within Month)
        st.markdown("<h5 style='text-align: center; color: black;'><b>Incidents by Month and Type</b></h5>", unsafe_allow_html=True)
        monthly_pct = calculate_within_group_percentage(filtered_df, 'Month')
        
        fig1 = px.bar(
            monthly_pct,
            x='Month',
            y='Percentage',
            color='Type',
            barmode='group',
            category_orders={'Month': months},
            color_discrete_map={'Cases': color_scheme['Cases'], 'Complaints': color_scheme['Complaints']},
            labels={'Percentage': 'Percentage of Monthly Total (%)'},
            text='Percentage'
        )
        fig1.update_layout(
            **common_layout,
            xaxis_title='',
            yaxis_title='Percentage of Incidents (%)',
            legend_title_text='',
            hovermode='closest',
        )
        fig1.update_traces(texttemplate='%{text}%', textposition='outside')
        st.plotly_chart(fig1, use_container_width=True, key="monthly_percentage_chart")
        st.markdown("<br>", unsafe_allow_html=True)

        # Quarterly: Incidents by Quarter and Type (Percentage within Quarter)
        st.markdown("<h5 style='text-align: center; color: black;'><b>Incidents by Quarter and Type</b></h5>", unsafe_allow_html=True)
        quarter_pct = calculate_within_group_percentage(filtered_df, 'Quarter')
        
        fig_quarter = px.bar(
            quarter_pct,
            x='Quarter',
            y='Percentage',
            color='Type',
            barmode='group',
            category_orders={'Quarter': quarters},
            color_discrete_map={'Cases': color_scheme['Cases'], 'Complaints': color_scheme['Complaints']},
            labels={'Percentage': 'Percentage of Incidents (%)'},
            text='Percentage'
        )
        fig_quarter.update_layout(
            **common_layout,
            xaxis_title='',
            yaxis_title='Percentage of Quarter Total (%)',
            legend_title_text='Incident Type',
            hovermode='closest'
        )
        fig_quarter.update_traces(texttemplate='%{text}%', textposition='outside')
        st.plotly_chart(fig_quarter, use_container_width=True, key="quarterly_percentage_chart_2")
        st.markdown("<br>", unsafe_allow_html=True)

    else:  # Summation method
        # Monthly: Incidents by Month and Type
        st.markdown("<h5 style='text-align: center; color: black;'><b>Incidents by Month and Type</b></h5>", unsafe_allow_html=True)
        monthly_abs = filtered_df.groupby(['Month', 'Type'])['Number'].sum().reset_index()
        fig1 = px.bar(
            monthly_abs,
            x='Month',
            y='Number',
            color='Type',
            barmode='group',
            category_orders={'Month': months},
            color_discrete_map={'Cases': color_scheme['Cases'], 'Complaints': color_scheme['Complaints']},
            labels={'Number': 'Number of Incidents'},
            text='Number'
        )
        fig1.update_layout(
            **common_layout,
            xaxis_title='',
            yaxis_title='Number of Incidents',
            legend_title_text='',
            hovermode='closest'
        )
        fig1.update_traces(texttemplate='%{text:,.0f}', textposition='outside')
        st.plotly_chart(fig1, use_container_width=True, key="monthly_absolute_chart")
        st.markdown("<br>", unsafe_allow_html=True)

        # Quarterly: Incidents by Quarter and Type
        st.markdown("<h5 style='text-align: center; color: black;'><b>Incidents by Quarter and Type</b></h5>", unsafe_allow_html=True)
        quarter_abs = filtered_df.groupby(['Quarter', 'Type'])['Number'].sum().reset_index()
        fig_quarter = px.bar(
            quarter_abs,
            x='Quarter',
            y='Number',
            color='Type',
            barmode='group',
            category_orders={'Quarter': quarters},
            color_discrete_map={'Cases': color_scheme['Cases'], 'Complaints': color_scheme['Complaints']},
            labels={'Number': 'Number of Incidents'},
            text='Number'
        )
        fig_quarter.update_layout(
            **common_layout,
            xaxis_title='',
            yaxis_title='Number of Incidents',
            legend_title_text='',
            hovermode='closest'
        )
        fig_quarter.update_traces(texttemplate='%{text:,.0f}', textposition='outside')
        st.plotly_chart(fig_quarter, use_container_width=True, key="quarterly_absolute_chart")
        st.markdown("<br>", unsafe_allow_html=True)
  

    # Pie chart - separate row
    st.markdown("<h5 style='text-align: center; color: black;'><b>Incidents by Type</b></h5>", unsafe_allow_html=True)
    fig2 = px.pie(
        filtered_df.groupby('Type')['Number'].sum().reset_index(),
        names='Type',
        values='Number',
        color='Type',
        color_discrete_map={'Cases': color_scheme['Cases'], 'Complaints': color_scheme['Complaints']}
    )
    fig2.update_layout(**common_layout, legend_title_text='')
    fig2.update_traces(textinfo='percent+value', textposition='inside', textfont_size=14)
    st.plotly_chart(fig2, use_container_width=True, key="incidents_pie_chart")
    st.markdown("<br>", unsafe_allow_html=True)

    # Cases vs Complaints by Brand - separate row
    st.markdown("<h5 style='text-align: center; color: black;'><b>Cases vs Complaints by Brand</b></h5>", unsafe_allow_html=True)
    brand_type_df = filtered_df.groupby(['Brand', 'Type'])['Number'].sum().reset_index()

    if method == 'Percentage %':
        # Percentage within Brand
        brand_totals = brand_type_df.groupby('Brand')['Number'].sum()
        brand_type_df['Percentage'] = brand_type_df.apply(
            lambda row: (row['Number'] / brand_totals[row['Brand']]) * 100 if brand_totals[row['Brand']] > 0 else 0,
            axis=1
        )
        brand_type_df['Percentage'] = brand_type_df['Percentage'].round(0).astype(int)

        fig3 = px.bar(
            brand_type_df.sort_values('Percentage', ascending=False),
            x='Brand',
            y='Percentage',
            color='Type',
            barmode='group',
            color_discrete_map={'Cases': color_scheme['Cases'], 'Complaints': color_scheme['Complaints']},
            labels={'Percentage': 'Percentage of Incidents (%)'},
            text='Percentage'
        )
        fig3.update_traces(texttemplate='%{text}%', textposition='outside',
                            hovertemplate='<b>Brand:</b> %{x}<br><b>Type:</b> %{fullData.name}<br><b>Percentage:</b> %{y}%<extra></extra>')
    else:
        fig3 = px.bar(
            brand_type_df.sort_values('Number', ascending=False),
            x='Brand',
            y='Number',
            color='Type',
            barmode='group',
            color_discrete_map={'Cases': color_scheme['Cases'], 'Complaints': color_scheme['Complaints']},
            labels={'Number': 'Number of Incidents'},
            text='Number'
        )
        fig3.update_traces(texttemplate='%{text:,.0f}', textposition='outside',
                            hovertemplate='<b>Brand:</b> %{x}<br><b>Type:</b> %{fullData.name}<br><b>Number:</b> %{y:,.0f}<extra></extra>')

    fig3.update_layout(
        **common_layout,
        xaxis_title=None,
        yaxis_title='Percentage of Incidents (%)' if method == 'Percentage %' else 'Number of Incidents',
        legend_title_text='Incident Type',
        height=500,
        hovermode='closest'
    )
    fig3.update_xaxes(tickangle=45)
    st.plotly_chart(fig3, use_container_width=True, key="cases_complaints_by_brand_chart")
    st.markdown("<br>", unsafe_allow_html=True)

    # Cases and Complaints by Country - separate row
    st.markdown("<h5 style='text-align: center; color: black;'><b>Cases vs Complaints by Country</b></h5>", unsafe_allow_html=True)
    country_type_df = filtered_df.groupby(['Country', 'Type'])['Number'].sum().reset_index()

    if method == 'Percentage %':
        # Percentage within Country
        country_totals = country_type_df.groupby('Country')['Number'].sum()
        country_type_df['Percentage'] = country_type_df.apply(
            lambda row: (row['Number'] / country_totals[row['Country']]) * 100 if country_totals[row['Country']] > 0 else 0,
            axis=1
        )
        country_type_df['Percentage'] = country_type_df['Percentage'].round(0).astype(int)

        fig7 = px.bar(
            country_type_df.sort_values('Percentage', ascending=False),
            x='Country',
            y='Percentage',
            color='Type',
            barmode='group',
            color_discrete_map={'Cases': color_scheme['Cases'], 'Complaints': color_scheme['Complaints']},
            labels={'Percentage': 'Percentage of Incidents (%)', 'Type': 'Incident Type'},
            text='Percentage'
        )
        fig7.update_traces(texttemplate='%{text}%', textposition='outside',
                            hovertemplate='<b>Country:</b> %{x}<br><b>Type:</b> %{fullData.name}<br><b>Percentage:</b> %{y}%<extra></extra>')
    else:
        fig7 = px.bar(
            country_type_df.sort_values('Number', ascending=False),
            x='Country',
            y='Number',
            color='Type',
            barmode='group',
            color_discrete_map={'Cases': color_scheme['Cases'], 'Complaints': color_scheme['Complaints']},
            labels={'Number': 'Number of Incidents', 'Type': 'Incident Type'},
            text='Number'
        )
        fig7.update_traces(texttemplate='%{text:,.0f}', textposition='outside',
                            hovertemplate='<b>Country:</b> %{x}<br><b>Type:</b> %{fullData.name}<br><b>Number:</b> %{y:,.0f}<extra></extra>')

    fig7.update_layout(
        **common_layout,
        title=None,
        xaxis_title=None,
        yaxis_title='Percentage of Incidents (%)' if method == 'Percentage %' else 'Number of Incidents',
        legend_title_text='Incident Type',
        height=500,
        hovermode='closest'
    )
    fig7.update_xaxes(tickangle=45)
    st.plotly_chart(fig7, use_container_width=True, key="cases_complaints_by_country_chart")
    st.markdown("<br>", unsafe_allow_html=True)

        # NEW: Contact Ways by Brand and Month - separate row
    st.markdown("<h5 style='text-align: center; color: black;'><b>Contact Ways by Brand and Month</b></h5>", unsafe_allow_html=True)
    contact_brand_month_df = filtered_df.groupby(['Brand', 'Month', 'Contact Way'])['Number'].sum().reset_index()
    
    # Filter to only show months that exist in the data
    existing_months = [m for m in months if m in contact_brand_month_df['Month'].unique()]
    
    if method == 'Percentage %':
        # Calculate percentage within each brand
        brand_totals = contact_brand_month_df.groupby('Brand')['Number'].sum()
        contact_brand_month_df['Percentage'] = contact_brand_month_df.apply(
            lambda row: (row['Number'] / brand_totals[row['Brand']]) * 100 if brand_totals[row['Brand']] > 0 else 0,
            axis=1
        )
        contact_brand_month_df['Percentage'] = contact_brand_month_df['Percentage'].round(0).astype(int)

        fig_contact_brand = px.bar(
            contact_brand_month_df,
            x='Contact Way',
            y='Percentage',
            color='Month',
            barmode='group',
            facet_col='Brand',
            facet_col_wrap=min(4, len(contact_brand_month_df['Brand'].unique())),
            facet_row_spacing=0.2,
            category_orders={'Month': existing_months},
            color_discrete_sequence=color_scheme['Months'][:len(existing_months)],
            labels={'Percentage': 'Percentage of Incidents (%)'},
            text='Percentage'
        )
        fig_contact_brand.update_traces(
            texttemplate='%{text}%', 
            textposition='outside',
            width=0.15,  # REDUCED BAR WIDTH to prevent overlapping
            textfont=dict(size=9)  # Smaller annotation numbers
        )
        y_title = 'Percentage of Incidents (%)'
        y_max_val = 30  # CHANGED: Set max y-axis value to 30 for percentage
    else:
        fig_contact_brand = px.bar(
            contact_brand_month_df,
            x='Contact Way',
            y='Number',
            color='Month',
            barmode='group',
            facet_col='Brand',
            facet_col_wrap=min(4, len(contact_brand_month_df['Brand'].unique())),
            facet_row_spacing=0.2,
            category_orders={'Month': existing_months},
            color_discrete_sequence=color_scheme['Months'][:len(existing_months)],
            labels={'Number': 'Number of Incidents'},
            text='Number'
        )
        fig_contact_brand.update_traces(
            texttemplate='%{text:,.0f}', 
            textposition='outside',
            width=0.15,  # REDUCED BAR WIDTH to prevent overlapping
            textfont=dict(size=9)  # Smaller annotation numbers
        )
        y_title = 'Number of Incidents'
        # Calculate max value for proper scaling but cap at 30
        y_max_val = min(contact_brand_month_df.groupby(['Brand', 'Contact Way'])['Number'].sum().max(), 20)

    # DYNAMIC FONT SIZES BASED ON NUMBER OF SUB-GRIDS
    num_brands = len(contact_brand_month_df['Brand'].unique())
    
    # Define font sizes based on number of sub-grids
    if num_brands <= 2:
        annotation_font_size = 24  # Double size for 1-2 sub-grids
        tick_font_size = 16
        legend_font_size = 16
    elif num_brands <= 4:
        annotation_font_size = 18  # Larger for 3-4 sub-grids
        tick_font_size = 14
        legend_font_size = 14
    else:
        annotation_font_size = 14  # Default for more than 4
        tick_font_size = 10
        legend_font_size = 12

    # FIXED: Apply the exact same layout as "Incidents by Quarter per Brand"
    fig_contact_brand.update_layout(
        plot_bgcolor=bg_color,
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(size=14, family="Arial", color='black', weight='bold'),
        legend=dict(
            font=dict(size=legend_font_size, color='black', weight='bold'), 
            bgcolor='rgba(0,0,0,0)',
            title_font=dict(size=legend_font_size, color='black', weight='bold')
        ),
        yaxis_title=y_title,
        legend_title_text='Month',
        hovermode='closest',
        height=800,
        margin=dict(l=20, r=20, t=100, b=200),
        bargap=0.3,  # ADDED: Space between bars of different groups
        bargroupgap=0.4  # ADDED: Space between bars within the same group
    )
    
    # Update all x-axes to match the quarter per brand chart style
    fig_contact_brand.update_xaxes(
        matches=None,
        showticklabels=True,
        title_text='',
        tickangle=45,
        tickfont=dict(size=tick_font_size, color='black', weight='bold'),
        title_font=dict(size=14, color='black', weight='bold'),
        showgrid=False
    )
    
    # Update all y-axes to match the quarter per brand chart style
    fig_contact_brand.update_yaxes(
        tickfont=dict(size=tick_font_size, color='black', weight='bold'),
        title_font=dict(size=14, color='black', weight='bold'),
        showgrid=False,
        range=[0, 20 ]  # Add padding for text labels
    )
    
    # Update annotation styling with dynamic font sizes
    fig_contact_brand.for_each_annotation(lambda a: a.update(
        text=a.text.split("=")[-1], 
        font=dict(size=annotation_font_size, color='black', weight='bold')
    ))
    
    st.plotly_chart(fig_contact_brand, use_container_width=True, key="contact_ways_by_brand_month_chart")
    st.markdown("<br>", unsafe_allow_html=True)

    # Incidents by Type Detail (by Quarter) - ORDERED DESCENDING PER QUARTER - SIMPLIFIED (NO CASES/COMPLAINTS)
    st.markdown("<h5 style='text-align: center; color: black;'><b>Incidents by Type Detail (by Quarter)</b></h5>", unsafe_allow_html=True)
    
    # Aggregate by Type Detail and Quarter only (ignore Cases/Complaints separation)
    type_detail_df = filtered_df.groupby(['Type Detail', 'Quarter'])['Number'].sum().reset_index()

    # Check if quarter filter is applied
    quarter_filter_applied = st.session_state.get('quarter_filter_applied', False)
    
    if quarter_filter_applied:
        # When quarter filter is applied: show top 10
        top_types = type_detail_df.groupby('Type Detail')['Number'].sum().nlargest(10).index
    else:
        # When no quarter filter: show top 4
        top_types = type_detail_df.groupby('Type Detail')['Number'].sum().nlargest(4).index
        
    type_detail_df = type_detail_df[type_detail_df['Type Detail'].isin(top_types)]

    # Filter to only show quarters that exist in the data
    existing_quarters = [q for q in quarters if q in type_detail_df['Quarter'].unique()]

    # Sort Type Detail in descending order BY QUARTER
    # Create a sorted order for each quarter separately
    quarterly_sorted_details = {}
    for quarter in existing_quarters:
        quarter_data = type_detail_df[type_detail_df['Quarter'] == quarter]
        quarter_sorted = quarter_data.sort_values('Number', ascending=False)['Type Detail'].tolist()
        quarterly_sorted_details[quarter] = quarter_sorted

    # Create a comprehensive sorted list for all quarters (prioritizing most common overall)
    all_sorted_details = type_detail_df.groupby('Type Detail')['Number'].sum().sort_values(ascending=False).index.tolist()

    # SPECIAL COLOR SCHEME: Q1 and Q2 with #F9F28A, Q3 and Q4 with #E4A21F
    quarter_colors_type = []
    for quarter in existing_quarters:
        if quarter in ['Q1', 'Q2']:
            quarter_colors_type.append('#F9F28A')  # Light yellow for Q1 and Q2
        else:
            quarter_colors_type.append('#E4A21F')  # Orange for Q3 and Q4

    if method == 'Percentage %':
        # Calculate percentage within each quarter
        quarter_totals = type_detail_df.groupby('Quarter')['Number'].sum()
        type_detail_df['Percentage'] = type_detail_df.apply(
            lambda row: (row['Number'] / quarter_totals[row['Quarter']]) * 100 if quarter_totals[row['Quarter']] > 0 else 0,
            axis=1
        )
        type_detail_df['Percentage'] = type_detail_df['Percentage'].round(0).astype(int)

        fig6 = px.bar(
            type_detail_df,
            x='Type Detail',
            y='Percentage',
            color='Quarter',
            barmode='group',
            facet_col='Quarter',
            facet_col_wrap=len(existing_quarters),
            color_discrete_sequence=quarter_colors_type,
            labels={'Percentage': 'Percentage of Incidents (%)'},
            text='Percentage',
            category_orders={'Type Detail': all_sorted_details, 'Quarter': existing_quarters}
        )
        # Update each subplot to have descending order for its quarter
        for i, quarter in enumerate(existing_quarters):
            if quarter in quarterly_sorted_details:
                fig6.update_xaxes(categoryorder='array', categoryarray=quarterly_sorted_details[quarter], row=1, col=i+1)
        
        fig6.update_traces(texttemplate='%{text}%', textposition='outside',
                          hovertemplate='<b>Type Detail:</b> %{x}<br><b>Percentage:</b> %{y}%<br><b>Quarter:</b> %{fullData.name}<extra></extra>')
        y_title = 'Percentage of Incidents (%)'
    else:
        fig6 = px.bar(
            type_detail_df,
            x='Type Detail',
            y='Number',
            color='Quarter',
            barmode='group',
            facet_col='Quarter',
            facet_col_wrap=len(existing_quarters),
            color_discrete_sequence=quarter_colors_type,
            labels={'Number': 'Number of Incidents'},
            text='Number',
            category_orders={'Type Detail': all_sorted_details, 'Quarter': existing_quarters}
        )
        # Update each subplot to have descending order for its quarter - FIXED VARIABLE NAME
        for i, quarter in enumerate(existing_quarters):
            if quarter in quarterly_sorted_details:  # Fixed variable name here
                fig6.update_xaxes(categoryorder='array', categoryarray=quarterly_sorted_details[quarter], row=1, col=i+1)
        
        fig6.update_traces(texttemplate='%{text:,.0f}', textposition='outside',
                          hovertemplate='<b>Type Detail:</b> %{x}<br><b>Number:</b> %{y:,.0f}<br><b>Quarter:</b> %{fullData.name}<extra></extra>')
        y_title = 'Number of Incidents'

    fig6.update_layout(
        plot_bgcolor=bg_color,
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(size=14, family="Arial", color='black', weight='bold'),
        xaxis=dict(showgrid=False, tickfont=dict(size=10, color='black', weight='bold'), title_font=dict(size=14, color='black', weight='bold')),
        yaxis=dict(showgrid=False, tickfont=dict(size=10, color='black', weight='bold'), title_font=dict(size=14, color='black', weight='bold')),
        legend=dict(font=dict(size=12, color='black', weight='bold'), bgcolor='rgba(0,0,0,0)'),
        yaxis_title=y_title,
        legend_title_text='Quarter',
        hovermode='closest',
        height=600,
        margin=dict(l=20, r=20, t=80, b=150)
    )
    fig6.update_xaxes(
        matches=None,
        title_text='',
        tickangle=45,  # CHANGED: 180 degree angle for x-axis labels
        tickfont=dict(size=10, color='black', weight='bold'),
        title_font=dict(size=14, color='black', weight='bold'),
        showgrid=False,
        showticklabels=True
    )
    fig6.update_yaxes(
        tickfont=dict(size=10, color='black', weight='bold'),
        title_font=dict(size=14, color='black', weight='bold'),
        showgrid=False
    )
    fig6.for_each_annotation(lambda a: a.update(text=a.text.split("=")[-1], font=dict(size=16, color='black', weight='bold')))
    st.plotly_chart(fig6, use_container_width=True, key="incidents_by_type_detail_chart")
    st.markdown("<br>", unsafe_allow_html=True)

    # Top 10 Countries by Incidents - ORDERED DESCENDING PER QUARTER - COLOR PALETTE FOR QUARTERS
    st.markdown("<h5 style='text-align: center; color: black;'><b>Top 10 Countries by Incidents</b></h5>", unsafe_allow_html=True)
    country_quarter_df = filtered_df.groupby(['Country', 'Quarter'])['Number'].sum().reset_index()

    # Get top 10 countries across all data
    country_totals = country_quarter_df.groupby('Country')['Number'].sum().reset_index()
    country_totals = country_totals.sort_values('Number', ascending=False).head(10)
    all_sorted_countries = country_totals['Country'].tolist()

    country_quarter_df = country_quarter_df[country_quarter_df['Country'].isin(all_sorted_countries)]

    # Filter to only show quarters that exist in the data
    existing_quarters_country = [q for q in quarters if q in country_quarter_df['Quarter'].unique()]

    # Sort countries in descending order BY QUARTER for each subplot
    quarterly_sorted_countries = {}
    for quarter in existing_quarters_country:
        quarter_data = country_quarter_df[country_quarter_df['Quarter'] == quarter]
        quarter_sorted = quarter_data.sort_values('Number', ascending=False)['Country'].tolist()
        quarterly_sorted_countries[quarter] = quarter_sorted

    # Use overall sorted order as base
    country_quarter_df['Country'] = pd.Categorical(country_quarter_df['Country'], categories=all_sorted_countries, ordered=True)

    # SPECIAL COLOR SCHEME: Q1 and Q2 with #F9F28A, Q3 and Q4 with #E4A21F
    quarter_colors_country = []
    for quarter in existing_quarters_country:
        if quarter in ['Q1', 'Q2']:
            quarter_colors_country.append('#F9F28A')  # Light yellow for Q1 and Q2
        else:
            quarter_colors_country.append('#E4A21F')  # Orange for Q3 and Q4

    if method == 'Percentage %':
        # Percentage within Country
        country_totals_sum = country_quarter_df.groupby('Country')['Number'].sum()
        country_quarter_df['Percentage'] = country_quarter_df.apply(
            lambda row: (row['Number'] / country_totals_sum[row['Country']]) * 100 if country_totals_sum[row['Country']] > 0 else 0,
            axis=1
        )
        country_quarter_df['Percentage'] = country_quarter_df['Percentage'].round(0).astype(int)
        
        fig4 = px.bar(
            country_quarter_df,
            x='Country',
            y='Percentage',
            color='Quarter',
            barmode='group',
            facet_col='Quarter',
            facet_col_wrap=len(existing_quarters_country),
            color_discrete_sequence=quarter_colors_country,
            labels={'Percentage': 'Percentage of Incidents (%)'},
            category_orders={'Country': all_sorted_countries, 'Quarter': existing_quarters_country},
            text='Percentage'
        )
        # Update each subplot to have descending order for its quarter
        for i, quarter in enumerate(existing_quarters_country):
            if quarter in quarterly_sorted_countries:
                fig4.update_xaxes(categoryorder='array', categoryarray=quarterly_sorted_countries[quarter], row=1, col=i+1)
        
        fig4.update_traces(texttemplate='%{text}%', textposition='outside')
        y_title = 'Percentage of Incidents (%)'
    else:
        fig4 = px.bar(
            country_quarter_df,
            x='Country',
            y='Number',
            color='Quarter',
            barmode='group',
            facet_col='Quarter',
            facet_col_wrap=len(existing_quarters_country),
            color_discrete_sequence=quarter_colors_country,
            labels={'Number': 'Number of Incidents'},
            category_orders={'Country': all_sorted_countries, 'Quarter': existing_quarters_country},
            text='Number'
        )
        # Update each subplot to have descending order for its quarter
        for i, quarter in enumerate(existing_quarters_country):
            if quarter in quarterly_sorted_countries:
                fig4.update_xaxes(categoryorder='array', categoryarray=quarterly_sorted_countries[quarter], row=1, col=i+1)
        
        fig4.update_traces(texttemplate='%{y:,.0f}', textposition='outside')
        y_title = 'Number of Incidents'

    fig4.update_layout(
        plot_bgcolor=bg_color,
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(size=14, family="Arial", color='black', weight='bold'),
        xaxis=dict(showgrid=False, tickfont=dict(size=10, color='black', weight='bold'), title_font=dict(size=14, color='black', weight='bold')),
        yaxis=dict(showgrid=False, tickfont=dict(size=10, color='black', weight='bold'), title_font=dict(size=14, color='black', weight='bold')),
        legend=dict(font=dict(size=12, color='black', weight='bold'), bgcolor='rgba(0,0,0,0)'),
        yaxis_title=y_title,
        legend_title_text='Quarter',
        hovermode='closest',
        height=600,
        margin=dict(l=20, r=20, t=80, b=150)
    )
    fig4.update_xaxes(
        matches=None,
        title_text='',
        tickangle=45,
        tickfont=dict(size=10, color='black', weight='bold'),
        title_font=dict(size=14, color='black', weight='bold'),
        showgrid=False,
        showticklabels=True
    )
    fig4.update_yaxes(
        tickfont=dict(size=10, color='black', weight='bold'),
        title_font=dict(size=14, color='black', weight='bold'),
        showgrid=False
    )
    fig4.for_each_annotation(lambda a: a.update(text=a.text.split("=")[-1], font=dict(size=16, color='black', weight='bold')))
    st.plotly_chart(fig4, use_container_width=True, key="top_10_countries_chart")
    st.markdown("<br>", unsafe_allow_html=True)

    # Contact Methods by Quarter (Grouped Bar)
    st.markdown("<h5 style='text-align: center; color: black;'><b>Contact Methods by Quarter</b></h5>", unsafe_allow_html=True)
    contact_quarter_df = filtered_df.groupby(['Contact Way', 'Quarter'])['Number'].sum().reset_index()
    contact_quarter_df = contact_quarter_df.sort_values(['Quarter', 'Number'], ascending=[True, False])

    unique_contacts = contact_quarter_df['Contact Way'].unique()
    contact_colors = color_scheme['Contact'][:len(unique_contacts)]

    if method == 'Percentage %':
        # Percentage within Quarter
        quarter_totals = contact_quarter_df.groupby('Quarter')['Number'].sum()
        contact_quarter_df['Percentage'] = contact_quarter_df.apply(
            lambda row: (row['Number'] / quarter_totals[row['Quarter']]) * 100 if quarter_totals[row['Quarter']] > 0 else 0,
            axis=1
        )
        contact_quarter_df['Percentage'] = contact_quarter_df['Percentage'].round(0).astype(int)
        
        fig_contact_quarter = px.bar(
            contact_quarter_df,
            x='Quarter',
            y='Percentage',
            color='Contact Way',
            barmode='group',
            color_discrete_sequence=contact_colors,
            labels={'Percentage': 'Percentage of Incidents (%)'},
            text='Percentage'
        )
        fig_contact_quarter.update_traces(texttemplate='%{text}%', textposition='outside')
        y_title = 'Percentage of Incidents (%)'
    else:
        fig_contact_quarter = px.bar(
            contact_quarter_df,
            x='Quarter',
            y='Number',
            color='Contact Way',
            barmode='group',
            color_discrete_sequence=contact_colors,
            labels={'Number': 'Number of Incidents'},
            text='Number'
        )
        fig_contact_quarter.update_traces(texttemplate='%{y:,.0f}', textposition='outside')
        y_title = 'Number of Incidents'

    fig_contact_quarter.update_layout(
        **common_layout,
        xaxis_title='',
        yaxis_title=y_title,
        legend_title_text='Contact Way',
        height=500,
        hovermode='closest'
    )
    fig_contact_quarter.update_xaxes(tickangle=0)
    st.plotly_chart(fig_contact_quarter, use_container_width=True, key="contact_methods_by_quarter_chart")
    st.markdown("<br>", unsafe_allow_html=True)

    # Incidents by Quarter per Brand - Split by Cases and Complaints
    st.markdown("<h5 style='text-align: center; color: black;'><b>Incidents by Quarter per Brand</b></h5>", unsafe_allow_html=True)
    quarter_brand_type_df = filtered_df.groupby(['Quarter', 'Brand', 'Type'])['Number'].sum().reset_index()
    quarter_brand_type_df = quarter_brand_type_df.sort_values(['Brand', 'Quarter', 'Type'], ascending=[True, True, True])
    quarter_brand_type_df['Quarter'] = pd.Categorical(
        quarter_brand_type_df['Quarter'],
        categories=[q for q in quarters if q in quarter_brand_type_df['Quarter'].unique()],
        ordered=True
    )
    unique_brands = quarter_brand_type_df['Brand'].unique()

    if method == 'Percentage %':
        # Calculate percentage for each quarter within the brand's total
        brand_totals = quarter_brand_type_df.groupby('Brand')['Number'].sum()
        quarter_brand_type_df['Percentage'] = quarter_brand_type_df.apply(
            lambda row: (row['Number'] / brand_totals[row['Brand']]) * 100 if brand_totals[row['Brand']] > 0 else 0,
            axis=1
        )
        quarter_brand_type_df['Percentage'] = quarter_brand_type_df['Percentage'].round(0).astype(int)
        y_max_val = 100
        y_axis_title = 'Percentage of Incidents (%)'

        fig11 = px.bar(
            quarter_brand_type_df,
            x='Quarter',
            y='Percentage',
            color='Type',
            barmode='group',  # Grouped bars for Cases and Complaints
            facet_col='Brand',
            facet_col_wrap=min(4, len(unique_brands)),
            facet_row_spacing=0.2,
            color_discrete_map={'Cases': color_scheme['Cases'], 'Complaints': color_scheme['Complaints']},
            labels={'Percentage': y_axis_title, 'Quarter': ''},
            text='Percentage'
        )
        # Set a fixed width to prevent bars from being too thin and ensure full height display
        fig11.update_traces(width=0.4, texttemplate='%{text}%', textposition='outside')
    else: # Summation
        y_max_val = quarter_brand_type_df.groupby(['Brand', 'Quarter'])['Number'].sum().max()
        y_axis_title = 'Number of Incidents'
        
        fig11 = px.bar(
            quarter_brand_type_df,
            x='Quarter',
            y='Number',
            color='Type',
            barmode='group',  # Grouped bars for Cases and Complaints
            facet_col='Brand',
            facet_col_wrap=min(4, len(unique_brands)),
            facet_row_spacing=0.2,
            color_discrete_map={'Cases': color_scheme['Cases'], 'Complaints': color_scheme['Complaints']},
            labels={'Number': y_axis_title, 'Quarter': ''},
            text='Number'
        )
        # Set a fixed width to prevent bars from being too thin and ensure full height display
        fig11.update_traces(width=0.4, texttemplate='%{text:,.0f}', textposition='outside')

    fig11.update_layout(
        plot_bgcolor=bg_color,
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(size=14, family="Arial", color='black', weight='bold'),
        legend=dict(font=dict(size=12, color='black', weight='bold'), bgcolor='rgba(0,0,0,0)'),
        yaxis_title=y_axis_title,
        legend_title_text='Incident Type',
        hovermode='closest',
        height=800,
        margin=dict(l=20, r=20, t=100, b=200)
    )
    fig11.for_each_annotation(lambda a: a.update(text=a.text.split("=")[-1], font=dict(size=12, color='black', weight='bold')))
    
    fig11.update_xaxes(
        matches=None,
        showticklabels=True,
        title_text='',
        tickangle=0,
        tickfont=dict(size=10, color='black', weight='bold'),
        title_font=dict(size=14, color='black', weight='bold')
    )
    fig11.update_yaxes(
        tickfont=dict(size=10, color='black', weight='bold'),
        title_font=dict(size=14, color='black', weight='bold'),
        showgrid=False, 
        range=[0, y_max_val * 1.3]
    )
    st.plotly_chart(fig11, use_container_width=True, key="quarter_per_brand_chart")
    st.markdown("<br>", unsafe_allow_html=True)

    # Timeline charts
    try:
        if 'Date' not in filtered_df.columns:
            filtered_df['Month'] = pd.Categorical(filtered_df['Month'], categories=months, ordered=True)
            filtered_df['Month_Num'] = filtered_df['Month'].apply(lambda x: months.index(x) + 1)
            filtered_df['Date'] = pd.to_datetime(
                filtered_df['Year'].astype(str) + '-' +
                filtered_df['Month_Num'].astype(str) + '-01'
            )

        timeline_df = filtered_df.groupby(['Date', 'Type'])['Number'].sum().reset_index()
        if method == 'Percentage %':
            monthly_totals = timeline_df.groupby('Date')['Number'].sum()
            timeline_df['Percentage'] = timeline_df.apply(
                lambda row: (row['Number'] / monthly_totals[row['Date']]) * 100 if monthly_totals[row['Date']] > 0 else 0,
                axis=1
            )
            timeline_df['Percentage'] = timeline_df['Percentage'].round(0).astype(int)
            
            st.markdown("<h5 style='text-align: center; color: black;'><b>Monthly Incidents Timeline by Type</b></h5>", unsafe_allow_html=True)
            fig15 = px.line(
                timeline_df,
                x='Date',
                y='Percentage',
                color='Type',
                markers=True,
                color_discrete_map={'Cases': color_scheme['Cases'], 'Complaints': color_scheme['Complaints']}
            )
            
            fig15.update_traces(
                line=dict(width=4, shape='spline', smoothing=1.3),
                marker=dict(size=8, line=dict(width=2, color='Black')),
                hovertemplate='<b>Date:</b> %{x}<br><b>Percentage:</b> %{y}%<br><extra></extra>'
            )
            
            fig15.update_layout(
                **timeline_layout,
                xaxis_title='Date',
                yaxis_title='Percentage of Incidents (%)',
                legend_title_text='Incident Type',
                height=400
            )
        else:
            st.markdown("<h5 style='text-align: center; color: black;'><b>Monthly Incidents Timeline by Type</b></h5>", unsafe_allow_html=True)
            fig15 = px.line(
                timeline_df,
                x='Date',
                y='Number',
                color='Type',
                markers=True,
                color_discrete_map={'Cases': color_scheme['Cases'], 'Complaints': color_scheme['Complaints']}
            )
            
            fig15.update_traces(
                line=dict(width=4, shape='spline', smoothing=1.3),
                marker=dict(size=8, line=dict(width=2, color='Black')),
                hovertemplate='<b>Date:</b> %{x}<br><b>Count:</b> %{y:,}<br><extra></extra>'
            )
            
            fig15.update_layout(
                **timeline_layout,
                xaxis_title='Date',
                yaxis_title='Number of Incidents',
                legend_title_text='Incident Type',
                height=400
            )
        st.plotly_chart(fig15, use_container_width=True, key="monthly_timeline_chart")
        st.markdown("<br>", unsafe_allow_html=True)
    except Exception as e:
        st.warning(f"Could not create timeline chart: {str(e)}")

    try:
        if 'Quarter_Date' not in filtered_df.columns:
            quarter_map = {'Q1': 1, 'Q2': 4, 'Q3': 7, 'Q4': 10}
            filtered_df['Quarter_Start_Month'] = filtered_df['Quarter'].map(quarter_map)
            filtered_df['Quarter_Date'] = pd.to_datetime(
                filtered_df['Year'].astype(str) + '-' +
                filtered_df['Quarter_Start_Month'].astype(str) + '-01'
            )

        quarter_timeline_df = filtered_df.groupby(['Quarter_Date', 'Type'])['Number'].sum().reset_index()
        if method == 'Percentage %':
            quarterly_totals = quarter_timeline_df.groupby('Quarter_Date')['Number'].sum()
            quarter_timeline_df['Percentage'] = quarter_timeline_df.apply(
                lambda row: (row['Number'] / quarterly_totals[row['Quarter_Date']]) * 100 if quarterly_totals[row['Quarter_Date']] > 0 else 0,
                axis=1
            )
            quarter_timeline_df['Percentage'] = quarter_timeline_df['Percentage'].round(0).astype(int)
            
            st.markdown("<h5 style='text-align: center; color: black;'><b>Quarterly Incidents Timeline by Type</b></h5>", unsafe_allow_html=True)
            fig16 = px.line(
                quarter_timeline_df,
                x='Quarter_Date',
                y='Percentage',
                color='Type',
                markers=True,
                color_discrete_map={'Cases': color_scheme['Cases'], 'Complaints': color_scheme['Complaints']}
            )
            
            fig16.update_traces(
                line=dict(width=4, shape='spline', smoothing=1.3),
                marker=dict(size=8, line=dict(width=2, color='Black')),
                hovertemplate='<b>Date:</b> %{x}<br><b>Percentage:</b> %{y}%<br><extra></extra>'
            )
            
            fig16.update_layout(
                **timeline_layout,
                xaxis_title='Date',
                yaxis_title='Percentage of Incidents (%)',
                legend_title_text='Incident Type',
                height=400
            )
        else:
            st.markdown("<h5 style='text-align: center; color: black;'><b>Quarterly Incidents Timeline by Type</b></h5>", unsafe_allow_html=True)
            fig16 = px.line(
                quarter_timeline_df,
                x='Quarter_Date',
                y='Number',
                color='Type',
                markers=True,
                color_discrete_map={'Cases': color_scheme['Cases'], 'Complaints': color_scheme['Complaints']}
            )
            
            fig16.update_traces(
                line=dict(width=4, shape='spline', smoothing=1.3),
                marker=dict(size=8, line=dict(width=2, color='Black')),
                hovertemplate='<b>Date:</b> %{x}<br><b>Count:</b> %{y:,}<br><extra></extra>'
            )
            
            fig16.update_layout(
                **timeline_layout,
                xaxis_title='Date',
                yaxis_title='Number of Incidents',
                legend_title_text='Incident Type',
                height=400
            )
        st.plotly_chart(fig16, use_container_width=True, key="quarterly_timeline_chart")
        st.markdown("<br>", unsafe_allow_html=True)
    except Exception as e:
        st.warning(f"Could not create quarterly timeline chart: {str(e)}")
import pandas as pd
import plotly.express as px
from datetime import datetime
import base64

def create_download_link(val, filename):
    b64 = base64.b64encode(val.encode()).decode()
    return f'<a href="data:application/octet-stream;base64,{b64}" download="{filename}.html">Download HTML Report</a>'

def plot_to_html(fig):
    return fig.to_html(full_html=False, include_plotlyjs='cdn')

def generate_html_report(filtered_df, month, quarter, year, brand, type_cc, type_detail, contact_way, country, color_scheme, method="Summation"):
    month_names = "+".join(month) if month else "All Months"
    month_names_pdf = "+".join(month) if month else "All_Months"
    quarter_names = "+".join(quarter) if quarter else "All Quarters"
    quarter_names_pdf = "+".join(quarter) if quarter else "All_Quarters"
    year_names = "+".join(map(str, year)) if year else "All Years"
    year_names_pdf = "+".join(map(str, year)) if year else "All_Years"
    brand_names = "+".join(brand) if brand else "All Brands"
    brand_names_pdf = "+".join(brand) if brand else "All_Brands"
    report_name = f"Customer_Feedback_And_Complaint_System_{month_names_pdf}_{quarter_names_pdf}_{year_names_pdf}_{brand_names_pdf}_report"
    
    total_incidents = filtered_df.shape[0]
    total_brands = filtered_df['Brand'].nunique()
    total_countries = filtered_df['Country'].nunique()
    total_contact_ways = filtered_df['Contact Way'].nunique()
    total_cases = filtered_df[filtered_df['Type'] == 'Cases']['Number'].sum()
    total_complaints = filtered_df[filtered_df['Type'] == 'Complaints']['Number'].sum()
    
    monthly_cases = filtered_df[filtered_df['Type'] == 'Cases'].groupby('Month')['Number'].sum()
    monthly_complaints = filtered_df[filtered_df['Type'] == 'Complaints'].groupby('Month')['Number'].sum()
    months_order = ["January", "February", "March", "April", "May", "June",
                    "July", "August", "September", "October", "November", "December"]
    if month:
        months_order = [m for m in months_order if m in month]
    monthly_cases_df = pd.DataFrame(index=months_order)
    monthly_cases_df['Cases'] = monthly_cases.reindex(months_order, fill_value=0)
    monthly_complaints_df = pd.DataFrame(index=months_order)
    monthly_complaints_df['Complaints'] = monthly_complaints.reindex(months_order, fill_value=0)
    avg_cases_month = monthly_cases_df['Cases'].mean() if not monthly_cases_df.empty else 0
    avg_complaints_month = monthly_complaints_df['Complaints'].mean() if not monthly_complaints_df.empty else 0
    
    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Customer Feedback And Complaint System Report</title>
        <script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
        <style>
            body {{
                font-family: Arial, sans-serif;
                margin: 20px;
                color: #333;
            }}
            .header {{
                background-color: #005ca1;
                color: white;
                padding: 15px;
                text-align: center;
                margin-bottom: 20px;
                border-radius: 5px;
            }}
            .report-details {{
                text-align: center;
                margin-bottom: 30px;
                font-size: 14px;
                color: #555;
            }}
            .section-title {{
                color: #005ca1;
                border-bottom: 2px solid #005ca1;
                padding-bottom: 5px;
                margin-top: 30px;
                margin-bottom: 15px;
            }}
            .metrics-grid {{
                display: grid;
                grid-template-columns: repeat(4, 1fr);
                gap: 15px;
                margin-bottom: 30px;
            }}
            .metric-card {{
                border: 1px solid #ddd;
                border-radius: 5px;
                padding: 15px;
                text-align: center;
                box-shadow: 0 2px 5px rgba(0,0,0,0.1);
            }}
            .metric-title {{
                font-weight: bold;
                color: #005ca1;
                margin-bottom: 10px;
                font-size: 14px;
            }}
            .metric-value {{
                font-size: 24px;
                font-weight: bold;
            }}
            .footer {{
                margin-top: 50px;
                text-align: center;
                font-size: 12px;
                color: #005ca1;
            }}
            .visualization {{
                margin: 30px 0;
                border: 1px solid #eee;
                padding: 15px;
                border-radius: 5px;
            }}
            .visualization-title {{
                text-align: center;
                font-weight: bold;
                margin-bottom: 15px;
                color: #005ca1;
                font-size: 18px;
            }}
            .chart-container {{
                width: 100%;
            }}
            .method-badge {{
                background-color: #005ca1;
                color: white;
                padding: 5px 10px;
                border-radius: 15px;
                font-size: 12px;
                margin-left: 10px;
            }}
        </style>
    </head>
    <body>
        <div class="header">
            <h1>Customer Feedback And Complaint System Report</h1>
            <div class="method-badge">Method: {method}</div>
        </div>
        
        <div class="report-details">
            <p><strong>Generated on:</strong> {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
            <p><strong>Month:</strong> {month_names.replace('+', ', ')}</p>
            <p><strong>Quarter:</strong> {quarter_names.replace('+', ', ')}</p>
            <p><strong>Year:</strong> {year_names.replace('+', ', ')}</p>
            <p><strong>Brand:</strong> {brand_names.replace('+', ', ')}</p>
        </div>
        
        <h2 class="section-title">Key Metrics</h2>
        <div class="metrics-grid">
            <div class="metric-card">
                <div class="metric-title">📊 Total Incidents</div>
                <div class="metric-value">{total_incidents}</div>
            </div>
            <div class="metric-card">
                <div class="metric-title">🏷️ Total Brands</div>
                <div class="metric-value">{total_brands}</div>
            </div>
            <div class="metric-card">
                <div class="metric-title">📍 Total Countries</div>
                <div class="metric-value">{total_countries}</div>
            </div>
            <div class="metric-card">
                <div class="metric-title">🤝 Contact Ways</div>
                <div class="metric-value">{total_contact_ways}</div>
            </div>
            <div class="metric-card">
                <div class="metric-title">📞 Total Cases</div>
                <div class="metric-value">{total_cases}</div>
            </div>
            <div class="metric-card">
                <div class="metric-title">⚠️ Total Complaints</div>
                <div class="metric-value">{total_complaints}</div>
            </div>
            <div class="metric-card">
                <div class="metric-title">🗂️ Avg. Cases/Month</div>
                <div class="metric-value">{int(avg_cases_month)}</div>
            </div>
            <div class="metric-card">
                <div class="metric-title">📢 Avg. Complaints/Month</div>
                <div class="metric-value">{int(avg_complaints_month)}</div>
            </div>
        </div>
        
        <h2 class="section-title">Visualizations</h2>
    """
    
    months = ["January", "February", "March", "April", "May", "June",
              "July", "August", "September", "October", "November", "December"]
    quarters = ['Q1', 'Q2', 'Q3', 'Q4']
    
    bg_color = color_scheme.get('bg_color', 'rgba(0,0,0,0)')
    
    common_layout = dict(
        plot_bgcolor=bg_color,
        paper_bgcolor='rgba(0,0,0,0)',
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
            bgcolor='rgba(0,0,0,0)'
        )
    )
    
    timeline_layout = dict(
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(size=14, family="Arial", color='black', weight='bold'),
        xaxis=dict(
            showgrid=True,
            gridcolor='rgba(128,128,128,0.2)',
            tickfont=dict(size=12, color='black', weight='bold'),
            title_font=dict(size=14, color='black', weight='bold'),
        ),
        yaxis=dict(
            showgrid=True,
            gridcolor='rgba(128,128,128,0.2)',
            tickfont=dict(size=12, color='black', weight='bold'),
            title_font=dict(size=14, color='black', weight='bold'),
        ),
        legend=dict(
            font=dict(size=12, color='black', weight='bold'),
            bgcolor='rgba(0,0,0,0)'
        )
    )

    # Helper function for percentage within group
    def calculate_within_group_percentage(df, group_col, value_col='Number'):
        grouped = df.groupby([group_col, 'Type'])[value_col].sum().reset_index()
        group_totals = grouped.groupby(group_col)[value_col].transform('sum')
        grouped['Percentage'] = (grouped[value_col] / group_totals) * 100
        grouped['Percentage'] = grouped['Percentage'].round(0).astype(int)
        return grouped

    # 1. Monthly: Incidents by Month and Type
    if method == 'Percentage %':
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
    else:
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

    html += f"""
    <div class="visualization">
        <div class="visualization-title">Incidents by Month and Type</div>
        <div class="chart-container">{plot_to_html(fig1)}</div>
    </div>
    """

    # 2. Quarterly: Incidents by Quarter and Type
    if method == 'Percentage %':
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
    else:
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

    html += f"""
    <div class="visualization">
        <div class="visualization-title">Incidents by Quarter and Type</div>
        <div class="chart-container">{plot_to_html(fig_quarter)}</div>
    </div>
    """

    # 3. Pie chart - Incidents by Type
    fig2 = px.pie(
        filtered_df.groupby('Type')['Number'].sum().reset_index(),
        names='Type',
        values='Number',
        color='Type',
        color_discrete_map={'Cases': color_scheme['Cases'], 'Complaints': color_scheme['Complaints']}
    )
    fig2.update_layout(**common_layout, legend_title_text='')
    fig2.update_traces(textinfo='percent+value', textposition='inside', textfont_size=14)
    
    html += f"""
    <div class="visualization">
        <div class="visualization-title">Incidents by Type</div>
        <div class="chart-container">{plot_to_html(fig2)}</div>
    </div>
    """

    # 4. Cases vs Complaints by Brand
    brand_type_df = filtered_df.groupby(['Brand', 'Type'])['Number'].sum().reset_index()

    if method == 'Percentage %':
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
        fig3.update_traces(texttemplate='%{text}%', textposition='outside')
        y_title = 'Percentage of Incidents (%)'
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
        fig3.update_traces(texttemplate='%{text:,.0f}', textposition='outside')
        y_title = 'Number of Incidents'

    fig3.update_layout(
        **common_layout,
        xaxis_title=None,
        yaxis_title=y_title,
        legend_title_text='Incident Type',
        height=650,
        hovermode='closest'
    )
    fig3.update_xaxes(tickangle=45)
    
    html += f"""
    <div class="visualization" style="height:700px">
        <div class="visualization-title">Cases vs Complaints by Brand</div>
        <div class="chart-container">{plot_to_html(fig3)}</div>
    </div>
    """

    # 5. Cases and Complaints by Country
    country_type_df = filtered_df.groupby(['Country', 'Type'])['Number'].sum().reset_index()

    if method == 'Percentage %':
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
        fig7.update_traces(texttemplate='%{text}%', textposition='outside')
        y_title = 'Percentage of Incidents (%)'
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
        fig7.update_traces(texttemplate='%{text:,.0f}', textposition='outside')
        y_title = 'Number of Incidents'

    fig7.update_layout(
        **common_layout,
        xaxis_title=None,
        yaxis_title=y_title,
        legend_title_text='Incident Type',
        height=500,
        hovermode='closest'
    )
    fig7.update_xaxes(tickangle=0)
    
    html += f"""
    <div class="visualization">
        <div class="visualization-title">Cases vs Complaints by Country</div>
        <div class="chart-container">{plot_to_html(fig7)}</div>
    </div>
    """

    # 6. Contact Ways by Brand and Month - WITH DYNAMIC FONT SIZES
    contact_brand_month_df = filtered_df.groupby(['Brand', 'Month', 'Contact Way'])['Number'].sum().reset_index()
    existing_months = [m for m in months if m in contact_brand_month_df['Month'].unique()]
    
    if method == 'Percentage %':
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
            width=0.15,
            textfont=dict(size=9)
        )
        y_title = 'Percentage of Incidents (%)'
        y_max_val = 100
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
            width=0.15,
            textfont=dict(size=9)
        )
        y_title = 'Number of Incidents'
        y_max_val = contact_brand_month_df.groupby(['Brand', 'Contact Way'])['Number'].sum().max()

    # DYNAMIC FONT SIZES BASED ON NUMBER OF SUB-GRIDS
    num_brands = len(contact_brand_month_df['Brand'].unique())
    
    if num_brands <= 2:
        annotation_font_size = 24
        tick_font_size = 16
        legend_font_size = 16
    elif num_brands <= 4:
        annotation_font_size = 18
        tick_font_size = 14
        legend_font_size = 14
    else:
        annotation_font_size = 14
        tick_font_size = 10
        legend_font_size = 12

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
        bargap=0.3,
        bargroupgap=0.4
    )
    
    fig_contact_brand.update_xaxes(
        matches=None,
        showticklabels=True,
        title_text='',
        tickangle=45,
        tickfont=dict(size=tick_font_size, color='black', weight='bold'),
        title_font=dict(size=14, color='black', weight='bold'),
        showgrid=False
    )
    
    fig_contact_brand.update_yaxes(
        tickfont=dict(size=tick_font_size, color='black', weight='bold'),
        title_font=dict(size=14, color='black', weight='bold'),
        showgrid=False,
        range=[0, y_max_val * 1.3]
    )
    
    fig_contact_brand.for_each_annotation(lambda a: a.update(
        text=a.text.split("=")[-1], 
        font=dict(size=annotation_font_size, color='black', weight='bold')
    ))
    
    html += f"""
    <div class="visualization">
        <div class="visualization-title">Contact Ways by Brand and Month</div>
        <div class="chart-container">{plot_to_html(fig_contact_brand)}</div>
    </div>
    """

    # 7. Incidents by Type Detail (by Quarter) - WITH SPECIAL COLOR SCHEME AND 180 DEGREE TICKS
    type_detail_df = filtered_df.groupby(['Type Detail', 'Quarter'])['Number'].sum().reset_index()

    # Check if quarter filter is applied (simulate the session state logic)
    quarter_filter_applied = bool(quarter)
    
    if quarter_filter_applied:
        # When quarter filter is applied: show top 10
        top_types = type_detail_df.groupby('Type Detail')['Number'].sum().nlargest(10).index
    else:
        # When no quarter filter: show top 4
        top_types = type_detail_df.groupby('Type Detail')['Number'].sum().nlargest(4).index
        
    type_detail_df = type_detail_df[type_detail_df['Type Detail'].isin(top_types)]

    existing_quarters = [q for q in quarters if q in type_detail_df['Quarter'].unique()]

    # Sort Type Detail in descending order BY QUARTER
    quarterly_sorted_details = {}
    for quarter_name in existing_quarters:
        quarter_data = type_detail_df[type_detail_df['Quarter'] == quarter_name]
        quarter_sorted = quarter_data.sort_values('Number', ascending=False)['Type Detail'].tolist()
        quarterly_sorted_details[quarter_name] = quarter_sorted

    all_sorted_details = type_detail_df.groupby('Type Detail')['Number'].sum().sort_values(ascending=False).index.tolist()

    # SPECIAL COLOR SCHEME: Q1 and Q2 with #F9F28A, Q3 and Q4 with #E4A21F
    quarter_colors_type = []
    for quarter_name in existing_quarters:
        if quarter_name in ['Q1', 'Q2']:
            quarter_colors_type.append('#F9F28A')  # Light yellow for Q1 and Q2
        else:
            quarter_colors_type.append('#E4A21F')  # Orange for Q3 and Q4

    if method == 'Percentage %':
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
            labels={'Percentage': '', 'Type Detail': ''},
            text='Percentage',
            category_orders={'Type Detail': all_sorted_details, 'Quarter': existing_quarters}
        )
        # Update each subplot to have descending order for its quarter
        for i, quarter_name in enumerate(existing_quarters):
            if quarter_name in quarterly_sorted_details:
                fig6.update_xaxes(categoryorder='array', categoryarray=quarterly_sorted_details[quarter_name], row=1, col=i+1)
        
        fig6.update_traces(texttemplate='%{text}%', textposition='outside')
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
            labels={'Number': '', 'Type Detail': ''},
            text='Number',
            category_orders={'Type Detail': all_sorted_details, 'Quarter': existing_quarters}
        )
        # Update each subplot to have descending order for its quarter
        for i, quarter_name in enumerate(existing_quarters):
            if quarter_name in quarterly_sorted_details:
                fig6.update_xaxes(categoryorder='array', categoryarray=quarterly_sorted_details[quarter_name], row=1, col=i+1)
        
        fig6.update_traces(texttemplate='%{text:,.0f}', textposition='outside')

    fig6.update_layout(
        plot_bgcolor=bg_color,
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(size=14, family="Arial", color='black', weight='bold'),
        xaxis=dict(showgrid=False, tickfont=dict(size=10, color='black', weight='bold'), title_font=dict(size=14, color='black', weight='bold')),
        yaxis=dict(showgrid=False, tickfont=dict(size=10, color='black', weight='bold'), title_font=dict(size=14, color='black', weight='bold')),
        legend=dict(font=dict(size=12, color='black', weight='bold'), bgcolor='rgba(0,0,0,0)'),
        yaxis_title=' ',
        legend_title_text='Quarter',
        hovermode='closest',
        height=600,
        margin=dict(l=20, r=20, t=80, b=150)
    )
    fig6.update_xaxes(
        matches=None,
        title_text='',
        tickangle=45,  # 180 degree angle for x-axis labels
        tickfont=dict(size=10, color='black', weight='bold'),
        title_font=dict(size=14, color='black', weight='bold'),
        showgrid=False,
        showticklabels=True
    )
    fig6.update_yaxes(
        tickfont=dict(size=10, color='black', weight='bold'),
        title_font=dict(size=14, color='black', weight='bold'),
        showgrid=False,
        title_text=''
    )
    fig6.for_each_annotation(lambda a: a.update(text=a.text.split("=")[-1], font=dict(size=16, color='black', weight='bold')))
    
    html += f"""
    <div class="visualization">
        <div class="visualization-title">Incidents by Type Detail (by Quarter)</div>
        <div class="chart-container">{plot_to_html(fig6)}</div>
    </div>
    """

    # 8. Top 10 Countries by Incidents - WITH SPECIAL COLOR SCHEME
    country_quarter_df = filtered_df.groupby(['Country', 'Quarter'])['Number'].sum().reset_index()
    country_totals = country_quarter_df.groupby('Country')['Number'].sum().reset_index()
    country_totals = country_totals.sort_values('Number', ascending=False).head(10)
    all_sorted_countries = country_totals['Country'].tolist()
    country_quarter_df = country_quarter_df[country_quarter_df['Country'].isin(all_sorted_countries)]
    existing_quarters_country = [q for q in quarters if q in country_quarter_df['Quarter'].unique()]

    # Sort countries in descending order BY QUARTER for each subplot
    quarterly_sorted_countries = {}
    for quarter_name in existing_quarters_country:
        quarter_data = country_quarter_df[country_quarter_df['Quarter'] == quarter_name]
        quarter_sorted = quarter_data.sort_values('Number', ascending=False)['Country'].tolist()
        quarterly_sorted_countries[quarter_name] = quarter_sorted

    country_quarter_df['Country'] = pd.Categorical(country_quarter_df['Country'], categories=all_sorted_countries, ordered=True)

    # SPECIAL COLOR SCHEME: Q1 and Q2 with #F9F28A, Q3 and Q4 with #E4A21F
    quarter_colors_country = []
    for quarter_name in existing_quarters_country:
        if quarter_name in ['Q1', 'Q2']:
            quarter_colors_country.append('#F9F28A')  # Light yellow for Q1 and Q2
        else:
            quarter_colors_country.append('#E4A21F')  # Orange for Q3 and Q4

    if method == 'Percentage %':
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
            labels={'Percentage': '', 'Country': ''},
            category_orders={'Country': all_sorted_countries, 'Quarter': existing_quarters_country},
            text='Percentage'
        )
        # Update each subplot to have descending order for its quarter
        for i, quarter_name in enumerate(existing_quarters_country):
            if quarter_name in quarterly_sorted_countries:
                fig4.update_xaxes(categoryorder='array', categoryarray=quarterly_sorted_countries[quarter_name], row=1, col=i+1)
        
        fig4.update_traces(texttemplate='%{text}%', textposition='outside')
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
            labels={'Number': '', 'Country': ''},
            category_orders={'Country': all_sorted_countries, 'Quarter': existing_quarters_country},
            text='Number'
        )
        # Update each subplot to have descending order for its quarter
        for i, quarter_name in enumerate(existing_quarters_country):
            if quarter_name in quarterly_sorted_countries:
                fig4.update_xaxes(categoryorder='array', categoryarray=quarterly_sorted_countries[quarter_name], row=1, col=i+1)
        
        fig4.update_traces(texttemplate='%{y:,.0f}', textposition='outside')

    fig4.update_layout(
        plot_bgcolor=bg_color,
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(size=14, family="Arial", color='black', weight='bold'),
        xaxis=dict(showgrid=False, tickfont=dict(size=10, color='black', weight='bold'), title_font=dict(size=14, color='black', weight='bold')),
        yaxis=dict(showgrid=False, tickfont=dict(size=10, color='black', weight='bold'), title_font=dict(size=14, color='black', weight='bold')),
        legend=dict(font=dict(size=12, color='black', weight='bold'), bgcolor='rgba(0,0,0,0)'),
        yaxis_title=' ',
        legend_title_text='Quarter',
        hovermode='closest',
        height=600,
        margin=dict(l=20, r=20, t=80, b=150)
    )
    fig4.update_xaxes(
        matches=None,
        title_text='',
        tickangle=0,
        tickfont=dict(size=10, color='black', weight='bold'),
        title_font=dict(size=14, color='black', weight='bold'),
        showgrid=False,
        showticklabels=True
    )
    fig4.update_yaxes(
        tickfont=dict(size=10, color='black', weight='bold'),
        title_font=dict(size=14, color='black', weight='bold'),
        showgrid=False,
        title_text=''
    )
    fig4.for_each_annotation(lambda a: a.update(text=a.text.split("=")[-1], font=dict(size=16, color='black', weight='bold')))
    
    html += f"""
    <div class="visualization">
        <div class="visualization-title">Top 10 Countries by Incidents</div>
        <div class="chart-container">{plot_to_html(fig4)}</div>
    </div>
    """

    # 9. Contact Methods by Quarter
    contact_quarter_df = filtered_df.groupby(['Contact Way', 'Quarter'])['Number'].sum().reset_index()
    contact_quarter_df = contact_quarter_df.sort_values(['Quarter', 'Number'], ascending=[True, False])

    unique_contacts = contact_quarter_df['Contact Way'].unique()
    contact_colors = color_scheme['Contact'][:len(unique_contacts)]

    if method == 'Percentage %':
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
    
    html += f"""
    <div class="visualization">
        <div class="visualization-title">Contact Methods by Quarter</div>
        <div class="chart-container">{plot_to_html(fig_contact_quarter)}</div>
    </div>
    """

    # 10. Incidents by Quarter per Brand - NO Y-AXIS LABEL
    quarter_brand_type_df = filtered_df.groupby(['Quarter', 'Brand', 'Type'])['Number'].sum().reset_index()
    quarter_brand_type_df = quarter_brand_type_df.sort_values(['Brand', 'Quarter', 'Type'], ascending=[True, True, True])
    quarter_brand_type_df['Quarter'] = pd.Categorical(
        quarter_brand_type_df['Quarter'],
        categories=[q for q in quarters if q in quarter_brand_type_df['Quarter'].unique()],
        ordered=True
    )
    unique_brands = quarter_brand_type_df['Brand'].unique()

    if method == 'Percentage %':
        brand_totals = quarter_brand_type_df.groupby('Brand')['Number'].sum()
        quarter_brand_type_df['Percentage'] = quarter_brand_type_df.apply(
            lambda row: (row['Number'] / brand_totals[row['Brand']]) * 100 if brand_totals[row['Brand']] > 0 else 0,
            axis=1
        )
        quarter_brand_type_df['Percentage'] = quarter_brand_type_df['Percentage'].round(0).astype(int)
        y_max_val = 100

        fig11 = px.bar(
            quarter_brand_type_df,
            x='Quarter',
            y='Percentage',
            color='Type',
            barmode='group',
            facet_col='Brand',
            facet_col_wrap=min(4, len(unique_brands)),
            facet_row_spacing=0.2,
            color_discrete_map={'Cases': color_scheme['Cases'], 'Complaints': color_scheme['Complaints']},
            labels={'Percentage': '', 'Quarter': ''},
            text='Percentage'
        )
        fig11.update_traces(width=0.4, texttemplate='%{text}%', textposition='outside')
    else:
        y_max_val = quarter_brand_type_df.groupby(['Brand', 'Quarter'])['Number'].sum().max()
        
        fig11 = px.bar(
            quarter_brand_type_df,
            x='Quarter',
            y='Number',
            color='Type',
            barmode='group',
            facet_col='Brand',
            facet_col_wrap=min(4, len(unique_brands)),
            facet_row_spacing=0.2,
            color_discrete_map={'Cases': color_scheme['Cases'], 'Complaints': color_scheme['Complaints']},
            labels={'Number': '', 'Quarter': ''},
            text='Number'
        )
        fig11.update_traces(width=0.4, texttemplate='%{text:,.0f}', textposition='outside')

    fig11.update_layout(
        plot_bgcolor=bg_color,
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(size=14, family="Arial", color='black', weight='bold'),
        legend=dict(font=dict(size=12, color='black', weight='bold'), bgcolor='rgba(0,0,0,0)'),
        yaxis_title=' ',
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
        range=[0, y_max_val * 1.3],
        title_text=''
    )
    
    html += f"""
    <div class="visualization">
        <div class="visualization-title">Incidents by Quarter per Brand</div>
        <div class="chart-container">{plot_to_html(fig11)}</div>
    </div>
    """

    # 11. Monthly Timeline
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
                marker=dict(size=8, line=dict(width=2, color='Black'))
            )
            
            fig15.update_layout(
                **timeline_layout,
                xaxis_title='Date',
                yaxis_title='Percentage of Incidents (%)',
                legend_title_text='Incident Type',
                height=400
            )
        else:
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
                marker=dict(size=8, line=dict(width=2, color='Black'))
            )
            
            fig15.update_layout(
                **timeline_layout,
                xaxis_title='Date',
                yaxis_title='Number of Incidents',
                legend_title_text='Incident Type',
                height=400
            )
            
        html += f"""
        <div class="visualization">
            <div class="visualization-title">Monthly Incidents Timeline by Type</div>
            <div class="chart-container">{plot_to_html(fig15)}</div>
        </div>
        """
    except Exception as e:
        html += f"<p>Could not create monthly timeline chart: {str(e)}</p>"

    # 12. Quarterly Timeline
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
                marker=dict(size=8, line=dict(width=2, color='Black'))
            )
            
            fig16.update_layout(
                **timeline_layout,
                xaxis_title='Date',
                yaxis_title='Percentage of Incidents (%)',
                legend_title_text='Incident Type',
                height=400
            )
        else:
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
                marker=dict(size=8, line=dict(width=2, color='Black'))
            )
            
            fig16.update_layout(
                **timeline_layout,
                xaxis_title='Date',
                yaxis_title='Number of Incidents',
                legend_title_text='Incident Type',
                height=400
            )
            
        html += f"""
        <div class="visualization">
            <div class="visualization-title">Quarterly Incidents Timeline by Type</div>
            <div class="chart-container">{plot_to_html(fig16)}</div>
        </div>
        """
    except Exception as e:
        html += f"<p>Could not create quarterly timeline chart: {str(e)}</p>"

    html += """
    <div class="footer">

        <p>📌 Authority :<a href="mailto:omarelshaarawy909@gmail.com"> <b>Omar Shaarawy</b></a> | Version 1.0.0 Beta</p>
    </div>
    </body>
    </html>
    """
    
    return html, report_name
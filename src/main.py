import streamlit as st
import pandas as pd
import warnings
from components.header import render_header
from components.sidebar import render_sidebar
from components.metrics import render_metrics
from components.visualizations import render_visualizations
from components.footer import render_footer
from file_utils import load_and_combine_files, preprocess_data
from report_utils import generate_html_report

warnings.filterwarnings('ignore')

def main():
    st.set_page_config(layout="wide", page_icon='🎧', page_title='Social Listening')
    
    months = ["January", "February", "March", "April", "May", "June",
              "July", "August", "September", "October", "November", "December"]
    quarters = ['Q1', 'Q2', 'Q3', 'Q4']
    
    render_header()
    
    if st.session_state.get('is_logged_in', False):
        st.sidebar.title("Visual Settings")

        st.sidebar.subheader("Primary Color")
        base_color = st.sidebar.color_picker("Pick a color", "#F9F28A")

        st.sidebar.subheader("Secondary Color")
        complementary_color = st.sidebar.color_picker("Pick a color", "#E4A21F")

        # NEW: Color Palette Dropdown
        st.sidebar.subheader("Color Palette")
        palette_options = {
            "🎨 Default": ["#F9F28A", "#E4A21F", "#D45D3F", "#4C4C47"],
            "🌸 Pastel": ["#AEC7E8", "#FFBB78", "#98DF8A", "#FF9896", "#C5B0D5", "#C49C94", "#F7B6D2", "#C7C7C7", "#DBDB8D", "#9EDAE5"],
            "🌑 Dark": ["#2E91E5", "#E15F99", "#1CA71C", "#FB0D0D", "#DA16FF", "#222A2A", "#B68100", "#750D86", "#EB663B", "#511CFB"],
            "☀️ Light": ["#FD3216", "#00FE35", "#6A76FC", "#FED4C4", "#FE00CE", "#0DF9FF", "#F6F926", "#FF9616", "#479B55", "#EEA6FB"],
            "💥 Bold": ["#BD1E1E", "#1E78BD", "#49A049", "#7B1E7B", "#E07B1E", "#1EBDBD", "#BDBD1E", "#7B1E7B", "#1E49A0", "#A01E1E"],
            "🌇 Sunset": ["#F94144", "#F3722C", "#F8961E", "#F9C74F", "#90BE6D", "#43AA8B", "#577590", "#F2A65A", "#D81159", "#8F2D56"],
            "🌊 Ocean": ["#0077B6", "#0096C7", "#00B4D8", "#48CAE4", "#90E0EF", "#ADE8F4", "#CAF0F8", "#023E8A", "#03045E", "#001845"],
            "🍂 Muted": ["#E07A5F", "#3D405B", "#81B29A", "#F2CC8F", "#BC4749", "#6A994E", "#A44A3F", "#545775", "#B58DB6", "#F4A259"],
            "✨ Neon": ["#39FF14", "#FF10F0", "#1B03A3", "#FF6037", "#0FF0FC", "#F7F528", "#FF073A", "#75D5FD", "#ADF7B6", "#FFC0CB"]
        }
        
        selected_palette = st.sidebar.selectbox(
            "Pick a color palette",
            options=list(palette_options.keys()),
            index=0
        )
        
        # Get the selected palette
        custom_palette = palette_options[selected_palette]
        
        st.sidebar.subheader("Background Color")
        use_transparent_bg = st.sidebar.checkbox("Transparent background", value=True)
        if use_transparent_bg:
            bg_color = "rgba(0,0,0,0)" 
        else:
            bg_color = st.sidebar.color_picker("Pick a color", "#ffffff")
    
        color_scheme = {             
            'Cases': base_color,             
            'Complaints': complementary_color,  
            'Quarters' : custom_palette,           
            'Brands': custom_palette,  # Use selected palette instead of generated
            'Countries': custom_palette,  # Use selected palette instead of generated
            'Months':custom_palette,
            'Contact': custom_palette,  # Use selected palette instead of generated
            'Type_Detail': custom_palette,  # Use selected palette instead of generated
            'bg_color': bg_color         
        }
        st.sidebar.markdown("---")
        
        uploaded_files = st.file_uploader("Choose files", type=["csv", "xlsx", "xls"], accept_multiple_files=True)

        if uploaded_files:
            df = load_and_combine_files(uploaded_files)
            
            if not df.empty:
                st.success(f"Successfully loaded {len(uploaded_files)} file(s) with {len(df)} total records!")
                df = preprocess_data(df)
                
                show_data, method, year, quarter, month, brand, country, type_cc, type_detail, contact_way = render_sidebar(df, months, quarters)
                
                # Track if quarter filter is applied
                st.session_state['quarter_filter_applied'] = bool(quarter)
                
                filtered_df = df.copy()
                if year:
                    filtered_df = filtered_df[filtered_df['Year'].isin(year)]
                if quarter:
                    filtered_df = filtered_df[filtered_df['Quarter'].isin(quarter)]
                if month:
                    filtered_df = filtered_df[filtered_df['Month'].isin(month)]
                if brand:
                    filtered_df = filtered_df[filtered_df['Brand'].isin(brand)]
                if type_cc:
                    filtered_df = filtered_df[filtered_df['Type'].isin(type_cc)]
                if type_detail:
                    filtered_df = filtered_df[filtered_df['Type Detail'].isin(type_detail)]
                if contact_way:
                    filtered_df = filtered_df[filtered_df['Contact Way'].isin(contact_way)]
                if country:
                    filtered_df = filtered_df[filtered_df['Country'].isin(country)]

                if show_data:
                    display_df = filtered_df.copy()
                    if display_df.empty:
                        st.dataframe(display_df, use_container_width=True)
                        st.warning("No data available for the selected filters.")
                    else:    
                        st.header('Filtered Data')    
                        display_df['Month'] = pd.Categorical(display_df['Month'], categories=months, ordered=True)
                        display_df['Quarter'] = pd.Categorical(display_df['Quarter'], categories=quarters, ordered=True)
                        display_df = display_df.sort_values(['Year', 'Month', 'Quarter'])
                        display_df['Year'] = display_df['Year'].astype(str)
                        display_df.index += 1
                        st.dataframe(display_df, use_container_width=True)

                st.markdown("<h2 style='text-align: center;'>Welcome to Social Listening Insights</h2>", unsafe_allow_html=True)
                
                col1, col2, col3, col4, col5 = st.columns([1, 1, 2, 1, 1])
                with col3:
                    if st.button('Generate Report 📄', use_container_width=True):
                        try:
                            html_content, report_name = generate_html_report(
                                filtered_df, month, quarter, year, brand, type_cc, type_detail, contact_way, country, color_scheme
                            )
                            st.download_button(
                                label="Download Report ⬇️",
                                data=html_content,
                                file_name=f"{report_name}.html",
                                mime="text/html",
                                use_container_width=True
                            )
                            st.success("Report generated successfully!\n\nYou can download it now.")
                        except Exception as e:
                            st.error(f"Error generating report: {str(e)}")

                st.markdown("<br><br>", unsafe_allow_html=True)
                
                render_metrics(filtered_df, months, month)
                
                st.markdown("<br><hr><br>", unsafe_allow_html=True)
                
                render_visualizations(filtered_df, months, quarters, color_scheme, method)
                
                st.markdown("<br>", unsafe_allow_html=True)
                st.markdown("<br>", unsafe_allow_html=True) 

                
            else:
                st.warning("The uploaded files could not be processed. Please check the file format.")
        else:
            st.info("Upload CSV or Excel files to analyse the data.")
        render_footer()    

if __name__ == "__main__":
    main()
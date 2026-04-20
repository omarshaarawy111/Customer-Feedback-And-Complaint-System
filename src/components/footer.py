import streamlit as st

def render_footer():
    st.markdown(
        """
        <div style='text-align: center; margin-top: 50px;'>
        <a href="#" target="_blank">
                        <img src=" width="120" style="margin-bottom: 10px;" />
        </a>    
            <h4 style='font-size: 16px;'>📌 Authority :<a href="mailto:omarelshaarawy909@gmail.com"> <b>Omar Shaarawy</b></a> | Version 1.2.1 </h4> 
        </div>
        """,
        unsafe_allow_html=True
    )
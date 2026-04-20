import streamlit as st
from auth import authenticate_user

def render_header():
    
    is_logged_in = st.session_state.get('is_logged_in', False)
    if not is_logged_in:
        st.markdown(
            '''
            <div style="text-align: center;">
               <img src="ht" alt="Logo" style="width: 600px; height: auto;">
            </div>
            ''',
            unsafe_allow_html=True
        )
        st.markdown('<h1 style="text-align: center; font-size:28px;">Customer Feedback And Complaint System</h1>', unsafe_allow_html=True)

        email = st.text_input("Username")
        password = st.text_input("Password", type="password")
        login_button = st.button("Login")

        if login_button:
            if authenticate_user(email, password):
                st.session_state.is_logged_in = True
                st.success("Logged in successfully!")
                st.rerun()
            else:
                st.error("Wrong Email or Password.")
    else:
        st.markdown("<h2 style='text-align: left;'>Start Analysing...</h2>", unsafe_allow_html=True)
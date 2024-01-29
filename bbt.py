import streamlit as st

def bbt():
    st.info("**Date: March 29, 2005**")
    st.caption("6:15 am [raining]")
    st.write("A family of four prepares for a surgery. ")
    with st.expander("Family details"):
        st.info("")

    st.success("Reason for surgery: **Sinus Problems.**")
    st.info("Estimated risk level: **Tiny.**")
    

bbt()
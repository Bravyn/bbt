import streamlit as st

def bbt():
    family = ["Martin Bromiley(Husband)", "Elaine(Wife)", "Victoria(Daughter)", "Adam(Son)"]
    st.info("**March 29, 2005.**")
    st.caption("6:15 am [raining]")
    st.write("A family of four prepares for a surgery. ")
    with st.expander("Family details"):
        for family_member in family:
            st.info(family_member)

    st.success("Reason for surgery: **Sinus Problems.**")
    st.info("Estimated risk level: **Tiny.**")
    

bbt()
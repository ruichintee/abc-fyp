import streamlit as st

def main():
    st.title("Welcome to the Singapore Blood Donation App")
    st.write("Learn more about blood donation and find out how you can contribute.")
    
    # Buttons to navigate to other pages
    st.write("Navigate to:")
    if st.button("Am I Eligible"):
        st.session_state.page = "Eligibility"
    if st.button("Where to Donate"):
        st.session_state.page = "DonationLocations"
    if st.button("About Us"):
        st.session_state.page = "AboutUs"
    if st.button("Methodology"):
        st.session_state.page = "Methodology"


    st.write("IMPORTANT NOTICE: This web application is a prototype developed for educational purposes only. The information provided here is NOT intended for real-world usage and should not be relied upon for making any decisions, especially those related to financial, legal, or healthcare matters. Furthermore, please be aware that the LLM may generate inaccurate or incorrect information. You assume full responsibility for how you use any generated output. Always consult with qualified professionals for accurate and personalized advice.")
if __name__ == "__main__":
    main()

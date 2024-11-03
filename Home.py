import streamlit as st

def main():
    st.title("Welcome to the Singapore Blood Donation App")
    st.write("Learn more about blood donation and find out how you can contribute.")


    st.write("IMPORTANT NOTICE: This web application is a prototype developed for educational purposes only. The information provided here is NOT intended for real-world usage and should not be relied upon for making any decisions, especially those related to financial, legal, or healthcare matters. Furthermore, please be aware that the LLM may generate inaccurate or incorrect information. You assume full responsibility for how you use any generated output. Always consult with qualified professionals for accurate and personalized advice.")

    pg = st.navigation([st.Page("Eligibility.py"), st.Page("DonationLocation.py"), st.Page("AboutUs.py"), st.Page("Methodology.py")])
    pg.run()

if __name__ == "__main__":
    main()

import streamlit as st

def main():
    st.title("About Us")
    st.write("""
    ### Project Scope
    This project is designed to improve public awareness of blood donation criteria and streamline the donation process.
    
    ### Objectives
    - Provide an easy-to-access eligibility checker
    - Update users with real-time blood stock levels
    - Guide users to nearby blood donation centers
    
    ### Data Sources
    - Blood donation eligibility: [HSA](https://www.hsa.gov.sg/blood-donation/can-i-donate)
    - Blood stock levels: [Singapore Red Cross](https://redcross.sg/#bloodstock)
    
    ### Key Features
    - User-friendly eligibility assessment
    - Real-time stock level updates
    - Interactive map of blood donation centers
    """)


if __name__ == "__main__":
    main()
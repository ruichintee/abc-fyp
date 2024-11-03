import streamlit as st

def main():
    st.title("About Us")
    st.write("""
    ### Project Scope
    This project is designed to allow the public to assess if they are able to donate blood and to find the nearest donation centre, 
    in a bid to make it more accessible
    
    ### Objectives
    - Provide an easy-to-access eligibility check
    - Guide users to nearby blood donation centers
    
    ### Data Sources
    - Blood donation eligibility: [HSA](https://www.hsa.gov.sg/blood-donation/can-i-donate)
    - Bloodbank Location: [HSA](https://www.hsa.gov.sg/blood-donation/where-to-donate)
    
    ### Key Features
    - User-friendly eligibility assessment
    - Interactive map of blood donation centers
    """)


if __name__ == "__main__":
    main()

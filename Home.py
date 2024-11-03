import streamlit as st

# Password protection logic
import hmac


def check_password():
    """Returns `True` if the user had the correct password."""

    def password_entered():
        if st.session_state["password"] == st.secrets["password"]:
            st.session_state["password_correct"] = True
            del st.session_state["password"]
        else:
            st.session_state["password_correct"] = False

if "password_correct" not in st.session_state:
    st.text_input("Enter the password", type="password", on_change=password_entered, key="password")
    return False
elif not st.session_state["password_correct"]:
    st.text_input("Enter the password", type="password", on_change=password_entered, key="password")
    st.error("Password is incorrect")
    return False
else:
    return True

def main():
    st.set_page_config(
        page_title="Blood Donation Eligibility Checker",
        page_icon="🩸",
        layout="wide",
        initial_sidebar_state="expanded",
    )
       
    st.title("Welcome to the Blood Donation Eligibility Checker")
    st.write("Learn more about your blood donation eligibility and the nearest blood bank")
       
    st.write("IMPORTANT NOTICE: This web application is a prototype developed for educational purposes only. The information provided here is NOT intended for real-world usage and should not be relied upon for making any decisions, especially those related to financial, legal, or healthcare matters. Furthermore, please be aware that the LLM may generate inaccurate or incorrect information. You assume full responsibility for how you use any generated output. Always consult with qualified professionals for accurate and personalized advice.")
    
if __name__ == "__main__":
     main()

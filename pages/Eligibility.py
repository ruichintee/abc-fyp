import streamlit as st
from bs4 import BeautifulSoup

# Set up the OpenAI API key
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Retrieve the OpenAI API key
# Set OpenAI API key
os.environ["OPENAI_API_KEY"] = st.secrets["OpenAI_key"]

def scrape_eligibility_info():
    with open("data/canidonate.html", "r", encoding="utf-8") as file:
        content = file.read()

    soup = BeautifulSoup(content, "html.parser")

    # Extract eligibility information contained within <div class="hsa-tab-inner"> and <p> tags
    eligibility_criteria = []
    eligibility_sections = soup.find_all("div", class_="hsa-tab-inner")  # Targeting specific divs

    for section in eligibility_sections:
        paragraphs = section.find_all("p")  # Find all <p> elements within each targeted div
        for paragraph in paragraphs:
            text = paragraph.get_text(strip=True)
            if text:  # Only add non-empty text
                eligibility_criteria.append(text)

    from langchain.schema import Document
    docs = [Document(page_content=x) for x in eligibility_criteria]
    print(eligibility_criteria)


    #Embed text
    from langchain_text_splitters import RecursiveCharacterTextSplitter
    from langchain_core.vectorstores import InMemoryVectorStore
    from langchain_openai import OpenAIEmbeddings

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000, chunk_overlap=200, add_start_index=True
        )
    splits = text_splitter.split_documents(docs)
    vectorstore = InMemoryVectorStore.from_documents(
        documents=splits, embedding=OpenAIEmbeddings()
        )

    retriever = vectorstore.as_retriever()
    return retriever 


def main():

    st.title("Am I Eligible to Donate Blood?")
    age = st.number_input("Enter your age", min_value=1, max_value=120)
    weight = st.number_input("Enter your weight (kg)", min_value=1.0, max_value=100.0)
    good_health = st.checkbox("Are you in good health?")
    
    if age >= 16 and weight >= 45 and good_health:
        travel_history = st.text_area("Please provide any recent travel history:")
        medical_conditions = st.text_area("Do you have any existing medical conditions?")

        # Pass data to the eligibility agent (using OpenAI)
        if st.button("Check Eligibility"):
            context = f"""
            The user is {age} years old, and weighs {weight}. He is in good health, and has travelled recently to the following places: {travel_history}.
            He also has the following medical history: {medical_conditions}.
        
            """
            from langchain.chains import create_retrieval_chain
            from langchain.chains.combine_documents import create_stuff_documents_chain
            from langchain_core.prompts import ChatPromptTemplate
            from langchain_openai import ChatOpenAI 

            system_prompt = (
            "You are an assistant for question-answering tasks. "
            "Use the following pieces of retrieved context to answer "
            "the question. If you don't know the answer, say that you "
            "don't know. Use three sentences maximum and keep the "
            "answer concise."
            "\n\n"
            "{context}"
            )

            
            prompt = ChatPromptTemplate.from_messages(
            [
                ("system", system_prompt),
                ("human", "{input}"),
            ]
            )
            llm = ChatOpenAI(model="gpt-4o")
            retriever = scrape_eligibility_info()
            document_chain = create_stuff_documents_chain(llm, prompt)
            rag_chain = create_retrieval_chain(retriever, document_chain)


            results = rag_chain.invoke({"input":  "The user is {} years old, and weighs {} kg. He is in good health, and has travelled recently to the following places: {}."
            "He also has the following medical history: {}. Determine if the user is eligible to donate blood.".format(age,weight,travel_history,medical_conditions)
                                       })
            st.write(results["answer"])

        elif age < 16:
            st.write("You need to be at least 16 years old to donate blood! Try again when you're older!")

        elif weight <45:
            st.write("You need to be at least 45 kg to donate blood!")



if __name__ == "__main__":
    main()

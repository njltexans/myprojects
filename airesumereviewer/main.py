import streamlit as st
import PyPDF2
import io
import os
from openai import OpenAI

from dotenv import load_dotenv

load_dotenv() # Load environment variables from .env file
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY") # Get the OpenAI API key from environment variables

client = OpenAI(api_key=OPENAI_API_KEY)

st.set_page_config(page_title="AI Resume Helper", page_icon="📄", layout="centered") # Set the page configuration for the Streamlit app

st.title("AI Resume Helper") # Set the title of the Streamlit app
st.markdown("Upload your resume in PDF format and get AI-powered feedback.") # Add a description to tell user what they need to do

uploaded_file = st.file_uploader("Upload your resume (PDF format)", type=["pdf"]) # Create a file uploader for PDF files
job_you_want = st.text_input("What job are you applying for?") # Create a text input for the job title

analyze = st.button("Analyze Resume") # Create a button to trigger the analysis

def extract_text_from_pdf(pdf_file):
    pdf_reader = PyPDF2.PdfReader(pdf_file) # Create a PDF reader object
    text = ""
    for page in pdf_reader.pages: # Iterate through each page in the PDF
        text += page.extract_text() + "\n" # Extract text from each page
    return text

def extract_text_from_file(uplaoded_file):
    if uploaded_file.type == "application/pdf":
        return extract_text_from_pdf(io.BytesIO(uploaded_file.read())) # If the file is a PDF, extract text from it
        return "Unsupported file type. Please upload a PDF file."
    return uploaded_file.read().decode("utf-8") # If the file is not a PDF, read it as text

if analyze and uploaded_file:
    try:
        file_content = extract_text_from_file(uploaded_file) # Extract text from the uploaded file

        if not file_content.strip():
            st.error("The uploaded file is empty or could not be read. Please upload a valid PDF file.")
            st.stop()

        prompt = f"""
        Please analyze the following resume based on the following criteria:
        1. Formatting and structure
        2. Clarity and conciseness
        3. Presentation of skills
        4. Experience descriptions and/or bullet points
        5. Overall impression
        6. Specific suggestions for {job_you_want if job_you_want else 'general job applications'} 

        Resume Content:
        {file_content}

        Provide your feedback in a concise, clear, structured, and professional manner with specific recommendations.
        """

        # Use the OpenAI API to generate a response
        response = client.chat.completions.create(model="gpt-4",  # Use the GPT-4 model for the analysis
        messages=[
            {"role": "system", "content": "You are an expert resume reviewer."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=1000,  # Set the maximum number of tokens for the response
        temperature=0.5)

        # Display the results in the Streamlit app
        st.markdown("### Resume Analysis Results")  # Display the results section
        st.markdown(response.choices[0].message.content)  # Show the AI's feedback on the resume

    except Exception as e:
        st.error(f"An error occurred while processing the resume: {str(e)}")  # Handle any errors that occur during processing


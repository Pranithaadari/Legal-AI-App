import streamlit as st
from docx import Document # You need to install the python-docx library for this
from transformers import pipeline  # Install transformers library
qa_pipeline = pipeline("question-answering")

def extract_text_from_docx(docx_file):
    doc = Document(docx_file)
    full_text = []
    for para in doc.paragraphs:
        full_text.append(para.text)
    return '\n'.join(full_text)

# Title and description
st.title("AI-Driven Legal Document Analysis")
st.write("Upload a legal document to summarize, assess risks, and ask questions.")

# File uploader
document_file = st.file_uploader("Upload your legal document (PDF, DOCX, or Text):", type=["pdf", "txt", "docx"])

if document_file is not None:
    # Extract text from the uploaded document based on the file type
    if document_file.type == "text/plain":
        document_text = document_file.read().decode("utf-8")
    elif document_file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
        document_text = extract_text_from_docx(document_file)
    else:
        document_text = "Extracted text from PDF"  # Placeholder for PDF extraction logic

    # Display the uploaded document's content
    with st.expander("View Document Content"):
        st.text_area("Document Content", document_text, height=300)

    # Summarize the document
    st.write("### Document Summary")
    summary = "This is a summarized version of the document."  # Placeholder for summarization logic
    st.write(summary)

    # Risk assessment
    st.write("### Risk Assessment")
    risk_score = 7.5  # Example risk score
    risk_details = "Potential legal risks identified in clauses 3, 5, and 8."
    st.metric("Risk Score", risk_score, "Moderate")
    st.write(risk_details)

    # Question-Answering Section
    st.write("### Ask Questions About the Document")
    question = st.text_input("Enter your question about the document:")
    
    if question:
        try:
            # Use the QA pipeline to get an answer
            result = qa_pipeline(question=question, context=document_text)
            answer = result['answer']
            st.write("#### Answer:")
            st.success(answer)
        except Exception as e:
            st.error(f"An error occurred: {e}")

    # Suggestions
    st.write("### Suggestions for Improvement")
    st.write("- Review clauses 3, 5, and 8 for potential issues.")
    st.write("- Consult with a legal expert for further guidance.")

# Footer
st.write("---")
st.info("Powered by advanced AI models for legal document analysis.")

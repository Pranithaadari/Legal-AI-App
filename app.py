import streamlit as st
from docx import Document  # You need to install the python-docx library for this

def summarize_document(document_text):
    # Placeholder for AI-based summarization logic
    summary = "This is a summarized version of the document."
    return summary

def assess_risk(document_text):
    # Placeholder for AI-based risk assessment logic
    risk_score = 7.5  # Example risk score
    risk_details = "Potential legal risks identified in clauses 3, 5, and 8."
    return risk_score, risk_details

def extract_text_from_docx(docx_file):
    doc = Document(docx_file)
    full_text = []
    for para in doc.paragraphs:
        full_text.append(para.text)
    return '\n'.join(full_text)

# Title and description
st.title("Advanced AI-Driven Legal Document Summarization and Risk Assessment")
st.write("Upload a legal document to generate a summary and assess potential risks.")

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
    summary = summarize_document(document_text)
    st.write(summary)

    # Risk assessment
    st.write("### Risk Assessment")
    risk_score, risk_details = assess_risk(document_text)
    st.metric("Risk Score", risk_score, "Moderate")
    st.write(risk_details)

    # Suggestions
    st.write("### Suggestions for Improvement")
    st.write("- Review clauses 3, 5, and 8 for potential issues.")
    st.write("- Consult with a legal expert for further guidance.")

# Footer
st.write("---")
st.info("Powered by advanced AI models for legal document analysis.")

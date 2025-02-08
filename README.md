**Legal Document Risk Analysis Dashboard**
A Streamlit-powered web application for analyzing legal documents, identifying potential risks, and providing actionable recommendations. The application also integrates with Google Sheets for saving results and offers email notifications.

**Features**
**File Upload:** Upload legal documents in .txt, .docx, or .pdf formats for analysis.
**Risk Analysis:**Analyze documents for potential risks and recommendations using LLaMA 3.2 model.
**Interactive Dashboard:**
Displays analysis results in a table.
Allows downloading results as a CSV file.
**Google Sheets Integration:** Save the analysis results directly to a Google Sheet.
**Email Notifications:**Send a summary of the analysis to stakeholders via email.
**Chat Functionality:** Query the document for additional insights.
**User-Friendly Interface:** Organized layout with intuitive navigation and modern design.
**Technology Stack**
**Backend**
**Python:** Core programming language.
**LangChain:** Framework for handling LLMs and document-based analysis.
**LLaMA 3.2:** Advanced large language model for risk and recommendation generation.
**Chroma:** Vector database for document chunking and retrieval.
**HuggingFace:** Embedding models for semantic similarity.
**Frontend**
**Streamlit:** Framework for building the user interface with custom layouts and interactions.
**Additional Tools**
**Google Sheets API:** For exporting results to spreadsheets.
**SMTP:** For sending emails with report links.
**Custom CSS:** For styling the dashboard.
**How It Works**
1.Upload a Document:

   Users can upload .txt, .docx, or .pdf files.
2.Document Analysis:

  The document is split into chunks for analysis.
  The LLaMA 3.2 model evaluates each chunk to identify risks and recommendations.
3.View Results:

    Results are displayed in a structured table with columns for context, risks, and 
    recommendations.
4.Save and Share:

  Save results to a Google Sheet.
  Email a summary report to stakeholders.
5.Query the Document:

  Use the chat interface to ask questions about the document.
**Prerequisites**
Python 3.8 or above
Required Python libraries (install using pip install -r requirements.txt):
   streamlit
   pandas
   google-api-python-client
   google-auth
   langchain
   smtplib
**Setup Instructions**
1.Clone the Repository

git clone https://github.com/yourusername/legal-risk-dashboard.git
cd legal-risk-dashboard
2.Install Dependencies
Install all the required Python libraries using the following command:

pip install -r requirements.txt
3.Add Google Service Account Key

Obtain the service account key from the Google Cloud Console.
Download the JSON key file and place it in the project directory.
Update the SERVICE_ACCOUNT_FILE variable in the code with the path to this file.
4.Configure Google Sheets

Create a Google Sheet and copy its Sheet ID.
Replace the SPREADSHEET_ID variable in the code with your Google Sheet's ID.
5.Run the Streamlit App
Start the application by running the following command:

streamlit run app.py
6.Access the Application
Open the provided localhost or network URL in your browser to access the dashboard.

**Future Enhancements**
Add support for additional file formats.
Enhance the chat functionality with contextual responses.
Improve the dashboard's UI/UX with advanced visualization tools.
Integrate with other storage and sharing platforms (e.g., OneDrive, Dropbox).

**Acknowledgments**
OpenAI for providing the foundational models.
Streamlit for enabling quick and interactive web app development.
Google Cloud Platform for API services.






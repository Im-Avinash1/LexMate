import streamlit as st
from src.document_parser import parse_document
from src.ai_utils import generate_summary, extract_key_info
from src.legal_checker import check_legal_compliance

st.set_page_config(page_title="Legal Doc Analyzer", layout="wide")
st.title("📄 Legal Document Analyzer")

uploaded_file = st.file_uploader("Upload a legal document (PDF or DOCX)", type=["pdf", "docx"])
meta_info = st.text_area("Enter additional agreement details (optional)")

if uploaded_file:
    with st.spinner("Processing document..."):
        text = parse_document(uploaded_file)
        summary = generate_summary(text)
        key_info = extract_key_info(text)
        legal_flags = check_legal_compliance(text)

    st.subheader("📑 Document Summary")
    st.write(summary)

    st.subheader("🔍 Key Information Extracted")
    st.write(key_info)

    st.subheader("⚖️ Legal Compliance Check")
    if legal_flags:
        for issue in legal_flags:
            st.error(issue)
    else:
        st.success("No major legal issues detected.")
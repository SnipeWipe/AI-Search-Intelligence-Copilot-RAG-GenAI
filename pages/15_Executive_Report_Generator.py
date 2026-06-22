import streamlit as st
import base64

from backend.reports.report_generator import (
    ReportGenerator
)

from backend.llm.gemini_client import (
    GeminiClient
)

# ==========================================
# PAGE CONFIG
# ==========================================

st.set_page_config(
    page_title="Executive Report Generator",
    layout="wide"
)

st.title(
    "Executive Search Intelligence Report Generator"
)

st.markdown(
    """
Generate executive-level business reports powered by Gemini.
"""
)

# ==========================================
# USER INPUT
# ==========================================

question = st.text_area(
    "Ask for Executive Insights",
    placeholder="""
Examples:

• Give an executive summary of paid search performance.
• Recommend budget reallocations.
• Identify growth opportunities in paid search.
• Analyze risks and acquisition opportunities.
"""
)

# ==========================================
# GENERATE REPORT
# ==========================================

if st.button("Generate Executive Report"):

    if not question.strip():

        st.warning(
            "Please enter a question."
        )

    else:

        with st.spinner(
                "Generating executive insights..."
        ):

            prompt = f"""
You are the Vice President of Paid Search Analytics at American Express.

Prepare an executive report for senior leadership.

User request:
{question}

Generate a professional executive report in Markdown.

Rules:
- Use # for section headings.
- Use bullet points whenever possible.
- Keep paragraphs concise.
- Use business language suitable for senior executives.

Structure:

# Executive Summary

# Key Business Drivers

# Growth Opportunities

# Risks and Challenges

# Budget Recommendations

# AI Search Recommendations

# Expected Business Impact

# Top 5 Executive Actions

Provide five high-priority recommendations.
"""

            try:

                insights = (

                    GeminiClient()

                    .generate(prompt)

                )

                # ==========================================
                # DISPLAY INSIGHTS
                # ==========================================

                st.success(
                    "Executive insights generated successfully."
                )

                st.markdown(
                    "## Generated Executive Insights"
                )

                st.markdown(
                    insights
                )

                # ==========================================
                # GENERATE PDF
                # ==========================================

                file_path = (

                    ReportGenerator()

                    .create_report(

                        insights,

                        "reports/executive_report.pdf"

                    )

                )

                # ==========================================
                # PDF DOWNLOAD + PREVIEW
                # ==========================================

                with open(
                        file_path,
                        "rb"
                ) as f:

                    pdf_bytes = f.read()

                st.download_button(

                    label="Download PDF Report",

                    data=pdf_bytes,

                    file_name="executive_report.pdf",

                    mime="application/pdf"

                )

                # ==========================================
                # SHOW PDF IN STREAMLIT
                # ==========================================

                base64_pdf = (

                    base64.b64encode(
                        pdf_bytes
                    )

                    .decode("utf-8")

                )

                pdf_display = f"""
                    <iframe
                        src="data:application/pdf;base64,{base64_pdf}"
                        width="100%"
                        height="900"
                        type="application/pdf">
                    </iframe>
                """

                st.markdown(
                    "## PDF Preview"
                )

                st.markdown(
                    pdf_display,
                    unsafe_allow_html=True
                )

            except Exception as e:

                st.error(
                    f"Error: {e}"
                )
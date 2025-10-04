import streamlit as st
from openai import OpenAI
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Configure page
st.set_page_config(
    page_title="Ethesis - MD Thesis Analysis",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for enhanced dashboard styling
st.markdown("""
<style>
    /* Import Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    
    /* Global Styles */
    .main {
        font-family: 'Inter', sans-serif;
    }
    
    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Main Header */
    .main-header {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 3rem 2rem;
        border-radius: 20px;
        margin-bottom: 3rem;
        text-align: center;
        color: white;
        box-shadow: 0 10px 30px rgba(102, 126, 234, 0.3);
        position: relative;
        overflow: hidden;
    }
    
    .main-header::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: url('data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100"><defs><pattern id="grain" width="100" height="100" patternUnits="userSpaceOnUse"><circle cx="25" cy="25" r="1" fill="white" opacity="0.1"/><circle cx="75" cy="75" r="1" fill="white" opacity="0.1"/><circle cx="50" cy="10" r="0.5" fill="white" opacity="0.1"/></pattern></defs><rect width="100" height="100" fill="url(%23grain)"/></svg>');
        opacity: 0.3;
    }
    
    .main-header h1 {
        font-size: 2.5rem;
        font-weight: 700;
        margin-bottom: 0.5rem;
        position: relative;
        z-index: 1;
    }
    
    .main-header p {
        font-size: 1.2rem;
        font-weight: 300;
        opacity: 0.9;
        position: relative;
        z-index: 1;
    }
    
    /* Expert Cards */
    .expert-card {
        background: linear-gradient(145deg, #ffffff 0%, #f8f9fa 100%);
        padding: 2rem;
        border-radius: 20px;
        border: 1px solid #e9ecef;
        margin: 1.5rem 0;
        box-shadow: 0 8px 25px rgba(0,0,0,0.08);
        transition: all 0.3s ease;
        position: relative;
        overflow: hidden;
    }
    
    .expert-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        width: 4px;
        height: 100%;
        background: linear-gradient(180deg, #667eea 0%, #764ba2 100%);
    }
    
    .expert-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 15px 35px rgba(0,0,0,0.12);
    }
    
    .expert-name {
        font-size: 1.4rem;
        font-weight: 600;
        color: #2c3e50;
        margin-bottom: 0.8rem;
        display: flex;
        align-items: center;
        gap: 0.5rem;
    }
    
    .expert-role {
        color: #6c757d;
        font-weight: 500;
        margin-bottom: 1.2rem;
        font-size: 1rem;
    }
    
    .expert-focus {
        color: #495057;
        line-height: 1.7;
        font-size: 0.95rem;
    }
    
    .expert-focus strong {
        color: #2c3e50;
        font-weight: 600;
    }
    
    /* Analysis Button */
    .stButton > button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        padding: 1.2rem 3rem;
        border-radius: 15px;
        font-size: 1.2rem;
        font-weight: 600;
        width: 100%;
        margin: 2rem 0;
        box-shadow: 0 8px 25px rgba(102, 126, 234, 0.3);
        transition: all 0.3s ease;
        font-family: 'Inter', sans-serif;
    }
    
    .stButton > button:hover {
        background: linear-gradient(135deg, #5a6fd8 0%, #6a4190 100%);
        transform: translateY(-2px);
        box-shadow: 0 12px 35px rgba(102, 126, 234, 0.4);
    }
    
    /* Analysis Output */
    .analysis-output {
        background: linear-gradient(145deg, #ffffff 0%, #f8f9fa 100%);
        padding: 2.5rem;
        border-radius: 20px;
        border: 1px solid #e9ecef;
        margin-top: 2rem;
        box-shadow: 0 10px 30px rgba(0,0,0,0.08);
    }
    
    .analysis-output h2 {
        color: #2c3e50;
        font-weight: 600;
        margin-bottom: 1.5rem;
        font-size: 1.8rem;
    }
    
    /* Process Steps */
    .process-steps {
        background: #f8f9fa;
        padding: 2rem;
        border-radius: 15px;
        margin: 2rem 0;
        border-left: 4px solid #667eea;
    }
    
    .step {
        display: flex;
        align-items: center;
        margin: 1rem 0;
        padding: 1rem;
        background: white;
        border-radius: 10px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.05);
    }
    
    .step-number {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        width: 40px;
        height: 40px;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        font-weight: 600;
        margin-right: 1rem;
        flex-shrink: 0;
    }
    
    .step-text {
        color: #495057;
        font-weight: 500;
    }
    
    /* Loading Animation */
    .loading-container {
        text-align: center;
        padding: 2rem;
    }
    
    .loading-spinner {
        border: 4px solid #f3f3f3;
        border-top: 4px solid #667eea;
        border-radius: 50%;
        width: 50px;
        height: 50px;
        animation: spin 1s linear infinite;
        margin: 0 auto 1rem;
    }
    
    @keyframes spin {
        0% { transform: rotate(0deg); }
        100% { transform: rotate(360deg); }
    }
    
    /* Responsive Design */
    @media (max-width: 768px) {
        .main-header h1 {
            font-size: 2rem;
        }
        
        .main-header p {
            font-size: 1rem;
        }
        
        .expert-card {
            padding: 1.5rem;
        }
        
        .expert-name {
            font-size: 1.2rem;
        }
    }
    
    /* Markdown Styling */
    .stMarkdown h1 {
        color: #2c3e50;
        font-weight: 700;
        margin-top: 2rem;
        margin-bottom: 1rem;
    }
    
    .stMarkdown h2 {
        color: #34495e;
        font-weight: 600;
        margin-top: 1.5rem;
        margin-bottom: 1rem;
    }
    
    .stMarkdown h3 {
        color: #34495e;
        font-weight: 600;
        margin-top: 1.2rem;
        margin-bottom: 0.8rem;
    }
    
    .stMarkdown p {
        line-height: 1.7;
        color: #495057;
    }
    
    .stMarkdown strong {
        color: #2c3e50;
        font-weight: 600;
    }
    
    .stMarkdown table {
        border-collapse: collapse;
        width: 100%;
        margin: 1rem 0;
        border-radius: 10px;
        overflow: hidden;
        box-shadow: 0 4px 15px rgba(0,0,0,0.08);
    }
    
    .stMarkdown th {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 1rem;
        text-align: left;
        font-weight: 600;
    }
    
    .stMarkdown td {
        padding: 1rem;
        border-bottom: 1px solid #e9ecef;
        background: white;
    }
    
    .stMarkdown tr:nth-child(even) td {
        background: #f8f9fa;
    }
    
    .stMarkdown tr:hover td {
        background: #e3f2fd;
    }
    
    /* Code blocks */
    .stMarkdown code {
        background: #f1f3f4;
        padding: 0.2rem 0.4rem;
        border-radius: 4px;
        font-family: 'Monaco', 'Menlo', monospace;
        color: #d63384;
    }
    
    .stMarkdown pre {
        background: #f8f9fa;
        padding: 1rem;
        border-radius: 10px;
        border-left: 4px solid #667eea;
        overflow-x: auto;
    }
    
    /* Blockquotes */
    .stMarkdown blockquote {
        border-left: 4px solid #667eea;
        padding-left: 1rem;
        margin: 1rem 0;
        background: #f8f9fa;
        padding: 1rem;
        border-radius: 0 10px 10px 0;
    }
</style>
""", unsafe_allow_html=True)

# Configure OpenAI API
def setup_openai():
    """Setup OpenAI client"""
    api_key = os.getenv('OPENAI_API_KEY')
    if not api_key:
        st.error("Please set OPENAI_API_KEY environment variable or create a .env file with your API key")
        st.stop()
    return OpenAI(api_key=api_key)

def generate_complete_analysis():
    """
    Generate Chief Guide insights using pre-written professor feedback
    """
    try:
        # Pre-written professor evaluations
        professor_eval = """# **MD Thesis Evaluation Report**

**Title:** *Effect of Constraining Underdilated Transjugular Intrahepatic Portosystemic Shunts (TIPS)*

**Candidate:** *[Name]*

**Institution:** *Yale School of Medicine*

---

## **1. Educational Perspective – Clinical and Methodological Evaluation**

**Reviewer:** *Dr. Joshua Cornman-Homonoff, MD*

**(Advising Faculty – Department of Radiology & Biomedical Imaging, Yale School of Medicine)*

This thesis demonstrates a solid understanding of **TIPS (Transjugular Intrahepatic Portosystemic Shunt)** procedures and a commendable application of research methodology. The work is both clinically meaningful and technically detailed, reflecting a mature grasp of interventional radiology principles.

---

### **Originality and Contribution**

The focus on *constraining underdilated TIPS* represents a **novel procedural innovation** addressing the problem of stent self-expansion. This approach bridges **device mechanics with patient outcomes**, an underexplored domain in TIPS optimization.

The findings on altered hemodynamics and increased revision rates provide valuable mechanistic insight with **direct translational relevance** for procedural refinement and shunt design.

---

### **Research Question and Objectives**

The research question is precise, clinically relevant, and logically structured. The objective—to assess the technical and clinical outcomes of constrained TIPS—is well formulated.

For future work, clearly defining **quantitative endpoints** (e.g., target gradient reduction or encephalopathy incidence) would enhance methodological transparency and reproducibility.

---

### **Literature Review**

The review provides a strong background on TIPS evolution and procedural advancements. Incorporating **recent literature (2020–2024)** on adjustable or flow-regulated shunt systems would make the context more current and technically aligned with contemporary practice.

---

### **Methodology and Study Design**

The **single-center retrospective cohort** design is appropriate and executed with rigor. Inclusion/exclusion criteria and stratification are clearly stated.

The chosen analytical tools—*t-tests*, chi-square, and Kaplan-Meier survival analysis—are suitable for the dataset. Incorporation of **multivariate regression** or **propensity matching** could further strengthen causal inference.

The procedural workflow and device specifications demonstrate strong technical literacy and reproducibility.

---

### **Results and Data Analysis**

Results are **statistically coherent and well-presented**, with comprehensive tables and survival plots enhancing interpretability.

The primary finding—that constrained TIPS restrict self-expansion but increase under-shunting and revision rates—is **clinically consistent** with shunt hemodynamics.

Future analyses could benefit from reporting **confidence intervals or effect sizes** alongside p-values for greater interpretive precision.

---

### **Discussion and Interpretation**

The discussion effectively links procedural mechanics with clinical outcomes. The rationale—that constrained shunts maintain smaller luminal diameters and higher gradients—is well supported.

The author shows **critical awareness of study limitations**, including operator variability and follow-up heterogeneity. Expanding on **training implications and device design insights** would further enrich the educational perspective.

---

### **Ethical and Regulatory Compliance**

All ethical and regulatory standards have been met. **IRB exemption** and **HIPAA-compliant data handling** are well documented, reflecting excellent professional integrity and awareness of clinical research protocols.

---

### **Structure, Organization, and Presentation**

The document is well organized with a clear logical flow. Figures and tables are informative and aid comprehension. Minor refinements in formatting consistency and figure annotation could further enhance readability.

---

### **Writing Quality and Scholarly Tone**

The writing is precise, professional, and technically fluent. The tone aligns with academic standards and demonstrates clarity in communicating complex procedural and analytical details.

---

### **Overall Impact and Defense Readiness**

The candidate demonstrates **clinical insight, procedural understanding, and analytical competence**. The work reflects readiness for independent research and advanced training in interventional radiology.

The thesis successfully bridges **clinical practice with research methodology**, making it a valuable contribution to the field and an excellent foundation for future academic and clinical endeavors.

---

## **2. Research Excellence and Innovation Assessment**

**Reviewer:** *Dr. Michael Chen, PhD*

**(Senior Research Scientist – Interventional Radiology Research Lab, Johns Hopkins University)*

This work represents a **methodologically sound investigation** into an important clinical question with significant implications for procedural optimization and patient outcomes.

---

### **Originality and Contribution**

The research addresses a **clinically relevant gap** in TIPS optimization by examining the impact of constraining underdilated shunts. While the concept of constraining stents is not entirely novel, the **systematic evaluation of clinical outcomes** provides valuable empirical evidence.

The contribution lies in the **quantitative assessment** of revision rates and hemodynamic changes, offering actionable insights for clinical practice.

---

### **Research Question and Objectives**

The research question is **well-defined and clinically meaningful**. The objectives are clear and directly address the clinical need for optimizing TIPS procedures.

The study design appropriately focuses on **patient-centered outcomes** while maintaining scientific rigor in data collection and analysis.

---

### **Literature Review**

The literature review provides adequate background on TIPS development and current practices. However, it could benefit from **deeper integration of recent research** on stent mechanics and flow dynamics.

Including more **comparative studies** and **meta-analyses** would strengthen the theoretical foundation and contextualize the current findings.

---

### **Methodology and Study Design**

The **retrospective cohort design** is appropriate for the research question. The methodology is well-described with clear inclusion/exclusion criteria.

The statistical approach is sound, though **propensity score matching** or **multivariate analysis** could help address potential confounding variables and strengthen the causal inference.

---

### **Results and Data Analysis**

The results are **clearly presented** with appropriate statistical analysis. The use of survival analysis for revision rates is particularly appropriate.

The findings demonstrate **statistical significance** and clinical relevance, with clear implications for procedural optimization.

---

### **Discussion and Interpretation**

The discussion effectively interprets the results in the context of existing literature. The **limitations are appropriately acknowledged**, including the retrospective nature and potential selection bias.

The implications for **clinical practice and future research** are well-articulated, providing a clear path forward for the field.

---

### **Ethical and Regulatory Compliance**

The study demonstrates **excellent adherence** to ethical standards with proper IRB oversight and data protection measures.

The **transparent reporting** of methodology and limitations reflects high ethical standards in clinical research.

---

### **Structure, Organization, and Presentation**

The thesis is **well-organized** with logical flow and clear presentation of data. Figures and tables effectively support the narrative.

The **academic writing style** is appropriate and maintains scientific rigor throughout.

---

### **Writing Quality and Scholarly Tone**

The writing demonstrates **strong scientific communication skills** with clear, concise language appropriate for the target audience.

The **technical terminology** is used correctly and consistently throughout the document.

---

### **Overall Impact and Defense Readiness**

This work makes a **valuable contribution** to the field of interventional radiology and demonstrates the candidate's readiness for advanced research and clinical practice.

The **defense readiness** is high, with the candidate well-prepared to discuss methodology, results, and implications.

---

## **3. Industry and Clinical Practice Perspective**

**Reviewer:** *Dr. Jennifer Martinez, MD*

**(Senior Medical Director – Interventional Radiology, MedTech Solutions Inc.)*

This thesis addresses a **practical clinical challenge** with direct implications for device design and procedural optimization in interventional radiology.

---

### **Originality and Contribution**

The research provides **practical insights** into TIPS optimization that could influence device design and clinical protocols. The focus on constraining underdilated shunts addresses a **real-world clinical problem**.

The contribution is particularly valuable for **industry applications** and could inform future device development and training protocols.

---

### **Research Question and Objectives**

The research question is **highly relevant** to clinical practice and addresses a common challenge in TIPS procedures. The objectives are clear and actionable.

The study design appropriately balances **clinical relevance** with scientific rigor, making it valuable for both academic and industry audiences.

---

### **Literature Review**

The literature review provides **adequate context** for the research, though it could benefit from more **industry-focused perspectives** on device optimization and clinical outcomes.

Including more **real-world clinical data** and **industry reports** would strengthen the practical relevance of the study.

---

### **Methodology and Study Design**

The methodology is **clinically appropriate** and well-executed. The retrospective design is suitable for the research question and provides valuable real-world data.

The **statistical analysis** is robust and appropriate for the clinical outcomes being measured.

---

### **Results and Data Analysis**

The results provide **clear clinical insights** with practical implications for procedural optimization. The data presentation is effective and supports the study conclusions.

The findings offer **actionable recommendations** for clinical practice and device optimization.

---

### **Discussion and Interpretation**

The discussion effectively translates research findings into **practical clinical insights**. The implications for **device design and procedural optimization** are well-articulated.

The **industry perspective** is valuable and provides a different lens through which to view the research findings.

---

### **Ethical and Regulatory Compliance**

The study demonstrates **excellent compliance** with ethical and regulatory standards, which is crucial for industry applications and clinical implementation.

The **transparent methodology** and **ethical oversight** enhance the credibility and applicability of the findings.

---

### **Structure, Organization, and Presentation**

The thesis is **well-structured** and presents information in a logical, accessible manner. The **clinical focus** makes it particularly valuable for industry and clinical audiences.

The **practical recommendations** are clearly presented and actionable.

---

### **Writing Quality and Scholarly Tone**

The writing maintains **professional standards** while remaining accessible to clinical and industry audiences. The **technical accuracy** is high throughout.

The **practical focus** of the writing makes it valuable for real-world applications.

---

### **Overall Impact and Defense Readiness**

This work demonstrates **strong clinical insight** and practical understanding of interventional radiology procedures. The candidate shows readiness for **industry and clinical practice**.

The **defense readiness** is high, with the candidate well-prepared to discuss clinical implications and practical applications.

---

## **Summary and Recommendations**

### **Overall Assessment**

This thesis represents a **strong contribution** to the field of interventional radiology, combining academic rigor with practical clinical relevance. The work demonstrates the candidate's ability to conduct **methodologically sound research** while addressing real-world clinical challenges.

### **Key Strengths**

- **Novel approach** to TIPS optimization
- **Strong methodology** and statistical analysis
- **Clear clinical relevance** and practical implications
- **Excellent ethical compliance** and professional standards
- **Well-written** and professionally presented

### **Areas for Improvement**

- **Enhanced literature review** with more recent studies
- **Deeper statistical analysis** with multivariate approaches
- **Expanded discussion** of clinical implications
- **Industry perspective** integration

### **Defense Readiness**

The candidate demonstrates **high readiness** for thesis defense with strong understanding of methodology, results, and implications. The work is **defense-ready** with minor revisions.

### **Final Recommendation**

**PASS** - This thesis meets the standards for MD degree completion and represents a valuable contribution to the field. The candidate is **ready for defense** with minor revisions to enhance literature review and statistical analysis.

---

**Total Score: 8.5/10**

**Defense Recommendation: APPROVED with minor revisions**"""

        researcher_eval = """# **MD Thesis Evaluation Report**

**Title:** *Effect of Constraining Underdilated Transjugular Intrahepatic Portosystemic Shunts (TIPS)*

**Candidate:** *[Name]*

**Institution:** *Yale School of Medicine*

---

## **1. Research Excellence and Innovation Assessment**

**Reviewer:** *Dr. Michael Chen, PhD*

**(Senior Research Scientist – Interventional Radiology Research Lab, Johns Hopkins University)*

This work represents a **methodologically sound investigation** into an important clinical question with significant implications for procedural optimization and patient outcomes.

---

### **Originality and Contribution**

The research addresses a **clinically relevant gap** in TIPS optimization by examining the impact of constraining underdilated shunts. While the concept of constraining stents is not entirely novel, the **systematic evaluation of clinical outcomes** provides valuable empirical evidence.

The contribution lies in the **quantitative assessment** of revision rates and hemodynamic changes, offering actionable insights for clinical practice.

---

### **Research Question and Objectives**

The research question is **well-defined and clinically meaningful**. The objectives are clear and directly address the clinical need for optimizing TIPS procedures.

The study design appropriately focuses on **patient-centered outcomes** while maintaining scientific rigor in data collection and analysis.

---

### **Literature Review**

The literature review provides adequate background on TIPS development and current practices. However, it could benefit from **deeper integration of recent research** on stent mechanics and flow dynamics.

Including more **comparative studies** and **meta-analyses** would strengthen the theoretical foundation and contextualize the current findings.

---

### **Methodology and Study Design**

The **retrospective cohort design** is appropriate for the research question. The methodology is well-described with clear inclusion/exclusion criteria.

The statistical approach is sound, though **propensity score matching** or **multivariate analysis** could help address potential confounding variables and strengthen the causal inference.

---

### **Results and Data Analysis**

The results are **clearly presented** with appropriate statistical analysis. The use of survival analysis for revision rates is particularly appropriate.

The findings demonstrate **statistical significance** and clinical relevance, with clear implications for procedural optimization.

---

### **Discussion and Interpretation**

The discussion effectively interprets the results in the context of existing literature. The **limitations are appropriately acknowledged**, including the retrospective nature and potential selection bias.

The implications for **clinical practice and future research** are well-articulated, providing a clear path forward for the field.

---

### **Ethical and Regulatory Compliance**

The study demonstrates **excellent adherence** to ethical standards with proper IRB oversight and data protection measures.

The **transparent reporting** of methodology and limitations reflects high ethical standards in clinical research.

---

### **Structure, Organization, and Presentation**

The thesis is **well-organized** with logical flow and clear presentation of data. Figures and tables effectively support the narrative.

The **academic writing style** is appropriate and maintains scientific rigor throughout.

---

### **Writing Quality and Scholarly Tone**

The writing demonstrates **strong scientific communication skills** with clear, concise language appropriate for the target audience.

The **technical terminology** is used correctly and consistently throughout the document.

---

### **Overall Impact and Defense Readiness**

This work makes a **valuable contribution** to the field of interventional radiology and demonstrates the candidate's readiness for advanced research and clinical practice.

The **defense readiness** is high, with the candidate well-prepared to discuss methodology, results, and implications.

---

## **Summary and Recommendations**

### **Overall Assessment**

This thesis represents a **strong contribution** to the field of interventional radiology, combining academic rigor with practical clinical relevance. The work demonstrates the candidate's ability to conduct **methodologically sound research** while addressing real-world clinical challenges.

### **Key Strengths**

- **Novel approach** to TIPS optimization
- **Strong methodology** and statistical analysis
- **Clear clinical relevance** and practical implications
- **Excellent ethical compliance** and professional standards
- **Well-written** and professionally presented

### **Areas for Improvement**

- **Enhanced literature review** with more recent studies
- **Deeper statistical analysis** with multivariate approaches
- **Expanded discussion** of clinical implications
- **Industry perspective** integration

### **Defense Readiness**

The candidate demonstrates **high readiness** for thesis defense with strong understanding of methodology, results, and implications. The work is **defense-ready** with minor revisions.

### **Final Recommendation**

**PASS** - This thesis meets the standards for MD degree completion and represents a valuable contribution to the field. The candidate is **ready for defense** with minor revisions to enhance literature review and statistical analysis.

---

**Total Score: 8.2/10**

**Defense Recommendation: APPROVED with minor revisions**"""

        industry_eval = """# **MD Thesis Evaluation Report**

**Title:** *Effect of Constraining Underdilated Transjugular Intrahepatic Portosystemic Shunts (TIPS)*

**Candidate:** *[Name]*

**Institution:** *Yale School of Medicine*

---

## **1. Industry and Clinical Practice Perspective**

**Reviewer:** *Dr. Jennifer Martinez, MD*

**(Senior Medical Director – Interventional Radiology, MedTech Solutions Inc.)*

This thesis addresses a **practical clinical challenge** with direct implications for device design and procedural optimization in interventional radiology.

---

### **Originality and Contribution**

The research provides **practical insights** into TIPS optimization that could influence device design and clinical protocols. The focus on constraining underdilated shunts addresses a **real-world clinical problem**.

The contribution is particularly valuable for **industry applications** and could inform future device development and training protocols.

---

### **Research Question and Objectives**

The research question is **highly relevant** to clinical practice and addresses a common challenge in TIPS procedures. The objectives are clear and actionable.

The study design appropriately balances **clinical relevance** with scientific rigor, making it valuable for both academic and industry audiences.

---

### **Literature Review**

The literature review provides **adequate context** for the research, though it could benefit from more **industry-focused perspectives** on device optimization and clinical outcomes.

Including more **real-world clinical data** and **industry reports** would strengthen the practical relevance of the study.

---

### **Methodology and Study Design**

The methodology is **clinically appropriate** and well-executed. The retrospective design is suitable for the research question and provides valuable real-world data.

The **statistical analysis** is robust and appropriate for the clinical outcomes being measured.

---

### **Results and Data Analysis**

The results provide **clear clinical insights** with practical implications for procedural optimization. The data presentation is effective and supports the study conclusions.

The findings offer **actionable recommendations** for clinical practice and device optimization.

---

### **Discussion and Interpretation**

The discussion effectively translates research findings into **practical clinical insights**. The implications for **device design and procedural optimization** are well-articulated.

The **industry perspective** is valuable and provides a different lens through which to view the research findings.

---

### **Ethical and Regulatory Compliance**

The study demonstrates **excellent compliance** with ethical and regulatory standards, which is crucial for industry applications and clinical implementation.

The **transparent methodology** and **ethical oversight** enhance the credibility and applicability of the findings.

---

### **Structure, Organization, and Presentation**

The thesis is **well-structured** and presents information in a logical, accessible manner. The **clinical focus** makes it particularly valuable for industry and clinical audiences.

The **practical recommendations** are clearly presented and actionable.

---

### **Writing Quality and Scholarly Tone**

The writing maintains **professional standards** while remaining accessible to clinical and industry audiences. The **technical accuracy** is high throughout.

The **practical focus** of the writing makes it valuable for real-world applications.

---

### **Overall Impact and Defense Readiness**

This work demonstrates **strong clinical insight** and practical understanding of interventional radiology procedures. The candidate shows readiness for **industry and clinical practice**.

The **defense readiness** is high, with the candidate well-prepared to discuss clinical implications and practical applications.

---

## **Summary and Recommendations**

### **Overall Assessment**

This thesis represents a **strong contribution** to the field of interventional radiology, combining academic rigor with practical clinical relevance. The work demonstrates the candidate's ability to conduct **methodologically sound research** while addressing real-world clinical challenges.

### **Key Strengths**

- **Novel approach** to TIPS optimization
- **Strong methodology** and statistical analysis
- **Clear clinical relevance** and practical implications
- **Excellent ethical compliance** and professional standards
- **Well-written** and professionally presented

### **Areas for Improvement**

- **Enhanced literature review** with more recent studies
- **Deeper statistical analysis** with multivariate approaches
- **Expanded discussion** of clinical implications
- **Industry perspective** integration

### **Defense Readiness**

The candidate demonstrates **high readiness** for thesis defense with strong understanding of methodology, results, and implications. The work is **defense-ready** with minor revisions.

### **Final Recommendation**

**PASS** - This thesis meets the standards for MD degree completion and represents a valuable contribution to the field. The candidate is **ready for defense** with minor revisions to enhance literature review and statistical analysis.

---

**Total Score: 8.0/10**

**Defense Recommendation: APPROVED with minor revisions**"""

        # Generate Chief Guide insights
        chief_guide_insights = generate_chief_guide_insights(professor_eval, researcher_eval, industry_eval)
        
        return chief_guide_insights
        
    except Exception as e:
        return f"❌ **Error during analysis**: {str(e)}"

def generate_chief_guide_insights(professor_eval, researcher_eval, industry_eval):
    """
    Generate Chief Guide insights based on the three expert evaluations
    """
    try:
        client = setup_openai()
        
        # Sample thesis text for context
        thesis_text = """Effect of Constraining Underdilated Transjugular Intrahepatic Portosystemic Shunts (TIPS)

This study investigates the clinical outcomes of constraining underdilated TIPS procedures, focusing on the impact of stent constraining on revision rates and hemodynamic changes. The research employs a retrospective cohort design to evaluate the effectiveness of this procedural modification in improving patient outcomes and reducing complications associated with TIPS procedures."""

        prompt = f"""
You are Dr. Alexander Thompson, Chief Academic Guide and Director of Medical Education at a prestigious medical university. You have 30+ years of experience in medical education, have supervised over 500 MD theses, and are renowned for your ability to synthesize multiple expert opinions into actionable guidance for students.

**Your Role:**
- Meta-evaluator who analyzes other experts' evaluations
- Strategic advisor for student development
- Bridge between different perspectives
- Final authority on thesis readiness and improvement priorities

**ORIGINAL THESIS:**
{thesis_text}

**EXPERT EVALUATIONS:**

🏥 MEDICAL COLLEGE PROFESSOR EVALUATION:
{professor_eval}

🔬 RENOWNED RESEARCHER EVALUATION:
{researcher_eval}

🏭 INDUSTRY MEDICAL PROFESSIONAL EVALUATION:
{industry_eval}

**YOUR TASK:**
As Chief Guide, analyze these three evaluations and provide strategic insights. Focus on:

1. **Clear Agreement Analysis**: What do ALL three experts agree on?
2. **Clear Disagreement Analysis**: Where do experts have different views?
3. **Priority Assessment**: What are the most critical areas for improvement?
4. **Strategic Guidance**: What should be the student's next steps?
5. **Defense Readiness**: Is the student ready for defense, and what preparation is needed?

**CRITICAL REQUIREMENTS:**
- Base ALL insights and recommendations ONLY on what the three experts actually said
- Extract SPECIFIC technical details from each expert's feedback
- Quote or reference specific points made by each expert
- Be TECHNICAL and SPECIFIC, not generic
- Use actual terminology and concepts mentioned by the experts
- Make agreement and disagreement points VERY CLEAR with specific examples
- When experts disagree, clearly identify which expert(s) hold each view with their exact words
- Focus on actionable insights that help the student improve
- Use proper line separation and formatting
- Include tabular format for final assessment

**FORMAT YOUR RESPONSE AS:**

# 🎯 Chief Guide Strategic Analysis

## 📊 Meta-Analysis Summary
[Provide a comprehensive overview of what the three evaluations collectively reveal about the thesis, highlighting the main themes and overall quality assessment.]

---

## 🔍 Expert Feedback Analysis

### POINTS OF AGREEMENT
*What ALL three experts agree on*

**STRENGTHS - All Experts Agree:**

**• [Criterion Name]**
[Extract specific technical details from all three experts' feedback. Quote specific phrases or concepts they mentioned. Be technical and specific, not generic.]

**• [Criterion Name]**
[Extract specific technical details from all three experts' feedback. Quote specific phrases or concepts they mentioned. Be technical and specific, not generic.]

**AREAS FOR IMPROVEMENT - All Experts Agree:**

**• [Criterion Name]**
[Extract specific technical details from all three experts' feedback. Quote specific phrases or concepts they mentioned. Be technical and specific, not generic.]

**• [Criterion Name]**
[Extract specific technical details from all three experts' feedback. Quote specific phrases or concepts they mentioned. Be technical and specific, not generic.]

### POINTS OF DISAGREEMENT
*Where experts have different views*

**[Criterion Name] - Expert Disagreement:**

**Dr. Joshua Cornman-Homonoff (Professor)**: [Quote or reference her specific technical view from her feedback]

**Dr. Michael Chen (Researcher)**: [Quote or reference his specific technical view from his feedback]

**Dr. Jennifer Martinez (Industry)**: [Quote or reference her specific technical view from her feedback]

**[Criterion Name] - Expert Disagreement:**

**Dr. Joshua Cornman-Homonoff (Professor)**: [Quote or reference her specific technical view from her feedback]

**Dr. Michael Chen (Researcher)**: [Quote or reference his specific technical view from her feedback]

**Dr. Jennifer Martinez (Industry)**: [Quote or reference her specific technical view from her feedback]

---

## Strategic Recommendations

### Immediate Priorities (Next 2-4 weeks)
*Most critical improvements needed*

**1. [Priority Area]**
**Action Required:** [Specific actions]
**Timeline:** **[Timeline]**
**Impact:** [Expected impact]

**2. [Priority Area]**
**Action Required:** [Specific actions]
**Timeline:** **[Timeline]**
**Impact:** [Expected impact]

**3. [Priority Area]**
**Action Required:** [Specific actions]
**Timeline:** **[Timeline]**
**Impact:** [Expected impact]

### Medium-term Development (1-3 months)
*Areas for deeper development*

**Skills to Strengthen:**

**[Skill Area]**
**Action Plan:** [How to develop]
**Expected Outcome:** [Why important]

**[Skill Area]**
**Action Plan:** [How to develop]
**Expected Outcome:** [Why important]

**Research Enhancement:**

**[Research Area]**
**Action Plan:** [Specific recommendations]
**Expected Outcome:** [Expected outcomes]

**[Research Area]**
**Action Plan:** [Specific recommendations]
**Expected Outcome:** [Expected outcomes]

---

## Defense Preparation Strategy

### Readiness Assessment
| **Assessment Area** | **Current Level** | **Target Level** | **Gap** |
|---------------------|-------------------|------------------|---------|
| **Overall Readiness** | [Current level] | [Target level] | [Gap analysis] |
| **Knowledge Mastery** | [Current level] | [Target level] | [Gap analysis] |
| **Presentation Skills** | [Current level] | [Target level] | [Gap analysis] |

### Key Preparation Areas
| **Topic Area** | **Preparation Required** | **Priority** | **Timeline** |
|----------------|-------------------------|--------------|--------------|
| **[Topic Area 1]** | [Specific preparation needed] | [High/Medium/Low] | [Timeline] |
| **[Topic Area 2]** | [Specific preparation needed] | [High/Medium/Low] | [Timeline] |
| **[Topic Area 3]** | [Specific preparation needed] | [High/Medium/Low] | [Timeline] |

---

## Final Assessment

### Quality Metrics
| **Criterion** | **Score** | **Assessment** | **Expert Consensus** |
|---------------|-----------|----------------|---------------------|
| **Overall Thesis Quality** | **[X]/10** | [Assessment level] | [What experts agreed on] |
| **Student Development Level** | **[Level]** | [Assessment level] | [What experts agreed on] |
| **Defense Readiness** | **[Level]** | [Assessment level] | [What experts agreed on] |
| **Research Contribution** | **[Level]** | [Assessment level] | [What experts agreed on] |
| **Clinical Relevance** | **[Level]** | [Assessment level] | [What experts agreed on] |

### Final Recommendation
| **Decision** | **Justification** | **Next Steps** |
|---------------|------------------|----------------|
| **[Pass with minor revisions/Pass with major revisions/Needs resubmission]** | [Clear explanation based on expert feedback] | [Specific next steps required] |
"""
        
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You are Dr. Alexander Thompson, Chief Academic Guide with 30+ years of experience in medical education. You excel at synthesizing multiple expert opinions into actionable strategic guidance for students."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=4000,
            temperature=0.7
        )
        
        return response.choices[0].message.content
        
    except Exception as e:
        return f"❌ **Error generating insights**: {str(e)}"

# Main Streamlit app
def main():
    # Sidebar
    with st.sidebar:
        st.markdown("""
        <div style="text-align: center; padding: 1rem 0;">
            <h2 style="color: #2c3e50; margin-bottom: 0.5rem;">🎓 Ethesis</h2>
            <p style="color: #6c757d; font-size: 0.9rem;">MD Thesis Analysis Platform</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("---")
        
        # Platform info
        st.markdown("### 📊 Platform Status")
        st.success("✅ System Online")
        st.info("🤖 AI Models Ready")
        st.warning("🔑 API Key Configured")
        
        st.markdown("---")
        
        # Quick stats
        st.markdown("### 📈 Analysis Statistics")
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Evaluations", "3", "Experts")
        with col2:
            st.metric("Criteria", "10", "Assessed")
        
        st.markdown("---")
        
        # Help section
        with st.expander("❓ Help & Support"):
            st.markdown("""
            **Getting Started:**
            1. Review the expert panel below
            2. Click "Generate Analysis" 
            3. Wait for AI processing
            4. Review comprehensive results
            
            **Need Help?**
            - Check the evaluation criteria
            - Review the analysis components
            - Contact support if issues persist
            """)
        
        # Settings
        with st.expander("⚙️ Settings"):
            st.markdown("**Analysis Options:**")
            show_detailed = st.checkbox("Show Detailed Analysis", value=True)
            include_recommendations = st.checkbox("Include Recommendations", value=True)
            defense_prep = st.checkbox("Defense Preparation", value=True)
        
        st.markdown("---")
        
        # Footer
        st.markdown("""
        <div style="text-align: center; color: #6c757d; font-size: 0.8rem;">
            <p>Powered by OpenAI GPT-4o</p>
            <p>© 2024 Ethesis Platform</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Header
    st.markdown("""
    <div class="main-header">
        <h1>🎓 Ethesis - MD Thesis Analysis Platform</h1>
        <p>Advanced AI-Powered Thesis Evaluation and Strategic Guidance</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Introduction section
    st.markdown("""
    <div class="process-steps">
        <h3 style="color: #2c3e50; margin-bottom: 1.5rem;">📋 How It Works</h3>
        <div class="step">
            <div class="step-number">1</div>
            <div class="step-text">Three expert evaluators analyze your thesis from different perspectives</div>
        </div>
        <div class="step">
            <div class="step-number">2</div>
            <div class="step-text">AI Chief Guide synthesizes all feedback into strategic insights</div>
        </div>
        <div class="step">
            <div class="step-number">3</div>
            <div class="step-text">Receive comprehensive analysis with actionable recommendations</div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Expert cards
    st.markdown("### 👥 Expert Evaluation Panel")
    st.markdown("Our AI-powered system simulates three distinct expert perspectives to provide comprehensive thesis analysis:")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="expert-card">
            <div class="expert-name">🏥 Dr. Joshua Cornman-Homonoff</div>
            <div class="expert-role">Medical College Professor</div>
            <div class="expert-focus">
                <strong>Educational Focus:</strong> Student development, clinical methodology, and academic standards. Evaluates learning outcomes and educational value.
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="expert-card">
            <div class="expert-name">🔬 Dr. Michael Chen</div>
            <div class="expert-role">Renowned Researcher</div>
            <div class="expert-focus">
                <strong>Research Focus:</strong> Scientific rigor, innovation, and methodological soundness. Assesses contribution to knowledge and research excellence.
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="expert-card">
            <div class="expert-name">🏭 Dr. Jennifer Martinez</div>
            <div class="expert-role">Industry Medical Professional</div>
            <div class="expert-focus">
                <strong>Clinical Focus:</strong> Real-world applications, industry relevance, and practical implementation. Emphasizes patient outcomes and clinical utility.
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    # Analysis section
    st.markdown("---")
    st.markdown("### 🧠 Generate Strategic Analysis")
    
    # Add some context about what the analysis includes
    with st.expander("📖 What's Included in the Analysis", expanded=False):
        st.markdown("""
        **The Chief Guide Analysis provides:**
        
        - **📊 Meta-Analysis Summary**: Overview of all expert evaluations
        - **🔍 Expert Feedback Analysis**: Points of agreement and disagreement
        - **🎯 Strategic Recommendations**: Immediate priorities and medium-term development
        - **📋 Defense Preparation Strategy**: Readiness assessment and preparation areas
        - **📈 Final Assessment**: Quality metrics and final recommendations
        
        **Evaluation Criteria:**
        1. Originality and Contribution
        2. Research Question and Objectives
        3. Literature Review
        4. Methodology and Study Design
        5. Results and Data Analysis
        6. Discussion and Interpretation
        7. Ethical and Regulatory Compliance
        8. Structure, Organization, and Presentation
        9. Writing Quality and Scholarly Tone
        10. Overall Impact and Defense Readiness
        """)
    
    # Analysis button with enhanced styling
    col_btn1, col_btn2, col_btn3 = st.columns([1, 2, 1])
    
    with col_btn2:
        if st.button("🚀 Generate Chief Guide Insights & Summary", type="primary", use_container_width=True):
            # Create a more engaging loading experience
            progress_bar = st.progress(0)
            status_text = st.empty()
            
            # Simulate progress steps
            steps = [
                "🔍 Analyzing expert evaluations...",
                "🧠 Synthesizing feedback from all perspectives...",
                "📊 Generating strategic recommendations...",
                "📋 Preparing defense readiness assessment...",
                "✅ Finalizing comprehensive analysis..."
            ]
            
            for i, step in enumerate(steps):
                progress_bar.progress((i + 1) / len(steps))
                status_text.text(step)
                import time
                time.sleep(0.5)  # Small delay for better UX
            
            # Clear progress indicators
            progress_bar.empty()
            status_text.empty()
            
            # Generate analysis
            analysis_result = generate_complete_analysis()
            
            # Display results with enhanced styling
            st.markdown("""
            <div class="analysis-output">
                <h2>📊 Strategic Analysis Results</h2>
                <p style="color: #6c757d; font-style: italic; margin-bottom: 2rem;">
                    Comprehensive analysis generated by Dr. Alexander Thompson, Chief Academic Guide
                </p>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown(analysis_result)
            
            # Add download option for the analysis
            st.markdown("---")
            st.markdown("### 💾 Download Analysis")
            st.markdown("Save your analysis for future reference:")
            
            col_download1, col_download2, col_download3 = st.columns([1, 1, 1])
            
            with col_download1:
                if st.button("📄 Download as Text", use_container_width=True):
                    st.download_button(
                        label="Download Analysis",
                        data=analysis_result,
                        file_name="thesis_analysis.txt",
                        mime="text/plain"
                    )
            
            with col_download2:
                if st.button("📋 Copy to Clipboard", use_container_width=True):
                    st.code(analysis_result, language="markdown")
            
            with col_download3:
                if st.button("🔄 Generate New Analysis", use_container_width=True):
                    st.rerun()
    
    # Footer with additional information
    st.markdown("---")
    st.markdown("""
    <div style="text-align: center; color: #6c757d; padding: 2rem 0;">
        <p><strong>Ethesis Platform</strong> - Powered by Advanced AI Technology</p>
        <p>Comprehensive MD Thesis Analysis and Strategic Guidance</p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()

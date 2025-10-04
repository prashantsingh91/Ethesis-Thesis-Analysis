import gradio as gr
from openai import OpenAI
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Configure OpenAI API
def setup_openai():
    """Setup OpenAI client"""
    api_key = os.getenv('OPENAI_API_KEY')
    if not api_key:
        raise ValueError("Please set OPENAI_API_KEY environment variable or create a .env file with your API key")
    return OpenAI(api_key=api_key)

# Thesis evaluation criteria
EVALUATION_CRITERIA = [
    "1. Originality and Contribution",
    "2. Research Question and Objectives", 
    "3. Literature Review",
    "4. Methodology and Study Design",
    "5. Results and Data Analysis",
    "6. Discussion and Interpretation",
    "7. Ethical and Regulatory Compliance",
    "8. Structure, Organization, and Presentation",
    "9. Writing Quality and Scholarly Tone",
    "10. Overall Impact and Defense Readiness"
]


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

Findings contribute meaningful evidence toward **TIPS optimization and procedural safety**.

---

### **Final Thoughts**

This thesis is **technically rigorous, clinically relevant, and ethically sound**. It exemplifies how procedural modification and hemodynamic reasoning can directly enhance patient outcomes.

The work provides a foundation for **prospective multicenter trials, computational flow modeling, and device innovation**.

An **excellent academic effort** that reflects both technical maturity and educational growth."""

        researcher_eval = """## **2. Renowned Researcher (Dr. Michael Chen)**

### **Research Excellence Perspective — Scientific and Clinical Contribution**

---

### **1. Originality and Contribution**

This thesis presents a **biomechanical innovation** in TIPS management through the use of constraining underdilated shunts. The application of mechanical constraint to regulate shunt expansion is novel, data-driven, and clinically meaningful.

It contributes to scientific understanding of **flow dynamics and procedural control**, offering a reproducible approach that bridges clinical practice and device engineering.

---

### **2. Research Question and Objectives**

The research question is well-defined and clinically important, addressing how constraint impacts procedural success and patient outcomes.

While comprehensive, future research could include additional **patient-centric endpoints**—for example, hepatic function trajectory or encephalopathy grade—to expand translational impact.

---

### **3. Literature Review**

The literature review is conceptually strong and technically contextualized. However, inclusion of **recent computational or material-science studies** on constrained or adaptive TIPS systems would further strengthen the scientific relevance and underscore novelty.

---

### **4. Methodology and Study Design**

The retrospective cohort model is appropriate and well implemented. Procedural descriptions and selection criteria are clearly articulated.

Introducing **propensity scoring, regression adjustment, or Cox proportional hazards modeling** would mitigate selection bias and quantify time-dependent outcomes more robustly.

---

### **5. Results and Data Analysis**

The results are clear, well-analyzed, and statistically valid. The finding of increased revision rates with constrained TIPS, coupled with comparable mortality, is physiologically logical and clinically defensible.

Inclusion of **effect-size estimates and confidence intervals** would enhance interpretive rigor.

---

### **6. Discussion and Interpretation**

The discussion demonstrates mature analytical reasoning and situates the findings within the continuum of TIPS evolution. The explanation of higher gradients due to constrained expansion is coherent and supported by both physics and data.

Further discussion of **device-level implications** and **procedural training integration** could enhance long-term relevance.

---

### **7. Ethical and Regulatory Compliance**

Ethical conduct and data governance are thoroughly documented. IRB exemption, data encryption, and HIPAA compliance are properly executed.

Adding a short discussion on the **ethical balance between under-shunting and encephalopathy prevention** would elevate the reflection.

---

### **8. Structure, Organization, and Presentation**

The structure is consistent and methodical. Figures, tables, and legends are clear. Minor condensation of the introduction could improve pacing, and the addition of a **procedural schematic** could further aid understanding.

---

### **9. Writing Quality and Scholarly Tone**

The thesis maintains an academic tone, with terminology and formatting aligned with journal standards in interventional radiology.

Minor edits to remove redundancy and standardize statistical reporting are suggested.

---

### **10. Overall Impact and Defense Readiness**

This is a **scientifically sound, technically rigorous, and clinically valuable** thesis. The candidate demonstrates an advanced understanding of hemodynamics, device behavior, and research methodology.

The findings have potential to influence future **device development and procedural optimization**.

---

### **Final Thoughts**

This work represents a **significant contribution** to the scientific literature on TIPS modulation. It combines **mechanistic precision, ethical discipline, and translational relevance**.

With minor refinements in statistical methodology and contextual depth, it is **well suited for publication in a high-impact interventional journal**.

The author demonstrates clear scientific maturity and the potential to lead independent clinical research."""

        industry_eval = """## **3. Industry Medical Professional (Dr. Jennifer Martinez)**

### **Practical Application Perspective — Focus on Real-world Impact**

---

### **1. Originality and Contribution**

This thesis presents a **clinically innovative procedural modification**—constraining underdilated shunts to optimize decompression while minimizing over-shunting. The concept directly addresses a daily clinical challenge in TIPS management and has **strong real-world relevance**.

By connecting procedural mechanics to clinical outcomes, the work bridges academic inquiry with applied interventional practice.

---

### **2. Research Question and Objectives**

The research question is clear, operationally relevant, and grounded in clinical experience.

The objectives could be refined by defining **quantitative outcome measures** such as revision-free survival or post-TIPS encephalopathy incidence. Incorporating explicit hypotheses would support prospective validation.

---

### **3. Literature Review**

The review effectively traces TIPS evolution but should include **recent literature on controlled or adjustable-flow TIPS technologies**. Highlighting the gap in standardization for constrained shunts would underscore the study's industrial relevance.

---

### **4. Methodology and Study Design**

The single-center retrospective design is practical for early-phase procedural evaluation. The methodology is transparent and replicable.

For wider implementation, future research should adopt **prospective multicenter protocols** and include operator-level data to standardize technique reproducibility. Adjusting for MELD variation and procedural indication would enhance real-world applicability.

---

### **5. Results and Data Analysis**

The results are robustly analyzed and clinically meaningful. The demonstration that constrained TIPS increases revision frequency without elevating mortality is consistent with procedural trade-offs observed in practice.

Subgroup analyses (e.g., refractory ascites vs. variceal bleed) and inclusion of **post-TIPS Doppler flow assessments** would further strengthen translational value.

---

### **6. Discussion and Interpretation**

The discussion connects outcomes to procedural workflows, reflecting strong clinical insight.

Expanding commentary on **patient selection criteria**, **cost-effectiveness**, and **workflow integration** would enhance its direct relevance to hospital practice and health systems optimization.

---

### **7. Ethical and Regulatory Compliance**

Ethical standards are clearly upheld. IRB exemption and HIPAA compliance are well documented. The attention to patient privacy and data security aligns with both academic and industry norms.

---

### **8. Structure, Organization, and Presentation**

The thesis is well structured with coherent flow and clear visual data presentation.

Minor refinements in formatting consistency and inclusion of a **workflow schematic or decision tree** could further improve clarity for practitioners.

---

### **9. Writing Quality and Scholarly Tone**

The writing is professional, accessible, and technically articulate. The candidate communicates complex procedural nuances with clarity suitable for both academic and clinical audiences.

Only minor stylistic polishing is needed for journal-level publication.

---

### **10. Overall Impact and Defense Readiness**

The thesis delivers **immediate clinical relevance** and demonstrates strong understanding of interventional decision-making.

Although retrospective, the data provide a **solid foundation for prospective evaluation and procedural standardization**.

The candidate is clearly prepared to defend both the technical rationale and the clinical implications of this work.

---

### **Final Thoughts**

This thesis exemplifies **practical clinical innovation**—a technique conceived, executed, and analyzed with direct applicability to real-world care.

It bridges procedural creativity with measurable patient benefit and lays groundwork for **next-generation controlled-flow shunt systems**.

The study demonstrates how academic research can translate seamlessly into **improved clinical outcomes and procedural efficiency** within interventional hepatology."""

        # Generate Chief Guide insights using the pre-written evaluations
        chief_guide_insights = generate_chief_guide_insights(
            "Effect of Constraining Underdilated Transjugular Intrahepatic Portosystemic Shunts (TIPS)", 
            professor_eval, 
            researcher_eval, 
            industry_eval
        )
        
        # Create display text with only Chief Guide analysis
        display_text = f"""
{chief_guide_insights}
"""
        
        return display_text
        
    except Exception as e:
        return f"Error during analysis: {str(e)}"

def generate_chief_guide_insights(thesis_text: str, professor_eval: str, researcher_eval: str, industry_eval: str) -> str:
    """
    Generate Chief Guide insights analyzing all three persona evaluations
    """
    try:
        # Setup OpenAI client
        client = setup_openai()
        
        # Create Chief Guide prompt
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

        ### ✅ **POINTS OF AGREEMENT**
        *What ALL three experts agree on*

        **🎯 STRENGTHS - All Experts Agree:**

        **• [Criterion Name]**
        [Extract specific technical details from all three experts' feedback. Quote specific phrases or concepts they mentioned. Be technical and specific, not generic.]

        **• [Criterion Name]**
        [Extract specific technical details from all three experts' feedback. Quote specific phrases or concepts they mentioned. Be technical and specific, not generic.]

        **⚠️ AREAS FOR IMPROVEMENT - All Experts Agree:**

        **• [Criterion Name]**
        [Extract specific technical details from all three experts' feedback. Quote specific phrases or concepts they mentioned. Be technical and specific, not generic.]

        **• [Criterion Name]**
        [Extract specific technical details from all three experts' feedback. Quote specific phrases or concepts they mentioned. Be technical and specific, not generic.]

        ### ⚠️ **POINTS OF DISAGREEMENT**
        *Where experts have different views*

        **🔴 [Criterion Name] - Expert Disagreement:**

        **Dr. Sarah Williams (Professor)**: [Quote or reference her specific technical view from her feedback]

        **Dr. Michael Chen (Researcher)**: [Quote or reference his specific technical view from his feedback]

        **Dr. Jennifer Martinez (Industry)**: [Quote or reference her specific technical view from her feedback]

        **🔴 [Criterion Name] - Expert Disagreement:**

        **Dr. Sarah Williams (Professor)**: [Quote or reference her specific technical view from her feedback]

        **Dr. Michael Chen (Researcher)**: [Quote or reference his specific technical view from his feedback]

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

        # Call OpenAI API
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You are Dr. Alexander Thompson, Chief Academic Guide with extensive experience in synthesizing multiple expert evaluations into strategic guidance for medical students."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=4000,
            temperature=0.3
        )
        
        return response.choices[0].message.content
        
    except Exception as e:
        return f"Error generating Chief Guide insights: {str(e)}"

def create_gradio_interface():
    """Create the Gradio interface"""
    
    with gr.Blocks(
        title="Ethesis - MD Thesis Analysis Dashboard", 
        theme=gr.themes.Soft(),
        css="""
        .dashboard-container {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            padding: 20px;
            border-radius: 15px;
            margin: 10px;
        }
        .metric-card {
            background: white;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            margin: 10px 0;
            border-left: 4px solid #667eea;
        }
        .priority-high {
            border-left-color: #e74c3c;
            background: #fdf2f2;
        }
        .priority-medium {
            border-left-color: #f39c12;
            background: #fef9e7;
        }
        .priority-low {
            border-left-color: #27ae60;
            background: #f0f9f0;
        }
        .section-header {
            background: linear-gradient(90deg, #667eea, #764ba2);
            color: white;
            padding: 15px;
            border-radius: 8px;
            margin: 20px 0 10px 0;
            font-weight: bold;
            text-align: center;
        }
        .expert-card {
            background: #f8f9fa;
            border: 1px solid #dee2e6;
            border-radius: 8px;
            padding: 15px;
            margin: 10px 0;
        }
        .progress-bar {
            background: #e9ecef;
            border-radius: 10px;
            height: 20px;
            overflow: hidden;
            margin: 5px 0;
        }
        .progress-fill {
            height: 100%;
            background: linear-gradient(90deg, #667eea, #764ba2);
            border-radius: 10px;
            transition: width 0.3s ease;
        }
        .dashboard-button {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%) !important;
            border: none !important;
            color: white !important;
            font-weight: bold !important;
            padding: 15px 30px !important;
            border-radius: 10px !important;
            box-shadow: 0 4px 15px rgba(102, 126, 234, 0.4) !important;
            transition: all 0.3s ease !important;
        }
        .dashboard-button:hover {
            transform: translateY(-2px) !important;
            box-shadow: 0 6px 20px rgba(102, 126, 234, 0.6) !important;
        }
        """
    ) as interface:
        # Dashboard Header
        with gr.Row():
            gr.HTML("""
            <div class="dashboard-container">
                <h1 style="color: white; text-align: center; margin: 0; font-size: 2.5em;">🎓 Ethesis Dashboard</h1>
                <p style="color: white; text-align: center; margin: 10px 0 0 0; font-size: 1.2em;">MD Thesis Analysis & Strategic Insights</p>
            </div>
            """)
        
        # Expert Panel Cards
        gr.HTML('<div class="section-header">👥 Expert Evaluation Panel</div>')
        with gr.Row():
            with gr.Column():
                gr.HTML("""
                <div class="expert-card">
                    <h3 style="color: #667eea; margin: 0;">🏥 Dr. Sarah Williams</h3>
                    <p style="color: #666; margin: 5px 0;"><em>Medical College Professor</em></p>
                    <p style="margin: 0;"><strong>Focus:</strong> Educational value, student development, academic standards</p>
                </div>
                """)
            with gr.Column():
                gr.HTML("""
                <div class="expert-card">
                    <h3 style="color: #667eea; margin: 0;">🔬 Dr. Michael Chen</h3>
                    <p style="color: #666; margin: 5px 0;"><em>Renowned Researcher</em></p>
                    <p style="margin: 0;"><strong>Focus:</strong> Scientific rigor, innovation, contribution to the field</p>
                </div>
                """)
            with gr.Column():
                gr.HTML("""
                <div class="expert-card">
                    <h3 style="color: #667eea; margin: 0;">🏭 Dr. Jennifer Martinez</h3>
                    <p style="color: #666; margin: 5px 0;"><em>Industry Medical Professional</em></p>
                    <p style="margin: 0;"><strong>Focus:</strong> Practical applications, clinical relevance, real-world impact</p>
                </div>
                """)
        
        # Analysis Section
        gr.HTML('<div class="section-header">🚀 Analysis Generation</div>')
        with gr.Row():
            with gr.Column(scale=2):
                # Analysis controls
                gr.HTML("""
                <div class="metric-card">
                    <h3 style="color: #667eea; margin: 0 0 15px 0;">⚙️ Analysis Configuration</h3>
                    <p style="color: #666; margin: 10px 0;">Click the button below to generate comprehensive strategic analysis from our expert panel.</p>
                """)
                
                # Chief Guide button
                with gr.Row():
                    generate_insights_btn = gr.Button(
                        "🎯 Generate Strategic Analysis", 
                        variant="primary", 
                        size="lg",
                        elem_classes=["dashboard-button"]
                    )
                
                gr.HTML("</div>")
                
            with gr.Column(scale=3):
                # Output section
                gr.HTML('<div class="section-header">📊 Strategic Analysis Dashboard</div>')
                
                analysis_output = gr.Markdown(
                    label="Strategic Analysis",
                    elem_classes=["metric-card"]
                )
                
        
        # Example section
        with gr.Accordion("📋 Evaluation Criteria", open=False):
            gr.Markdown(f"""
**The system evaluates theses on these 10 criteria:**

{chr(10).join([f"• {criterion}" for criterion in EVALUATION_CRITERIA])}

**Rating Scale:**
- **Strong**: Exceeds expectations, demonstrates excellence
- **Adequate**: Meets basic requirements, satisfactory quality  
- **Weak**: Below expectations, needs significant improvement

**Output includes:**
- Detailed evaluation for each criterion
- Overall score (1-10)
- Strengths and weaknesses summary
- Improvement suggestions
- Defense readiness assessment
            """)
        
        # Persona descriptions
        with gr.Accordion("🎭 Evaluation Personas", open=False):
            gr.Markdown("""
### 🏥 Medical College Professor (Dr. Sarah Williams)
- **Focus**: Educational value, student development, academic standards
- **Style**: Supportive, encouraging, emphasis on learning
- **Perspective**: Thesis as a learning exercise and preparation for practice

### 🔬 Renowned Researcher (Dr. Michael Chen)  
- **Focus**: Scientific rigor, innovation, contribution to the field
- **Style**: Critical, analytical, emphasis on research excellence
- **Perspective**: Thesis as a potential scientific contribution

### 🏭 Industry Medical Professional (Dr. Jennifer Martinez)
- **Focus**: Practical applications, clinical relevance, real-world impact
- **Style**: Practical, application-focused, emphasis on implementation
- **Perspective**: Thesis from healthcare system and patient care viewpoint
            """)
        
        # Event handler for Chief Guide analysis
        generate_insights_btn.click(
            fn=generate_complete_analysis,
            inputs=[],
            outputs=analysis_output
        )
        
    
    return interface

if __name__ == "__main__":
    # Create and launch the interface
    interface = create_gradio_interface()
    interface.launch(
        server_name="0.0.0.0",
        server_port=7860,
        share=False,
        show_error=True
    )

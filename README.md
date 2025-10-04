# 🎓 Ethesis - MD Thesis Analysis Platform

A sophisticated AI-powered application for analyzing MD thesis reports using advanced language models. The platform provides comprehensive evaluations from multiple expert perspectives and generates strategic insights for thesis improvement.

## Features

- **Multi-Persona Evaluation**: Three distinct expert perspectives (Medical College Professor, Renowned Researcher, Industry Medical Professional)
- **Chief Guide Analysis**: Meta-evaluation that synthesizes expert feedback into actionable strategic recommendations
- **Advanced AI Integration**: Powered by OpenAI's GPT-4o for sophisticated analysis
- **Professional Dashboard**: Clean, intuitive Streamlit interface with expert cards and strategic analysis
- **Comprehensive Assessment**: 10-criteria evaluation system covering all aspects of thesis quality
- **Easy Deployment**: Ready for deployment on Streamlit Cloud, Railway, Render, or Hugging Face Spaces

## Expert Personas

### 🏥 Medical College Professor (Dr. Joshua Cornman-Homonoff)
- **Focus**: Educational perspective, clinical methodology, and student development
- **Emphasis**: Learning outcomes, academic standards, and clinical competence

### 🔬 Renowned Researcher (Dr. Michael Chen)
- **Focus**: Research excellence, innovation, and scientific rigor
- **Emphasis**: Methodological soundness, contribution to knowledge, and research impact

### 🏭 Industry Medical Professional (Dr. Jennifer Martinez)
- **Focus**: Clinical practice relevance, industry applications, and real-world impact
- **Emphasis**: Practical implementation, patient outcomes, and clinical utility

## Setup Instructions

### Prerequisites
- Python 3.8 or higher
- OpenAI API key

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd Ethesis
   ```

2. **Create and activate virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   Create a `.env` file in the project root:
   ```bash
   OPENAI_API_KEY=your-openai-api-key-here
   ```

5. **Run the application**
   ```bash
   streamlit run src/streamlit_app.py
   ```

6. **Access the application**
   Open your browser and navigate to `http://localhost:8501`

## Deployment Options

### 🚀 Streamlit Cloud (Recommended)
- **Free tier**: Unlimited public apps
- **Deployment**: Connect GitHub repo, auto-deploy
- **URL**: `https://your-app-name.streamlit.app`

### 🚂 Railway
- **Free tier**: $5 credit monthly
- **Deployment**: Connect GitHub, auto-deploy
- **Features**: Custom domains, databases

### 🎨 Render
- **Free tier**: 750 hours/month
- **Deployment**: Connect GitHub, configure build
- **Features**: Auto-deployments, custom domains

### 🤗 Hugging Face Spaces
- **Free tier**: Unlimited spaces
- **Deployment**: Upload files, auto-deploy
- **Features**: Great for ML/AI apps

See [DEPLOYMENT.md](DEPLOYMENT.md) for detailed deployment instructions.

## Usage

1. **Launch the Application**: The app will open with a dashboard showing three expert personas
2. **Generate Analysis**: Click "Generate Chief Guide Insights & Summary" to start the analysis
3. **Review Results**: The Chief Guide will provide comprehensive strategic analysis including:
   - Meta-analysis of expert feedback
   - Points of agreement and disagreement
   - Strategic recommendations
   - Defense preparation strategy
   - Final assessment and recommendations

## Project Structure

```
Ethesis/
├── src/
│   ├── app.py              # Original Gradio app
│   └── streamlit_app.py    # Streamlit version
├── requirements.txt        # Python dependencies
├── .env                   # Environment variables (create this)
├── DEPLOYMENT.md          # Deployment guide
├── setup.sh              # Setup script
└── README.md             # This file
```

## Evaluation Criteria

The system evaluates theses on 10 comprehensive criteria:

1. **Originality and Contribution**
2. **Research Question and Objectives**
3. **Literature Review**
4. **Methodology and Study Design**
5. **Results and Data Analysis**
6. **Discussion and Interpretation**
7. **Ethical and Regulatory Compliance**
8. **Structure, Organization, and Presentation**
9. **Writing Quality and Scholarly Tone**
10. **Overall Impact and Defense Readiness**

## Technology Stack

- **Frontend**: Streamlit 1.28+
- **AI Model**: OpenAI GPT-4o
- **Language**: Python 3.8+
- **Environment Management**: python-dotenv

## Quick Deploy

```bash
# 1. Push to GitHub
git add .
git commit -m "Ready for deployment"
git push origin main

# 2. Deploy to Streamlit Cloud
# Go to share.streamlit.io and deploy from GitHub
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

This project is licensed under the MIT License.

## Support

For support or questions, please open an issue in the repository.
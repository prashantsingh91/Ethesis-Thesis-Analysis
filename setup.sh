#!/bin/bash

# Ethesis Setup Script
echo "🎓 Setting up Ethesis - MD Thesis Analysis Dashboard"

# Activate the medgemma virtual environment
echo "📦 Activating medgemma_env virtual environment..."
source /home/psingh/medgemma/medgemma_env/bin/activate

# Install requirements
echo "📥 Installing dependencies..."
pip install -r requirements.txt

# Check for OpenAI API key
if [ -z "$OPENAI_API_KEY" ]; then
    echo "⚠️  Warning: OPENAI_API_KEY environment variable not set"
    echo "   The app has a default API key configured, but you can set your own with:"
    echo "   export OPENAI_API_KEY='your-api-key-here'"
else
    echo "✅ OpenAI API key is configured"
fi

echo "🚀 Setup complete! Run the dashboard with: python src/app.py"
echo "📊 The dashboard will be available at: http://localhost:7862"
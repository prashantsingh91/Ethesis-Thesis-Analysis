# 🚀 Ethesis App Deployment Guide

## 📋 Overview
This guide covers deploying your Ethesis Streamlit app to various free platforms.

## 🎯 Deployment Options

### 1. Streamlit Cloud (Recommended - Easiest)

**Steps:**
1. **Push to GitHub** (if not already done)
   ```bash
   git add .
   git commit -m "Convert to Streamlit app"
   git push origin main
   ```

2. **Deploy on Streamlit Cloud**
   - Go to [share.streamlit.io](https://share.streamlit.io)
   - Sign in with GitHub
   - Click "New app"
   - Select your repository: `your-username/Ethesis`
   - Main file path: `src/streamlit_app.py`
   - Branch: `main`
   - Click "Deploy!"

3. **Set Environment Variables**
   - In Streamlit Cloud dashboard, go to "Settings"
   - Add environment variable: `OPENAI_API_KEY` = `your-actual-api-key`

**Pros:** 
- ✅ Completely free
- ✅ Automatic HTTPS
- ✅ Easy deployment
- ✅ Built for Streamlit

**Cons:**
- ❌ Public by default
- ❌ Limited to Streamlit apps

---

### 2. Railway

**Steps:**
1. **Create Railway Account**
   - Go to [railway.app](https://railway.app)
   - Sign up with GitHub

2. **Deploy from GitHub**
   - Click "New Project"
   - Select "Deploy from GitHub repo"
   - Choose your Ethesis repository
   - Railway will auto-detect it's a Python app

3. **Configure Environment**
   - Add environment variable: `OPENAI_API_KEY`
   - Railway will auto-deploy

4. **Create Procfile** (if needed)
   ```bash
   echo "web: streamlit run src/streamlit_app.py --server.port=$PORT --server.address=0.0.0.0" > Procfile
   ```

**Pros:**
- ✅ $5 free credit monthly
- ✅ Supports databases
- ✅ Good for full-stack apps
- ✅ Custom domains

**Cons:**
- ❌ Limited free tier
- ❌ More complex setup

---

### 3. Render

**Steps:**
1. **Create Render Account**
   - Go to [render.com](https://render.com)
   - Sign up with GitHub

2. **Create Web Service**
   - Click "New +" → "Web Service"
   - Connect your GitHub repository
   - Choose "Ethesis" repository

3. **Configure Service**
   - **Name:** `ethesis-app`
   - **Environment:** `Python 3`
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `streamlit run src/streamlit_app.py --server.port=$PORT --server.address=0.0.0.0`

4. **Set Environment Variables**
   - Add `OPENAI_API_KEY` in environment section

**Pros:**
- ✅ 750 hours free monthly
- ✅ Automatic deployments
- ✅ Custom domains
- ✅ Good documentation

**Cons:**
- ❌ Apps sleep after inactivity
- ❌ Limited free tier

---

### 4. Hugging Face Spaces

**Steps:**
1. **Create Hugging Face Account**
   - Go to [huggingface.co](https://huggingface.co)
   - Sign up

2. **Create New Space**
   - Click "Create new Space"
   - **Name:** `ethesis-app`
   - **SDK:** `Streamlit`
   - **Visibility:** Public or Private

3. **Upload Files**
   - Upload your `src/streamlit_app.py`
   - Upload `requirements.txt`
   - Create `.env` file with your API key

4. **Deploy**
   - Hugging Face will auto-deploy
   - Your app will be available at: `https://huggingface.co/spaces/your-username/ethesis-app`

**Pros:**
- ✅ Completely free
- ✅ Great for ML/AI apps
- ✅ Built-in GPU support
- ✅ Easy sharing

**Cons:**
- ❌ Public by default
- ❌ Limited to ML/AI use cases

---

## 🔧 Local Testing

Before deploying, test locally:

```bash
# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run src/streamlit_app.py

# App will be available at http://localhost:8501
```

---

## 📝 Environment Variables

All platforms require setting the `OPENAI_API_KEY` environment variable:

```bash
OPENAI_API_KEY=sk-proj-your-actual-api-key-here
```

**⚠️ Security Note:** Never commit your actual API key to GitHub. Use environment variables or `.env` files.

---

## 🎯 Recommended Deployment Path

1. **Start with Streamlit Cloud** - Easiest and most reliable
2. **If you need more features** - Try Railway or Render
3. **For ML/AI focus** - Consider Hugging Face Spaces

---

## 🆘 Troubleshooting

### Common Issues:

1. **App won't start**
   - Check `requirements.txt` has all dependencies
   - Verify environment variables are set
   - Check logs in deployment platform

2. **API key not working**
   - Ensure environment variable is set correctly
   - Verify API key is valid and has credits

3. **Import errors**
   - Make sure all dependencies are in `requirements.txt`
   - Check Python version compatibility

### Getting Help:
- Check platform-specific documentation
- Look at deployment logs
- Test locally first

---

## 🚀 Quick Start Commands

```bash
# Test locally
streamlit run src/streamlit_app.py

# Deploy to Streamlit Cloud
# 1. Push to GitHub
git add .
git commit -m "Ready for deployment"
git push origin main

# 2. Go to share.streamlit.io and deploy
```

Your app will be live and accessible worldwide! 🌍

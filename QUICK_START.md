# Quick Start - Deploy to Streamlit Cloud

## Fast Track (5 minutes)

### 1. Initialize Git (Terminal)
```bash
cd "/Users/udoysaha/Desktop/Stock Simulator"
git init
git add .
git commit -m "Initial commit"
```

### 2. Create GitHub Repo
- Go to https://github.com/new
- Name: `stock-portfolio-simulator`
- Make it **Public**
- Click "Create repository"

### 3. Push to GitHub
```bash
git remote add origin https://github.com/YOUR_USERNAME/stock-portfolio-simulator.git
git branch -M main
git push -u origin main
```
*(Use Personal Access Token if prompted for password)*

### 4. Deploy on Streamlit
- Go to https://share.streamlit.io/
- Click "New app"
- Select your repo
- Main file: `app.py`
- Click "Deploy"

**Done!** Your app will be live in 2-5 minutes.

---

For detailed instructions, see `DEPLOYMENT_GUIDE.md`


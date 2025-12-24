# Step-by-Step Deployment Guide for Streamlit Community Cloud

This guide will walk you through deploying your Stock Portfolio Simulator to Streamlit Community Cloud.

## Prerequisites

- A GitHub account (create one at https://github.com if you don't have one)
- Git installed on your computer (check with `git --version` in terminal)
- Your project files ready

## Step 1: Initialize Git Repository

1. Open Terminal (Mac) or Command Prompt (Windows)
2. Navigate to your project directory:
   ```bash
   cd "/Users/udoysaha/Desktop/Stock Simulator"
   ```

3. Initialize a git repository:
   ```bash
   git init
   ```

## Step 2: Create .gitignore File

A `.gitignore` file has already been created for you. It excludes:
- Virtual environment (`venv/`)
- Python cache files (`__pycache__/`)
- IDE files
- OS-specific files

## Step 3: Add and Commit Your Files

1. Check which files will be added:
   ```bash
   git status
   ```

2. Add all project files:
   ```bash
   git add .
   ```

3. Create your first commit:
   ```bash
   git commit -m "Initial commit: Stock Portfolio Simulator"
   ```

## Step 4: Create a GitHub Repository

1. Go to https://github.com and sign in
2. Click the **"+"** icon in the top right corner
3. Select **"New repository"**
4. Fill in the repository details:
   - **Repository name**: `stock-portfolio-simulator` (or any name you prefer)
   - **Description**: "Advanced stock portfolio analysis tool with backtesting, Monte Carlo simulation, and optimization"
   - **Visibility**: Choose **Public** (required for free Streamlit Cloud)
   - **DO NOT** initialize with README, .gitignore, or license (we already have these)
5. Click **"Create repository"**

## Step 5: Connect Local Repository to GitHub

After creating the repository, GitHub will show you commands. Use these:

1. Add the remote repository (replace `YOUR_USERNAME` with your GitHub username):
   ```bash
   git remote add origin https://github.com/YOUR_USERNAME/stock-portfolio-simulator.git
   ```

2. Rename your branch to `main` (if needed):
   ```bash
   git branch -M main
   ```

3. Push your code to GitHub:
   ```bash
   git push -u origin main
   ```

   You'll be prompted for your GitHub username and password. For password, use a **Personal Access Token** (see Step 6 if you need to create one).

## Step 6: Create GitHub Personal Access Token (if needed)

If GitHub asks for a password and your regular password doesn't work:

1. Go to GitHub → Settings → Developer settings → Personal access tokens → Tokens (classic)
2. Click **"Generate new token (classic)"**
3. Give it a name like "Streamlit Deployment"
4. Select scopes: Check **"repo"** (this gives full control of private repositories)
5. Click **"Generate token"**
6. **Copy the token immediately** (you won't see it again!)
7. Use this token as your password when pushing

## Step 7: Verify Your Code is on GitHub

1. Go to your repository on GitHub: `https://github.com/YOUR_USERNAME/stock-portfolio-simulator`
2. Verify you can see all your files:
   - `app.py`
   - `data_utils.py`
   - `backtest.py`
   - `monte_carlo.py`
   - `optimization.py`
   - `requirements.txt`
   - `README.md`

## Step 8: Deploy to Streamlit Community Cloud

1. Go to https://share.streamlit.io/
2. Sign in with your GitHub account
3. Click **"New app"**
4. Fill in the deployment details:
   - **Repository**: Select your repository (`YOUR_USERNAME/stock-portfolio-simulator`)
   - **Branch**: `main` (or `master` if that's your branch)
   - **Main file path**: `app.py`
   - **App URL**: Choose a custom URL or use the default
5. Click **"Deploy"**

## Step 9: Wait for Deployment

- Streamlit will install dependencies from `requirements.txt`
- This may take 2-5 minutes
- You'll see build logs in real-time
- Once complete, your app will be live!

## Step 10: Access Your Deployed App

After deployment, you'll get a URL like:
```
https://YOUR-APP-NAME.streamlit.app
```

Share this URL with anyone to access your app!

## Troubleshooting

### Issue: "Module not found" errors
- **Solution**: Make sure all dependencies are in `requirements.txt`
- Check that you're using the correct Python package names

### Issue: "Failed to download data"
- **Solution**: This is normal - the app needs internet access to fetch stock data
- Make sure yfinance is in requirements.txt

### Issue: Git push fails
- **Solution**: Use a Personal Access Token instead of password
- Make sure you've added the remote repository correctly

### Issue: Deployment fails
- **Solution**: Check the build logs in Streamlit Cloud
- Verify `app.py` is the correct main file
- Ensure all imports are correct

## Updating Your App

After making changes to your code:

1. Stage your changes:
   ```bash
   git add .
   ```

2. Commit your changes:
   ```bash
   git commit -m "Description of your changes"
   ```

3. Push to GitHub:
   ```bash
   git push
   ```

4. Streamlit Cloud will automatically redeploy your app!

## Quick Command Reference

```bash
# Navigate to project
cd "/Users/udoysaha/Desktop/Stock Simulator"

# Check status
git status

# Add files
git add .

# Commit
git commit -m "Your commit message"

# Push to GitHub
git push

# View remote
git remote -v
```

## Need Help?

- Streamlit Community Cloud Docs: https://docs.streamlit.io/streamlit-community-cloud
- GitHub Docs: https://docs.github.com
- Streamlit Forums: https://discuss.streamlit.io

Good luck with your deployment! 🚀


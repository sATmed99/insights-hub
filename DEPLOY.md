# Deployment Guide

This project can be deployed to multiple platforms. Follow the instructions below for your preferred hosting service.

## 🚀 Quick Deployment Options

### 1. **Streamlit Cloud** (Recommended for Streamlit apps)

The easiest way to deploy your Streamlit app:

1. Push your code to GitHub
2. Go to [streamlit.io/cloud](https://streamlit.io/cloud)
3. Click "New app"
4. Connect your GitHub repository
5. Select the main branch and `main.py` as the entrypoint
6. Deploy!

No configuration needed. Streamlit Cloud handles everything.

---

### 2. **Vercel**

For serverless deployment:

1. Install Vercel CLI:
   ```bash
   npm i -g vercel
   ```

2. Deploy:
   ```bash
   vercel
   ```

3. Follow the prompts to connect your GitHub account and configure the project

4. Set environment variables in Vercel dashboard if needed

**Note**: Vercel has Python 3.11 support. The `vercel.json` is pre-configured.

---

### 3. **Netlify**

For serverless deployment with Functions:

1. Install Netlify CLI:
   ```bash
   npm install -g netlify-cli
   ```

2. Connect your repository:
   ```bash
   netlify connect
   ```

3. Deploy:
   ```bash
   netlify deploy --prod
   ```

**Note**: `netlify.toml` is pre-configured for automatic deployments from pushes to your main branch.

---

### 4. **GitHub Pages** 

For static hosting:

1. The GitHub Actions workflow `.github/workflows/deploy.yml` is already configured
2. Push to `main` or `master` branch
3. GitHub Actions will automatically:
   - Install dependencies
   - Build the project
   - Deploy to GitHub Pages

4. Enable GitHub Pages in your repository settings:
   - Settings → Pages → Source: "Deploy from a branch" → `gh-pages` branch

**Note**: GitHub Pages works best for static content. For dynamic Streamlit apps, use Streamlit Cloud instead.

---

### 5. **Heroku** (Alternative)

If you prefer traditional app hosting:

1. Install Heroku CLI
2. Create Heroku app:
   ```bash
   heroku create your-app-name
   ```

3. Deploy:
   ```bash
   git push heroku main
   ```

Files included:
- `Procfile`: Startup configuration
- `runtime.txt`: Python version

---

## 🔧 Environment Variables

Create a `.env` file for local development (not committed to git):

```
DATABASE_URL=your_db_url
API_KEY=your_api_key
```

For production deployment, set these in your platform's dashboard:
- **Vercel**: Settings → Environment Variables
- **Netlify**: Site settings → Build & Deploy → Environment
- **Streamlit Cloud**: App secrets (icon in top right)

---

## 📝 Pre-deployment Checklist

- [ ] Update `requirements.txt` with all dependencies
- [ ] Test locally: `streamlit run main.py`
- [ ] Update `.streamlit/config.toml` with your branding
- [ ] Add `.env` to `.gitignore` (sensitive data)
- [ ] Commit and push to GitHub
- [ ] Choose your deployment platform above

---

## 🆘 Troubleshooting

### Streamlit Cloud
- **Issue**: App doesn't start
  - Check `requirements.txt` is correct
  - View logs in Streamlit Cloud dashboard

### Vercel
- **Issue**: Python dependencies not installing
  - Ensure `vercel.json` runtime is correct
  - Check `requirements.txt` format

### Netlify
- **Issue**: Streamlit server not responding
  - Increase timeout in deploy settings
  - Check build logs in Netlify dashboard

### GitHub Pages
- **Issue**: Deployment fails
  - Verify `gh-pages` branch exists
  - Check GitHub Actions workflow in Actions tab
  - Ensure repository is public (for free Pages)

---

## 📚 Resources

- [Streamlit Cloud Docs](https://docs.streamlit.io/streamlit-cloud)
- [Vercel Deployment Docs](https://vercel.com/docs/concepts/deployments/overview)
- [Netlify Deployment Docs](https://docs.netlify.com/)
- [GitHub Pages Docs](https://docs.github.com/en/pages)

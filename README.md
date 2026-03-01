# Gym Progress Dashboard
## Live Dashboard for Your Training Data

This repository hosts a live dashboard of your gym training progress, automatically updated via GitHub Actions.

## 🎯 **Features**

- **Live Dashboard:** View at `https://shoegrabber.github.io/gym-dashboard/`
- **Auto-Update:** New data automatically updates the dashboard
- **Private Data:** Your actual numbers stay private (sample data public)
- **Progress Tracking:** Visualize strength gains over time

## 🔄 **How It Works**

### **Data Flow:**
```
Your Phone → Export JSON → Push to GitHub → GitHub Actions → Update Dashboard
```

### **Weekly Workflow:**
1. Export data from Gym Log app
2. Run local script to prepare data
3. Push to GitHub
4. Dashboard auto-updates within minutes

## 📁 **Repository Structure**

```
gym-dashboard/
├── index.html              # Main dashboard page
├── data/                   # Training data (private branch)
│   └── latest.json         # Latest export
├── scripts/                # Data processing scripts
│   └── process_data.py     # Converts export to dashboard format
├── .github/workflows/      # GitHub Actions
│   └── update-dashboard.yml # Auto-update workflow
└── assets/                 # Images, styles, etc.
```

## 🚀 **Quick Start**

### **1. Create the GitHub Repository:**
```bash
# Create new repo on GitHub named "gym-dashboard"
# Enable GitHub Pages (Settings → Pages → Source: gh-pages branch)
```

### **2. Set Up Locally:**
```bash
cd ~/Juju/02_GYM_LOG/github_pages
git init
git remote add origin https://github.com/Shoegrabber/gym-dashboard.git
```

### **3. Export and Update:**
```bash
# After exporting from app:
./scripts/update_dashboard.sh
```

## 🔒 **Privacy Considerations**

### **Public Branch (`main`):**
- Dashboard HTML/CSS/JS
- Sample data (for demo)
- Processing scripts

### **Private Branch (`data`):**
- Your actual training data
- Personal notes
- Progress history

## 📱 **App Integration**

### **Option A: Manual Export (Simple)**
1. Export from app to phone storage
2. Run script to process and push

### **Option B: Auto-Export (Advanced)**
Modify app to:
1. Export to app-specific folder
2. Use GitHub API to push updates
3. Trigger dashboard rebuild

## 🛠️ **Development**

### **Local Testing:**
```bash
# Serve dashboard locally
python3 -m http.server 8000
# Open http://localhost:8000
```

### **Update Dashboard:**
```bash
./scripts/update_dashboard.sh
```

## 📊 **Dashboard Features**

- **Progress Charts:** Visualize strength gains
- **Session History:** View past workouts
- **Goal Tracking:** Monitor progress toward targets
- **Training Plan:** Current week's plan
- **Statistics:** Volume, frequency, consistency

## 🔮 **Future Enhancements**

1. **Wearable Integration:** Add heart rate, sleep data
2. **Food Tracking:** Connect with nutrition logs
3. **AI Insights:** Personalized recommendations
4. **Mobile App:** Progressive Web App version

---

**Status:** Ready for deployment
**Next Step:** Create GitHub repo and push this structure
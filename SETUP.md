# GitHub Pages Dashboard Setup Guide

## 🚀 **Complete Setup in 10 Minutes**

### **Step 1: Create GitHub Repository**
1. Go to https://github.com/new
2. Repository name: `gym-dashboard`
3. Description: "Live dashboard for gym training progress"
4. **DO NOT** initialize with README (we'll push existing files)
5. Click "Create repository"

### **Step 2: Initialize Local Repository**
```bash
cd ~/Juju/02_GYM_LOG/github_pages
git init
git add .
git commit -m "Initial dashboard setup"
git branch -M main
git remote add origin https://github.com/Shoegrabber/gym-dashboard.git
git push -u origin main
```

### **Step 3: Enable GitHub Pages**
1. Go to your repo: `https://github.com/Shoegrabber/gym-dashboard`
2. Click **Settings** → **Pages**
3. Under **Source**, select:
   - Branch: `main`
   - Folder: `/ (root)`
4. Click **Save**
5. Wait 1-2 minutes for deployment

### **Step 4: Test Your Dashboard**
Visit: `https://shoegrabber.github.io/gym-dashboard/`

---

## 🔄 **Weekly Update Workflow**

### **After Each Export:**
```bash
cd ~/Juju/02_GYM_LOG/github_pages/scripts
./update_dashboard.sh
```

### **Or Manual Update:**
```bash
cd ~/Juju/02_GYM_LOG/github_pages
python3 scripts/process_data.py
git add data/latest.json
git commit -m "Update dashboard data $(date +%Y-%m-%d)"
git push origin main
```

---

## 📱 **App Integration Options**

### **Option A: Manual Export (Recommended)**
1. Export from app to phone storage
2. Copy to computer via USB/cloud
3. Run update script

### **Option B: Auto-Export (Future Enhancement)**
Modify your Android app to:
1. Export to app-specific folder
2. Use GitHub API to push updates
3. Trigger dashboard rebuild

---

## 🔒 **Privacy Considerations**

### **Public Data:**
- Dashboard HTML/CSS/JS
- Sample data (for demo)
- Processing scripts

### **Private Data Options:**
1. **Keep data local** - Only push processed summaries
2. **Private repo** - Make entire repo private
3. **Separate data branch** - Keep raw data in private branch

### **Recommended:**
- Process data locally
- Push only dashboard-ready JSON
- Keep raw exports in your local `data_exports/` folder

---

## 🛠️ **Folder Structure**

```
gym-dashboard/
├── index.html              # Main dashboard
├── README.md               # Documentation
├── SETUP.md                # This file
├── scripts/                # Data processing
│   ├── process_data.py     # Converts export → dashboard format
│   └── update_dashboard.sh # Update script
├── data/                   # Dashboard data (auto-generated)
│   └── latest.json         # Current data
├── .github/workflows/      # GitHub Actions
│   └── update-dashboard.yml # Auto-deploy workflow
└── assets/                 # (Optional) Images, styles
```

---

## 🎯 **How It Works**

### **Data Flow:**
```
Phone App → JSON Export → Local Processing → GitHub → Dashboard
    ↓           ↓              ↓              ↓         ↓
  [Log] → [Raw Data] → [Dashboard Format] → [Push] → [Live Site]
```

### **Update Timeline:**
1. **Push to GitHub:** Instant
2. **GitHub Actions:** 1-2 minutes
3. **GitHub Pages:** 1-2 minutes
4. **Total:** ~3-5 minutes

---

## ⚠️ **Troubleshooting**

### **Dashboard not loading:**
- Check GitHub Pages is enabled
- Wait 5 minutes after first push
- Clear browser cache

### **Data not updating:**
- Check `data/latest.json` exists
- Verify GitHub Actions ran successfully
- Check for errors in update script

### **Git push errors:**
- Check internet connection
- Verify GitHub credentials
- Try `git pull` first

---

## 🔮 **Future Enhancements**

### **Phase 1 (Now):**
- Basic dashboard with sample data
- Manual update workflow

### **Phase 2 (Next Month):**
- Auto-export from app
- Progress charts
- Historical data view

### **Phase 3 (Future):**
- Wearable integration
- Food/sleep tracking
- AI recommendations

---

## 📞 **Support**

### **Quick Fixes:**
1. **Dashboard blank:** Check browser console for errors
2. **Data not showing:** Verify `data/latest.json` format
3. **Update failed:** Check GitHub Actions logs

### **Need Help?**
1. Check this SETUP.md file
2. Review GitHub Actions logs
3. Contact for assistance

---

## ✅ **Success Checklist**

- [ ] GitHub repo created: `gym-dashboard`
- [ ] Files pushed to GitHub
- [ ] GitHub Pages enabled
- [ ] Dashboard loads: `https://shoegrabber.github.io/gym-dashboard/`
- [ ] Test update workflow
- [ ] Bookmark dashboard URL

---

**🎉 Congratulations!** You now have a live dashboard for your training progress.

**Next:** Export data from your app and run the update script!
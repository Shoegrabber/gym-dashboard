#!/bin/bash
# Update Gym Dashboard Script
# Run this after exporting data from your app

set -e  # Exit on error

echo "========================================"
echo "UPDATE GYM DASHBOARD"
echo "========================================"
echo ""

# Check for export file
EXPORT_DIR="../../data_exports"
LATEST_EXPORT=$(ls -t "$EXPORT_DIR"/*.json 2>/dev/null | head -1)

if [ -z "$LATEST_EXPORT" ]; then
    echo "❌ No JSON exports found in $EXPORT_DIR/"
    echo ""
    echo "Please export data from your Gym Log app first:"
    echo "1. Open Gym Log app on your phone"
    echo "2. Go to Settings → Export"
    echo "3. Save the JSON file to: $EXPORT_DIR/"
    echo ""
    echo "Or copy it manually:"
    echo "cp /path/to/export.json $EXPORT_DIR/gym_export_$(date +%Y-%m-%d).json"
    exit 1
fi

echo "📊 Found export: $(basename "$LATEST_EXPORT")"
echo ""

# Process data
echo "🔄 Processing data..."
python3 process_data.py
echo ""

# Check if data was created
DATA_FILE="../data/latest.json"
if [ ! -f "$DATA_FILE" ]; then
    echo "❌ Failed to create dashboard data"
    exit 1
fi

echo "✅ Data processed successfully"
echo "   File: $DATA_FILE"
echo "   Size: $(du -h "$DATA_FILE" | cut -f1)"
echo ""

# Show preview
echo "📈 Data preview:"
echo "----------------"
head -20 "$DATA_FILE"
echo "..."
echo ""

# Git status
echo "🔍 Git status:"
echo "-------------"
git status --short
echo ""

# Instructions
echo "🚀 To publish updates:"
echo "====================="
echo ""
echo "1. Review changes:"
echo "   git diff"
echo ""
echo "2. Commit changes:"
echo "   git add data/latest.json"
echo "   git commit -m 'Update dashboard data $(date +%Y-%m-%d)'"
echo ""
echo "3. Push to GitHub:"
echo "   git push origin main"
echo ""
echo "4. Your dashboard will update at:"
echo "   https://shoegrabber.github.io/gym-dashboard/"
echo ""
echo "⏱️  It may take 1-2 minutes for GitHub Pages to update."
echo ""

echo "========================================"
echo "UPDATE READY"
echo "========================================"
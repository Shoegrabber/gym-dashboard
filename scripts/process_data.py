#!/usr/bin/env python3
"""
Process gym log data for GitHub Pages dashboard
Converts raw JSON export to dashboard-friendly format
"""

import json
import os
import sys
from datetime import datetime
from collections import defaultdict

def load_raw_data(export_path):
    """Load raw JSON export from gym log app"""
    with open(export_path, 'r') as f:
        return json.load(f)

def analyze_data(raw_data):
    """Analyze raw data and extract key metrics"""
    sessions = raw_data['tables']['sessions']
    session_exercises = raw_data['tables']['session_exercises']
    sets = raw_data['tables']['sets']
    
    # Count sessions by focus
    focus_counts = defaultdict(int)
    for session in sessions:
        focus_counts[session['focus']] += 1
    
    # Get recent weights for key exercises
    key_exercises = [
        'Smith machine Squat',
        'Leg press',
        'Lying leg curl',
        'Seated calf raise',
        'Incline dumbbell press',
        'Seated shoulder press machine',
        'Lat pulldown',
        'Seated cable row',
        'Face pull',
        'Dumbbell bicep curl'
    ]
    
    # Map exercise names to session_exercise_ids
    exercise_to_ids = defaultdict(list)
    for se in session_exercises:
        exercise_to_ids[se['exercise_name']].append(se['id'])
    
    exercise_data = []
    
    for exercise in key_exercises:
        if exercise in exercise_to_ids:
            ids = exercise_to_ids[exercise][-3:]  # Last 3 instances
            recent_weights = []
            
            for s in sets:
                if s['session_exercise_id'] in ids and s['weight']:
                    recent_weights.append(s['weight'])
            
            if recent_weights:
                current = max(recent_weights[-3:]) if recent_weights else 0
                # Set target as 10% above current
                target = round(current * 1.1)
                
                exercise_data.append({
                    'name': exercise,
                    'current': current,
                    'target': target,
                    'unit': 'kg'
                })
    
    return {
        'lastUpdated': datetime.now().isoformat(),
        'stats': {
            'totalSessions': len(sessions),
            'legsSessions': focus_counts.get('legs', 0),
            'pushSessions': focus_counts.get('push', 0),
            'pullSessions': focus_counts.get('pull', 0)
        },
        'exercises': exercise_data
    }

def save_dashboard_data(data, output_path):
    """Save processed data for dashboard"""
    with open(output_path, 'w') as f:
        json.dump(data, f, indent=2)
    
    print(f"✅ Dashboard data saved to: {output_path}")
    print(f"   Total sessions: {data['stats']['totalSessions']}")
    print(f"   Exercises tracked: {len(data['exercises'])}")

def main():
    # Paths
    script_dir = os.path.dirname(os.path.abspath(__file__))
    repo_root = os.path.join(script_dir, '..')
    
    # Look for latest export in data_exports folder
    exports_dir = os.path.join(repo_root, '..', 'data_exports')
    if not os.path.exists(exports_dir):
        print(f"❌ Exports directory not found: {exports_dir}")
        print("Please export data from your app first.")
        sys.exit(1)
    
    # Find latest JSON file
    json_files = [f for f in os.listdir(exports_dir) if f.endswith('.json')]
    if not json_files:
        print(f"❌ No JSON exports found in {exports_dir}")
        print("Please export data from your Gym Log app.")
        sys.exit(1)
    
    latest_export = sorted(json_files)[-1]
    export_path = os.path.join(exports_dir, latest_export)
    
    print(f"📊 Processing: {latest_export}")
    
    # Load and process data
    raw_data = load_raw_data(export_path)
    dashboard_data = analyze_data(raw_data)
    
    # Save to data folder
    data_dir = os.path.join(repo_root, 'data')
    os.makedirs(data_dir, exist_ok=True)
    
    output_path = os.path.join(data_dir, 'latest.json')
    save_dashboard_data(dashboard_data, output_path)
    
    # Also save a dated copy
    dated_path = os.path.join(data_dir, f"data_{datetime.now().strftime('%Y-%m-%d')}.json")
    save_dashboard_data(dashboard_data, dated_path)
    
    print("\n🎯 Next steps:")
    print("1. Commit and push the changes:")
    print("   git add data/latest.json")
    print("   git commit -m 'Update dashboard data'")
    print("   git push origin main")
    print("\n2. Your dashboard will auto-update at:")
    print("   https://shoegrabber.github.io/gym-dashboard/")

if __name__ == "__main__":
    main()
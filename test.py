#!/usr/bin/env python3
"""
Quick test script to verify all components work
"""

print("🧪 Testing JSONPlaceholder Analytics Components...\n")

# Test 1: Data Fetcher
print("1️⃣ Testing Data Fetcher...")
try:
    from data_fetcher import DataFetcher
    fetcher = DataFetcher()
    print("   ✅ DataFetcher imported successfully")
except Exception as e:
    print(f"   ❌ Error: {e}")

# Test 2: Analytics
print("\n2️⃣ Testing Analytics...")
try:
    from analytics import DataAnalytics
    
    # Mock data
    mock_users = [{'id': 1, 'name': 'Test User'}]
    mock_posts = [{'id': 1, 'userId': 1, 'title': 'Test Post'}]
    mock_comments = [{'postId': 1}]
    mock_todos = [{'userId': 1, 'completed': True}]
    
    analytics = DataAnalytics(mock_users, mock_posts, mock_comments, mock_todos)
    metrics = analytics.get_all_metrics()
    print("   ✅ Analytics working correctly")
    print(f"   📊 Sample metric: {metrics['avg_comments_per_post']} avg comments/post")
except Exception as e:
    print(f"   ❌ Error: {e}")

# Test 3: Requirements
print("\n3️⃣ Checking dependencies...")
dependencies = ['streamlit', 'plotly', 'pandas', 'requests']
for dep in dependencies:
    try:
        __import__(dep)
        print(f"   ✅ {dep} installed")
    except ImportError:
        print(f"   ⚠️  {dep} not installed - run: pip install {dep}")

print("\n" + "="*50)
print("🎉 All tests completed!")
print("="*50)
print("\n📝 Next steps:")
print("1. Run: streamlit run app.py")
print("2. Open browser at http://localhost:8501")
print("3. Push to GitHub and deploy to Streamlit Cloud")

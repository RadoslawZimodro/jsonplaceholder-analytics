"""
Main Streamlit application for JSONPlaceholder Analytics
"""
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
from data_fetcher import DataFetcher
from analytics import DataAnalytics


# Page configuration
st.set_page_config(
    page_title="JSONPlaceholder Analytics",
    page_icon="📊",
    layout="wide"
)

# Title and description
st.title("📊 JSONPlaceholder Data Analytics")
st.markdown("""
Dashboard analyzing data from [JSONPlaceholder API](https://jsonplaceholder.typicode.com).
This app fetches data about users, posts, comments, and todos, then calculates and visualizes key metrics.
""")

# Sidebar
st.sidebar.header("About")
st.sidebar.info("""
**Data Sources:**
- Users
- Posts
- Comments
- TODOs

**Metrics Calculated:**
- Posts per user
- Average comments per post
- TODOs completion rate
- Top commented posts
""")


@st.cache_data(ttl=3600)
def load_data():
    """Load data from API with caching"""
    with st.spinner("Fetching data from API..."):
        fetcher = DataFetcher()
        data = fetcher.fetch_all()
    return data


# Load data
data = load_data()

# Check if data loaded successfully
if not data['users'] or not data['posts']:
    st.error("Failed to load data from API. Please check your internet connection and try again.")
    st.stop()

# Create analytics instance
analytics = DataAnalytics(
    users=data['users'],
    posts=data['posts'],
    comments=data['comments'],
    todos=data['todos']
)

# Get all metrics
metrics = analytics.get_all_metrics()

# Display key metrics in columns
st.header("📈 Key Metrics")
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Total Users", len(data['users']))

with col2:
    st.metric("Total Posts", len(data['posts']))

with col3:
    st.metric("Total Comments", len(data['comments']))

with col4:
    st.metric("Avg Comments/Post", metrics['avg_comments_per_post'])

st.divider()

# Visualization 1: Posts per User (Bar Chart)
st.header("📊 User Activity - Posts per User")
st.markdown("Shows how many posts each user has created.")

posts_data = metrics['posts_per_user']
df_posts = pd.DataFrame(list(posts_data.items()), columns=['User', 'Posts'])
df_posts = df_posts.sort_values('Posts', ascending=False)

fig_posts = px.bar(
    df_posts,
    x='User',
    y='Posts',
    title='Number of Posts per User',
    labels={'Posts': 'Number of Posts', 'User': 'User Name'},
    color='Posts',
    color_continuous_scale='Blues'
)
fig_posts.update_layout(
    xaxis_tickangle=-45,
    height=500,
    showlegend=False
)
st.plotly_chart(fig_posts, use_container_width=True)

st.divider()

# Visualization 2: TODOs Completion Rate (Pie Chart)
st.header("✅ TODOs Completion Rate")
st.markdown("Shows the percentage of completed vs incomplete tasks.")

col1, col2 = st.columns([2, 1])

with col1:
    todos_data = metrics['todos_completion']
    fig_todos = go.Figure(data=[go.Pie(
        labels=['Completed', 'Incomplete'],
        values=[todos_data['completed'], todos_data['incomplete']],
        hole=0.4,
        marker_colors=['#2ecc71', '#e74c3c']
    )])
    fig_todos.update_layout(
        title='TODOs Completion Status',
        height=400
    )
    st.plotly_chart(fig_todos, use_container_width=True)

with col2:
    st.metric(
        "Completion Rate",
        f"{todos_data['completed']}%",
        delta=f"{todos_data['completed'] - 50:.1f}% vs 50%"
    )
    st.markdown(f"""
    **Statistics:**
    - ✅ Completed: {todos_data['completed']}%
    - ⏳ Incomplete: {todos_data['incomplete']}%
    - 📋 Total TODOs: {len(data['todos'])}
    """)

st.divider()

# Visualization 3: Top Commented Posts (Horizontal Bar)
st.header("💬 Top 5 Most Commented Posts")
st.markdown("Posts that received the most comments from users.")

top_posts = metrics['top_commented_posts']
df_top = pd.DataFrame(top_posts, columns=['Post Title', 'Comments'])

fig_top = px.bar(
    df_top,
    x='Comments',
    y='Post Title',
    orientation='h',
    title='Top 5 Most Commented Posts',
    labels={'Comments': 'Number of Comments', 'Post Title': ''},
    color='Comments',
    color_continuous_scale='Viridis'
)
fig_top.update_layout(
    height=400,
    yaxis={'categoryorder': 'total ascending'},
    showlegend=False
)
st.plotly_chart(fig_top, use_container_width=True)

st.divider()

# Additional: User Activity Summary Table
st.header("👥 User Activity Summary")
st.markdown("Detailed breakdown of each user's activity.")

user_activity = metrics['user_activity']
df_activity = pd.DataFrame(user_activity)
df_activity['completion_rate'] = (
    df_activity['completed_todos'] / df_activity['todos'] * 100
).round(1)
df_activity = df_activity.rename(columns={
    'name': 'User Name',
    'posts': 'Posts',
    'todos': 'Total TODOs',
    'completed_todos': 'Completed TODOs',
    'completion_rate': 'Completion Rate (%)'
})

st.dataframe(
    df_activity,
    hide_index=True,
    use_container_width=True,
    column_config={
        "Completion Rate (%)": st.column_config.ProgressColumn(
            "Completion Rate (%)",
            format="%.1f%%",
            min_value=0,
            max_value=100,
        )
    }
)

# Footer
st.divider()
st.markdown("""
---
**Data Source:** [JSONPlaceholder](https://jsonplaceholder.typicode.com) - Free fake REST API for testing and prototyping  
**Created with:** Python, Streamlit, Plotly  
""")

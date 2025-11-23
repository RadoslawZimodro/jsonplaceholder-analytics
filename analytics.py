"""
Module for analyzing data and calculating statistics
"""
from typing import Dict, List, Tuple
from collections import Counter, defaultdict


class DataAnalytics:
    """Class for analyzing JSONPlaceholder data"""
    
    def __init__(self, users: List[Dict], posts: List[Dict], 
                 comments: List[Dict], todos: List[Dict]):
        self.users = users
        self.posts = posts
        self.comments = comments
        self.todos = todos
    
    def posts_per_user(self) -> Dict[str, int]:
        """
        Calculate number of posts per user
        Returns: Dict with user names as keys and post counts as values
        """
        # Create user ID to name mapping
        user_names = {user['id']: user['name'] for user in self.users}
        
        # Count posts per user ID
        post_counts = Counter(post['userId'] for post in self.posts)
        
        # Convert to user names
        return {user_names.get(user_id, f"User {user_id}"): count 
                for user_id, count in post_counts.items()}
    
    def average_comments_per_post(self) -> float:
        """
        Calculate average number of comments per post
        Returns: Average as float
        """
        if not self.posts:
            return 0.0
        
        # Count comments per post
        comments_count = Counter(comment['postId'] for comment in self.comments)
        
        # Calculate average
        total_comments = sum(comments_count.values())
        return total_comments / len(self.posts)
    
    def todos_completion_rate(self) -> Dict[str, float]:
        """
        Calculate percentage of completed TODOs
        Returns: Dict with 'completed' and 'incomplete' percentages
        """
        if not self.todos:
            return {'completed': 0.0, 'incomplete': 0.0}
        
        completed = sum(1 for todo in self.todos if todo['completed'])
        total = len(self.todos)
        
        completed_pct = (completed / total) * 100
        incomplete_pct = 100 - completed_pct
        
        return {
            'completed': round(completed_pct, 2),
            'incomplete': round(incomplete_pct, 2)
        }
    
    def top_commented_posts(self, n: int = 5) -> List[Tuple[str, int]]:
        """
        Get top N most commented posts
        Args:
            n: Number of top posts to return
        Returns: List of tuples (post_title, comment_count)
        """
        # Count comments per post
        comments_count = Counter(comment['postId'] for comment in self.comments)
        
        # Create post ID to title mapping
        post_titles = {post['id']: post['title'] for post in self.posts}
        
        # Get top N
        top_posts = comments_count.most_common(n)
        
        return [(post_titles.get(post_id, f"Post {post_id}"), count) 
                for post_id, count in top_posts]
    
    def user_activity_summary(self) -> List[Dict]:
        """
        Get comprehensive activity summary per user
        Returns: List of dicts with user activity data
        """
        user_names = {user['id']: user['name'] for user in self.users}
        
        # Count posts per user
        posts_per_user = Counter(post['userId'] for post in self.posts)
        
        # Count todos per user
        todos_per_user = Counter(todo['userId'] for todo in self.todos)
        
        # Count completed todos per user
        completed_todos = Counter(todo['userId'] for todo in self.todos 
                                 if todo['completed'])
        
        # Combine data
        summary = []
        for user_id in user_names.keys():
            summary.append({
                'name': user_names[user_id],
                'posts': posts_per_user.get(user_id, 0),
                'todos': todos_per_user.get(user_id, 0),
                'completed_todos': completed_todos.get(user_id, 0),
            })
        
        return summary
    
    def get_all_metrics(self) -> Dict:
        """
        Get all metrics at once
        Returns: Dict with all calculated metrics
        """
        return {
            'posts_per_user': self.posts_per_user(),
            'avg_comments_per_post': round(self.average_comments_per_post(), 2),
            'todos_completion': self.todos_completion_rate(),
            'top_commented_posts': self.top_commented_posts(5),
            'user_activity': self.user_activity_summary()
        }


# Test function
if __name__ == "__main__":
    # Mock data for testing
    mock_users = [
        {'id': 1, 'name': 'Jan Kowalski'},
        {'id': 2, 'name': 'Anna Nowak'}
    ]
    
    mock_posts = [
        {'id': 1, 'userId': 1, 'title': 'Post 1'},
        {'id': 2, 'userId': 1, 'title': 'Post 2'},
        {'id': 3, 'userId': 2, 'title': 'Post 3'}
    ]
    
    mock_comments = [
        {'postId': 1}, {'postId': 1}, {'postId': 1},
        {'postId': 2}, {'postId': 2},
        {'postId': 3}
    ]
    
    mock_todos = [
        {'userId': 1, 'completed': True},
        {'userId': 1, 'completed': False},
        {'userId': 2, 'completed': True},
        {'userId': 2, 'completed': True}
    ]
    
    analytics = DataAnalytics(mock_users, mock_posts, mock_comments, mock_todos)
    metrics = analytics.get_all_metrics()
    
    print("📊 Test Results:")
    print(f"Posts per user: {metrics['posts_per_user']}")
    print(f"Avg comments per post: {metrics['avg_comments_per_post']}")
    print(f"TODOs completion: {metrics['todos_completion']}")
    print(f"Top commented: {metrics['top_commented_posts']}")

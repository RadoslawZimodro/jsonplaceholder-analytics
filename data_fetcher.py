"""
Module for fetching data from JSONPlaceholder API
"""
import requests
from typing import Dict, List, Optional


class DataFetcher:
    """Class for fetching data from JSONPlaceholder API"""
    
    BASE_URL = "https://jsonplaceholder.typicode.com"
    
    def __init__(self):
        self.users = None
        self.posts = None
        self.comments = None
        self.todos = None
    
    def fetch_users(self) -> List[Dict]:
        """Fetch all users from API"""
        try:
            response = requests.get(f"{self.BASE_URL}/users")
            response.raise_for_status()
            self.users = response.json()
            return self.users
        except requests.exceptions.RequestException as e:
            print(f"Error fetching users: {e}")
            return []
    
    def fetch_posts(self) -> List[Dict]:
        """Fetch all posts from API"""
        try:
            response = requests.get(f"{self.BASE_URL}/posts")
            response.raise_for_status()
            self.posts = response.json()
            return self.posts
        except requests.exceptions.RequestException as e:
            print(f"Error fetching posts: {e}")
            return []
    
    def fetch_comments(self) -> List[Dict]:
        """Fetch all comments from API"""
        try:
            response = requests.get(f"{self.BASE_URL}/comments")
            response.raise_for_status()
            self.comments = response.json()
            return self.comments
        except requests.exceptions.RequestException as e:
            print(f"Error fetching comments: {e}")
            return []
    
    def fetch_todos(self) -> List[Dict]:
        """Fetch all todos from API"""
        try:
            response = requests.get(f"{self.BASE_URL}/todos")
            response.raise_for_status()
            self.todos = response.json()
            return self.todos
        except requests.exceptions.RequestException as e:
            print(f"Error fetching todos: {e}")
            return []
    
    def fetch_all(self) -> Dict[str, List[Dict]]:
        """Fetch all data at once"""
        return {
            'users': self.fetch_users(),
            'posts': self.fetch_posts(),
            'comments': self.fetch_comments(),
            'todos': self.fetch_todos()
        }


# Simple test function
if __name__ == "__main__":
    fetcher = DataFetcher()
    data = fetcher.fetch_all()
    
    print(f"Users fetched: {len(data['users'])}")
    print(f"Posts fetched: {len(data['posts'])}")
    print(f"Comments fetched: {len(data['comments'])}")
    print(f"Todos fetched: {len(data['todos'])}")
    
    # Show example data
    if data['users']:
        print(f"\nExample user: {data['users'][0]['name']}")
    if data['posts']:
        print(f"Example post title: {data['posts'][0]['title']}")

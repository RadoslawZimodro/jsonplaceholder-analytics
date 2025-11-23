# 📐 Architektura projektu - Diagram

```
┌─────────────────────────────────────────────────────────────────┐
│                  JSONPlaceholder Analytics                       │
│                     Streamlit Dashboard                          │
└─────────────────────────────────────────────────────────────────┘
                              │
                              │
                              ▼
                    ┌─────────────────┐
                    │     app.py      │ ◄─── Główna aplikacja
                    │   (Streamlit)   │      - UI/UX
                    └─────────────────┘      - Layout
                          │   │              - Wykresy
                          │   │
         ┌────────────────┘   └────────────────┐
         │                                      │
         ▼                                      ▼
┌──────────────────┐                 ┌──────────────────┐
│ data_fetcher.py  │                 │  analytics.py    │
│   (API Client)   │                 │   (Analytics)    │
└──────────────────┘                 └──────────────────┘
         │                                      │
         │ Requests                             │ Pandas
         ▼                                      ▼
┌──────────────────┐                 ┌──────────────────┐
│ JSONPlaceholder  │────────────────▶│  Przetworzone    │
│      API         │    Raw JSON     │      dane        │
│                  │                 │                  │
│  /users          │                 │ • Metryki        │
│  /posts          │                 │ • Agregacje      │
│  /comments       │                 │ • Rankingi       │
│  /todos          │                 │                  │
└──────────────────┘                 └──────────────────┘
                                              │
                                              │ DataFrames
                                              ▼
                                     ┌──────────────────┐
                                     │   Plotly Charts  │
                                     │                  │
                                     │ • Bar chart      │
                                     │ • Pie chart      │
                                     │ • Horizontal bar │
                                     └──────────────────┘
```

## 🔄 Przepływ danych

```
1. USER访问 Streamlit App
           ↓
2. app.py wywołuje DataFetcher
           ↓
3. DataFetcher pobiera z API:
   - GET /users
   - GET /posts  
   - GET /comments
   - GET /todos
           ↓
4. Raw JSON trafia do DataAnalytics
           ↓
5. DataAnalytics oblicza:
   - posts_per_user()
   - average_comments_per_post()
   - todos_completion_rate()
   - top_commented_posts()
           ↓
6. app.py wizualizuje z Plotly:
   - px.bar() → Posts per User
   - go.Pie() → TODOs Completion
   - px.bar(orientation='h') → Top Posts
           ↓
7. USER widzi interaktywny dashboard! 🎉
```

## 📦 Moduły i odpowiedzialności

```
┌────────────────────────────────────────────────────────┐
│ app.py                                                  │
│ ─────────────────────────────────────────────────────  │
│ Odpowiedzialność:                                       │
│ • UI/UX layout                                          │
│ • Integracja modułów                                    │
│ • Renderowanie wykresów                                 │
│ • State management                                      │
│ • Caching (@st.cache_data)                             │
└────────────────────────────────────────────────────────┘

┌────────────────────────────────────────────────────────┐
│ data_fetcher.py                                         │
│ ─────────────────────────────────────────────────────  │
│ Odpowiedzialność:                                       │
│ • Komunikacja z API                                     │
│ • Error handling                                        │
│ • Data validation                                       │
│ • Retry logic (future)                                  │
└────────────────────────────────────────────────────────┘

┌────────────────────────────────────────────────────────┐
│ analytics.py                                            │
│ ─────────────────────────────────────────────────────  │
│ Odpowiedzialność:                                       │
│ • Business logic                                        │
│ • Agregacje danych                                      │
│ • Kalkulacje metryk                                     │
│ • Data transformation                                   │
└────────────────────────────────────────────────────────┘
```

## 🎨 Stack technologiczny

```
┌─────────────────┐
│   Frontend      │
│   (Browser)     │
│                 │
│  • Plotly.js    │ ◄─── Interactive charts
│  • Streamlit UI │ ◄─── Web framework
└─────────────────┘
         │
         │ HTTP
         ▼
┌─────────────────┐
│    Backend      │
│   (Python)      │
│                 │
│  • Streamlit    │ ◄─── Server
│  • Pandas       │ ◄─── Data manipulation
│  • Requests     │ ◄─── HTTP client
└─────────────────┘
         │
         │ REST API
         ▼
┌─────────────────┐
│   External      │
│   API Service   │
│                 │
│  JSONPlaceholder│ ◄─── Fake REST API
└─────────────────┘
```

## 📊 Data Model

```
Users (10)
├── id: int
├── name: string
├── username: string
└── email: string

Posts (100)
├── id: int
├── userId: int ──┐
├── title: string │
└── body: string  │
                   │
Comments (500)     │
├── id: int        │
├── postId: int ───┤
├── name: string   │
└── email: string  │
                   │
TODOs (200)        │
├── id: int        │
├── userId: int ───┘
├── title: string
└── completed: bool

Relacje:
- User 1:N Posts (jeden user ma wiele postów)
- Post 1:N Comments (jeden post ma wiele komentarzy)
- User 1:N TODOs (jeden user ma wiele zadań)
```

## 🔌 API Endpoints

```
https://jsonplaceholder.typicode.com
│
├── /users       → GET all users (10)
├── /posts       → GET all posts (100)
├── /comments    → GET all comments (500)
└── /todos       → GET all todos (200)

Response format: JSON Array
Example:
[
  { "id": 1, "name": "...", ... },
  { "id": 2, "name": "...", ... },
  ...
]
```

## 🎯 Metryki kalkulowane

```
1. Posts per User
   Formula: COUNT(posts) GROUP BY userId
   Output: Dict[username, count]

2. Avg Comments per Post
   Formula: SUM(comments) / COUNT(posts)
   Output: float

3. TODOs Completion Rate
   Formula: (completed_todos / total_todos) * 100
   Output: Dict[completed%, incomplete%]

4. Top Commented Posts
   Formula: COUNT(comments) GROUP BY postId ORDER BY count DESC LIMIT 5
   Output: List[Tuple[title, count]]
```

## 📈 Wykresy

```
Chart 1: Bar Chart (Vertical)
├── Type: px.bar
├── X-axis: User names
├── Y-axis: Number of posts
└── Color: Gradient (Blues)

Chart 2: Pie Chart (Donut)
├── Type: go.Pie
├── Values: [completed%, incomplete%]
├── Colors: [green, red]
└── Hole: 0.4 (donut effect)

Chart 3: Bar Chart (Horizontal)
├── Type: px.bar(orientation='h')
├── X-axis: Number of comments
├── Y-axis: Post titles (top 5)
└── Color: Gradient (Viridis)
```

## 🚀 Deployment Flow

```
Local Development
       │
       │ git push
       ▼
GitHub Repository
       │
       │ webhook
       ▼
Streamlit Cloud
       │
       │ build & deploy
       ▼
Live App (24/7)
       │
       │ public URL
       ▼
Users can access! 🎉
```

---

**Diagram pokazuje pełną architekturę aplikacji od API do użytkownika!** 📐

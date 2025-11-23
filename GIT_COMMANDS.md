# Git Commands - Krok po kroku

## 1. Inicjalizacja repozytorium

```bash
# W folderze z projektem
git init
git add .
git commit -m "Initial commit: JSONPlaceholder Analytics Dashboard"
```

## 2. Stwórz repozytorium na GitHub

1. Idź na https://github.com/new
2. Nazwa: `jsonplaceholder-analytics`
3. Opis: `Mini data analytics app with JSONPlaceholder API`
4. **Publiczne** (ważne!)
5. **NIE** zaznaczaj "Add README" (już masz)
6. Kliknij "Create repository"

## 3. Połącz lokalne repo z GitHub

```bash
# Zastąp YOUR_USERNAME swoją nazwą użytkownika GitHub
git remote add origin https://github.com/YOUR_USERNAME/jsonplaceholder-analytics.git
git branch -M main
git push -u origin main
```

## 4. Jeśli coś zmienisz później

```bash
git add .
git commit -m "Opisz co zmieniłeś"
git push
```

## 5. Deploy na Streamlit Cloud

1. Idź na https://streamlit.io/cloud
2. Sign in with GitHub
3. New app
4. Repository: `YOUR_USERNAME/jsonplaceholder-analytics`
5. Branch: `main`
6. Main file: `app.py`
7. Deploy!

## Przykładowy link do repo:
https://github.com/YOUR_USERNAME/jsonplaceholder-analytics

## Przykładowy link do demo:
https://your-app-name.streamlit.app

---

## Troubleshooting

### Problem: git push pyta o hasło
**Rozwiązanie:** Użyj Personal Access Token zamiast hasła
1. GitHub → Settings → Developer settings → Personal access tokens → Generate new token
2. Zaznacz `repo` scope
3. Skopiuj token
4. Użyj jako hasło przy `git push`

### Problem: Authentication failed
**Rozwiązanie:** Skonfiguruj SSH albo użyj GitHub CLI
```bash
# Opcja 1: GitHub CLI (najłatwiejsza)
gh auth login

# Opcja 2: HTTPS z tokenem (jak wyżej)
```

---

**Tip:** Możesz edytować README bezpośrednio na GitHubie (przycisk ✏️) jeśli potrzebujesz szybkiej poprawki!

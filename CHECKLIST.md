# ✅ Checklist przed wysłaniem zadania

## Wymagania z zadania (100 pkt)

### ✅ Poprawne pobranie i przetworzenie danych (30 pkt)
- [x] Pobieranie z minimum 2 endpointów (mamy 4!)
  - [x] /users
  - [x] /posts
  - [x] /comments
  - [x] /todos
- [x] Obsługa błędów przy pobieraniu
- [x] Przetwarzanie danych (class DataAnalytics)

### ✅ Działające wizualizacje (30 pkt)
- [x] Minimum 2 wykresy (mamy 3!)
  - [x] Słupkowy - aktywność użytkowników
  - [x] Kołowy - procent wykonanych TODOs
  - [x] Poziomy - top 5 postów (bonus!)
- [x] Interaktywne wykresy (Plotly)
- [x] Czytelne opisy i legendy

### ✅ Czysty kod + struktura projektu (20 pkt)
- [x] Podział na moduły (app.py, data_fetcher.py, analytics.py)
- [x] Docstrings dla funkcji
- [x] Type hints
- [x] Znaczące nazwy zmiennych
- [x] PEP 8 formatting
- [x] .gitignore

### ✅ README + działające demo (10 pkt)
- [x] README.md z:
  - [x] Krótkim opisem projektu
  - [x] Miejsce na zrzut ekranu (do dodania)
  - [x] Instrukcją uruchomienia
  - [x] Strukturą projektu
- [ ] Link do repozytorium GitHub (do stworzenia)
- [ ] Link do działającego demo (do deployment)

### ✅ Jawne użycie ChatGPT/Claude (10 pkt)
- [x] Sekcja w README "Wykorzystanie AI"
- [x] Przykładowe prompty
- [x] Opis jak AI pomógł
- [x] Szczere podejście - co AI zrobił, czego nie

## 📋 Minimum 3 metryki (mamy 4!)
- [x] Liczba postów na użytkownika
- [x] Średnia liczba komentarzy na post
- [x] Procent wykonanych TODOs
- [x] Top 5 najbardziej komentowanych postów

## 🎯 Do zrobienia przed wysłaniem

### GitHub:
1. [ ] Stwórz publiczne repozytorium na GitHub
2. [ ] Push kod (użyj GIT_COMMANDS.md)
3. [ ] Sprawdź czy README wyświetla się poprawnie
4. [ ] Dodaj screenshot (opcjonalnie)

### Deployment:
1. [ ] Deploy na Streamlit Cloud
2. [ ] Sprawdź czy app działa na produkcji
3. [ ] Przetestuj wszystkie funkcje
4. [ ] Skopiuj link do demo

### Finalizacja:
1. [ ] Zaktualizuj README z prawdziwymi linkami
2. [ ] Sprawdź wszystkie wymagania jeszcze raz
3. [ ] Wyślij linki rekruterowi:
   - Link do repo: `_____________________`
   - Link do demo: `_____________________`

## 🧪 Testy przed wysłaniem

```bash
# Test 1: Czy kod się uruchamia?
python test.py

# Test 2: Czy app działa?
streamlit run app.py
# Sprawdź w przeglądarce http://localhost:8501

# Test 3: Czy wszystkie pliki są w repo?
git status
```

## 📝 Co wysłać rekruterowi

**Format email:**

```
Temat: Zadanie rekrutacyjne - Mini-analityka danych z API

Cześć,

Wysyłam rozwiązanie zadania rekrutacyjnego:

🔗 Repozytorium GitHub: https://github.com/YOUR_USERNAME/jsonplaceholder-analytics
🌐 Działające demo: https://your-app.streamlit.app

Projekt zawiera:
- 4 endpointy API (users, posts, comments, todos)
- 4 metryki analityczne
- 3 interaktywne wykresy (Plotly)
- Deployment na Streamlit Cloud
- Szczegółowy opis użycia AI w README

Pozdrawiam,
[Twoje Imię]
```

## 🎉 Gotowe!

Gdy wszystko zaznaczone - możesz wysyłać! 💪

---

**Powodzenia!** 🚀

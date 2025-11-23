# 🚀 Quick Start Guide

## Lokalne uruchomienie (5 minut)

### 1. Sklonuj kod
```bash
# Utwórz folder projektu
mkdir jsonplaceholder-analytics
cd jsonplaceholder-analytics

# Pobierz pliki (lub skopiuj ręcznie)
```

### 2. Zainstaluj zależności
```bash
pip install -r requirements.txt
```

### 3. Uruchom aplikację
```bash
streamlit run app.py
```

### 4. Otwórz w przeglądarce
Aplikacja automatycznie otworzy się pod adresem: `http://localhost:8501`

---

## Deployment na Streamlit Cloud (10 minut)

### 1. Stwórz repozytorium GitHub
```bash
git init
git add .
git commit -m "Initial commit: JSONPlaceholder Analytics"
git remote add origin https://github.com/TWOJ_USERNAME/jsonplaceholder-analytics.git
git push -u origin main
```

### 2. Wejdź na Streamlit Cloud
1. Idź na https://streamlit.io/cloud
2. Zaloguj się przez GitHub
3. Kliknij "New app"

### 3. Skonfiguruj deployment
- **Repository:** `TWOJ_USERNAME/jsonplaceholder-analytics`
- **Branch:** `main`
- **Main file path:** `app.py`

### 4. Deploy!
Kliknij "Deploy!" i poczekaj ~2 minuty. Gotowe! 🎉

---

## Testowanie

Przed wysłaniem sprawdź czy wszystko działa:

```bash
# Uruchom testy
python test.py

# Sprawdź czy app się uruchamia
streamlit run app.py
```

---

## Troubleshooting

### Problem: ModuleNotFoundError
**Rozwiązanie:** Zainstaluj brakujące pakiety
```bash
pip install -r requirements.txt
```

### Problem: API nie odpowiada
**Rozwiązanie:** Sprawdź połączenie internetowe. API jest publiczne i nie wymaga klucza.

### Problem: Streamlit Cloud deployment fails
**Rozwiązanie:** 
1. Sprawdź czy `requirements.txt` jest w repozytorium
2. Upewnij się że `app.py` jest w głównym katalogu
3. Sprawdź logi w Streamlit Cloud

---

## Co dalej?

### Możliwe rozszerzenia:
- 📧 Dodaj filtry po użytkownikach
- 🔍 Wyszukiwarka postów
- 📊 Więcej typów wykresów (scatter, heatmap)
- 💾 Export danych do CSV
- 🎨 Custom theme/branding
- 📈 Analiza czasowa (jeśli API zwróci timestamps)

### Nauka więcej:
- [Streamlit Documentation](https://docs.streamlit.io)
- [Plotly Documentation](https://plotly.com/python/)
- [Pandas Cheat Sheet](https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf)

---

**Powodzenia!** 🚀

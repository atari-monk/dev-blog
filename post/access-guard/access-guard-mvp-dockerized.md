Super! 😄 Przygotowałem kompletny wariant **Docker + docker-compose** dla Twojego MVP AccessGuard.
Będziesz mógł odpalić cały projekt jednym poleceniem i od razu mieć działające API z SQLite.

---

# ✅ **Dockerized AccessGuard MVP**

Struktura projektu:

```
accessguard/
├── app/
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   ├── crud.py
│   └── auth.py
├── tests/
│   └── test_auth.py
├── Dockerfile
├── docker-compose.yml
└── requirements.txt
```

---

# 📌 `Dockerfile`

```dockerfile
# Use official Python image
FROM python:3.12-slim

# Set workdir
WORKDIR /app

# Copy requirements first (caching)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Copy app source
COPY ./app ./app
COPY ./tests ./tests

# Expose FastAPI port
EXPOSE 8000

# Default command
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

---

# 📌 `docker-compose.yml`

```yaml
version: "3.9"

services:
  accessguard:
    build: .
    container_name: accessguard
    ports:
      - "8000:8000"
    volumes:
      - ./app:/app/app
      - ./tests:/app/tests
      - ./accessguard.db:/app/accessguard.db
    environment:
      - PYTHONUNBUFFERED=1
```

---

# 🔹 Uruchomienie

1. Zbuduj i uruchom kontener:

```bash
docker-compose up --build
```

2. Serwer FastAPI będzie dostępny pod:
   [http://127.0.0.1:8000](http://127.0.0.1:8000)

3. Możesz przetestować API za pomocą `curl`, Postman lub Swagger UI:
   [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

# 🔹 Testy w Dockerze

Jeżeli chcesz uruchomić testy w kontenerze:

```bash
docker-compose run --rm accessguard pytest -q
```

✅ Powinny przejść wszystkie testy integracyjne.

---

# 🔹 Notes

* SQLite jest podłączone jako **volume**, więc baza przetrwa restart kontenera.
* Volumes dla `app/` i `tests/` umożliwiają **hot-reload** kodu bez rebuilda.
* Możesz później wymienić SQLite na MSSQL lub PostgreSQL, modyfikując `DATABASE_URL` w `app/database.py`.

---

Jeżeli chcesz, mogę od razu przygotować **wersję docker-compose z Redis + RabbitMQ**, żeby mieć pełne środowisko do cache i eventów dla uprawnień.

Chcesz, żebym to zrobił?

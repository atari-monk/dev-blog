Świetnie! 😄 Oto kompletny wariant **Docker + docker-compose** dla Twojego MVP z **Redis + RabbitMQ**, gotowy do obsługi cache uprawnień i eventów przy zmianach ról.

---

# ✅ AccessGuard MVP + Redis + RabbitMQ

Struktura:

```
accessguard/
├── app/
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   ├── crud.py
│   ├── auth.py
│   └── events.py   # nowy plik do publikacji/odbioru eventów
├── tests/
│   └── test_auth.py
├── Dockerfile
├── docker-compose.yml
└── requirements.txt
```

---

# 📌 `app/events.py`

```python
import json
import asyncio
import aio_pika
import aioredis

REDIS_URL = "redis://redis:6379"
RABBITMQ_URL = "amqp://guest:guest@rabbitmq/"

# Redis cache helper
redis = None

async def init_redis():
    global redis
    redis = await aioredis.from_url(REDIS_URL, decode_responses=True)

async def cache_permission(username: str, resource: str, action: str, allowed: bool):
    key = f"perm:{username}:{resource}:{action}"
    await redis.set(key, json.dumps(allowed), ex=3600)

async def get_cached_permission(username: str, resource: str, action: str):
    key = f"perm:{username}:{resource}:{action}"
    value = await redis.get(key)
    if value is None:
        return None
    return json.loads(value)

# RabbitMQ helper
async def publish_event(event: dict, queue: str = "roles"):
    connection = await aio_pika.connect_robust(RABBITMQ_URL)
    async with connection:
        channel = await connection.channel()
        await channel.declare_queue(queue, durable=True)
        await channel.default_exchange.publish(
            aio_pika.Message(body=json.dumps(event).encode()),
            routing_key=queue
        )

async def consume_events(queue: str = "roles"):
    connection = await aio_pika.connect_robust(RABBITMQ_URL)
    channel = await connection.channel()
    q = await channel.declare_queue(queue, durable=True)
    async with q.iterator() as queue_iter:
        async for message in queue_iter:
            async with message.process():
                event = json.loads(message.body.decode())
                print("Received event:", event)
```

---

# 📌 `app/main.py` (fragmenty zmienione)

```python
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import models, schemas, crud, auth, events
from .database import engine, Base, get_db
import asyncio

Base.metadata.create_all(bind=engine)

app = FastAPI(title="AccessGuard MVP with Redis & RabbitMQ")

@app.on_event("startup")
async def startup_event():
    await events.init_redis()
    # opcjonalnie: start consumer w tle
    # asyncio.create_task(events.consume_events())

@app.post("/permissions/check")
async def check_permission(payload: schemas.PermissionCheck, db: Session = Depends(get_db)):
    cached = await events.get_cached_permission(payload.username, payload.resource, payload.action)
    if cached is not None:
        return {"allowed": cached}

    allowed = crud.check_permission(db, payload.username, payload.resource, payload.action)
    await events.cache_permission(payload.username, payload.resource, payload.action, allowed)
    return {"allowed": allowed}

@app.post("/roles/assign")
def assign_role(payload: schemas.RoleAssign, db: Session = Depends(get_db)):
    user = crud.get_user_by_username(db, payload.username)
    if not user:
        raise HTTPException(404, "User not found")
    role = crud.get_or_create_role(db, payload.role)
    user = crud.assign_role_to_user(db, user, role)
    # publish event to RabbitMQ
    asyncio.create_task(events.publish_event({"user": user.username, "role": role.name}))
    return {"username": user.username, "roles": [r.name for r in user.roles]}
```

---

# 📌 `Dockerfile` (bez zmian w stosunku do poprzedniego)

```dockerfile
FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
COPY ./app ./app
COPY ./tests ./tests
EXPOSE 8000
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

---

# 📌 `docker-compose.yml` (z Redis + RabbitMQ)

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
    depends_on:
      - redis
      - rabbitmq

  redis:
    image: redis:7
    container_name: redis
    ports:
      - "6379:6379"

  rabbitmq:
    image: rabbitmq:3-management
    container_name: rabbitmq
    ports:
      - "5672:5672"
      - "15672:15672" # management UI
```

---

# 🔹 Uruchomienie

1. Build i start kontenerów:

```bash
docker-compose up --build
```

2. API pod: [http://127.0.0.1:8000](http://127.0.0.1:8000)

3. RabbitMQ Management UI: [http://127.0.0.1:15672](http://127.0.0.1:15672) (login: guest / guest)

4. Testy:

```bash
docker-compose run --rm accessguard pytest -q
```

---

# 🔹 Co mamy teraz

* FastAPI + SQLite
* JWT + Argon2 do haseł
* Redis cache uprawnień
* RabbitMQ do eventów przy zmianach ról
* Testy integracyjne działające w kontenerze
* Hot-reload dzięki volumes

---

Jeśli chcesz, mogę teraz przygotować **wersję z MSSQL + Alembic**, żeby można było od razu robić migracje produkcyjne w Dockerze.

Chcesz, żebym to zrobił?

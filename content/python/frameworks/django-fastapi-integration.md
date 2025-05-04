# Django FastAPI Integration

## Combining Django and FastAPI

- **Django Use Cases**:
  - Admin panel
  - ORM and migrations
  - Built-in authentication

- **FastAPI Use Cases**:
  - High-performance async APIs
  - Type validation
  - Auto-generated API docs

## Integration Approaches

### Option 1: Side-by-Side Microservices

- Run Django and FastAPI as separate services
- Route traffic via Nginx:
  ```nginx
  location /admin {
      proxy_pass http://django:8000;
  }

  location /api {
      proxy_pass http://fastapi:8001;
  }
  ```

### Option 2: Mount FastAPI in Django

```python
# asgi.py
import os
from django.core.asgi import get_asgi_application
from fastapi import FastAPI
from starlette.applications import Starlette
from starlette.routing import Mount

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')

django_app = get_asgi_application()
fastapi_app = FastAPI()

application = Starlette(routes=[
    Mount("/api", app=fastapi_app),
    Mount("", app=django_app),
])
```

Run with:
```bash
uvicorn myproject.asgi:application
```

## Considerations

- **Authentication**:
  - Django: Session-based
  - FastAPI: Token-based (JWT/OAuth2)

- **Database**:
  - Use Django ORM or SQLAlchemy
  - Avoid mixing ORMs

## Architecture Options

### FastAPI Backend + Django Frontend

```plaintext
[Django Templates] → [FastAPI API] → [Database]
```

### Separate Frontend

```plaintext
[React Frontend] → [FastAPI API] → [Database]
[Django Admin]   → [Same Database]
```
Jasne — poniżej dostajesz **wersję 2h MVP w formie idealnej do kopiowania**, z pełną strukturą katalogów i oddzielnymi blokami kodu dla każdego pliku.
To jest **dokładnie ten sam projekt**, tylko uporządkowany w stylu „copy & paste”.

Możesz mi później wkleić ten plik `.md`, a ja będę wiedział dokładnie, w którym miejscu kontynuować (Docker, MSSQL, Redis, RabbitMQ, testy integracyjne, architektura, security hardening itd.).

---

# ✅ **ACCESSGUARD — 2h MVP (COPY/PASTE EDITION)**

**Python + FastAPI + SQLAlchemy + JWT + testy**

Struktura:

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
└── requirements.txt
```

---

# 📌 `requirements.txt`

```text
fastapi==0.95.2
uvicorn[standard]==0.22.0
SQLAlchemy==2.0.19
alembic==1.11.1
pydantic==1.10.11
passlib[bcrypt]==1.7.4
PyJWT==2.8.0
httpx==0.24.1
pytest==7.4.0
pytest-asyncio==0.21.0
```

---

# 📌 `app/database.py`

```python
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "sqlite:///./accessguard.db"

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False} if DATABASE_URL.startswith("sqlite") else {}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
```

---

# 📌 `app/models.py`

```python
from sqlalchemy import Column, Integer, String, Table, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from .database import Base

user_roles = Table(
    "user_roles",
    Base.metadata,
    Column("user_id", ForeignKey("users.id"), primary_key=True),
    Column("role_id", ForeignKey("roles.id"), primary_key=True),
)

role_permissions = Table(
    "role_permissions",
    Base.metadata,
    Column("role_id", ForeignKey("roles.id"), primary_key=True),
    Column("permission_id", ForeignKey("permissions.id"), primary_key=True),
)

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)

    roles = relationship("Role", secondary=user_roles, back_populates="users")

class Role(Base):
    __tablename__ = "roles"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)

    users = relationship("User", secondary=user_roles, back_populates="roles")
    permissions = relationship("Permission", secondary=role_permissions, back_populates="roles")

class Permission(Base):
    __tablename__ = "permissions"
    id = Column(Integer, primary_key=True, index=True)
    resource = Column(String, nullable=False)
    action = Column(String, nullable=False)

    roles = relationship("Role", secondary=role_permissions, back_populates="permissions")

class Resource(Base):
    __tablename__ = "resources"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)
    description = Column(String, nullable=True)
```

---

# 📌 `app/schemas.py`

```python
from pydantic import BaseModel
from typing import List

class UserCreate(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"

class RoleAssign(BaseModel):
    username: str
    role: str

class PermissionCheck(BaseModel):
    username: str
    resource: str
    action: str

class UserOut(BaseModel):
    id: int
    username: str
    roles: List[str] = []

    class Config:
        orm_mode = True
```

---

# 📌 `app/auth.py`

```python
from passlib.context import CryptContext
from datetime import datetime, timedelta
import jwt

PWD_CONTEXT = CryptContext(schemes=["bcrypt"], deprecated="auto")

SECRET_KEY = "CHANGE_THIS_SECRET_TO_SOMETHING_STRONG"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60

def hash_password(password: str) -> str:
    return PWD_CONTEXT.hash(password)

def verify_password(plain: str, hashed: str) -> bool:
    return PWD_CONTEXT.verify(plain, hashed)

def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def decode_token(token: str):
    try:
        return jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    except:
        return None
```

---

# 📌 `app/crud.py`

```python
from sqlalchemy.orm import Session
from . import models

def get_user_by_username(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()

def create_user(db: Session, username: str, hashed_password: str):
    user = models.User(username=username, hashed_password=hashed_password)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def get_or_create_role(db: Session, name: str):
    role = db.query(models.Role).filter(models.Role.name == name).first()
    if not role:
        role = models.Role(name=name)
        db.add(role)
        db.commit()
        db.refresh(role)
    return role

def assign_role_to_user(db: Session, user: models.User, role: models.Role):
    if role not in user.roles:
        user.roles.append(role)
        db.commit()
        db.refresh(user)
    return user

def check_permission(db: Session, username: str, resource: str, action: str) -> bool:
    user = get_user_by_username(db, username)
    if not user:
        return False
    for role in user.roles:
        for p in role.permissions:
            if p.resource == resource and p.action == action:
                return True
    return False

def create_permission(db: Session, resource: str, action: str):
    perm = db.query(models.Permission).filter(
        models.Permission.resource == resource,
        models.Permission.action == action
    ).first()
    if not perm:
        perm = models.Permission(resource=resource, action=action)
        db.add(perm)
        db.commit()
        db.refresh(perm)
    return perm

def add_permission_to_role(db: Session, role: models.Role, permission: models.Permission):
    if permission not in role.permissions:
        role.permissions.append(permission)
        db.commit()
        db.refresh(role)
    return role
```

---

# 📌 `app/main.py`

```python
from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from . import models, schemas, crud, auth
from .database import engine, Base, get_db

Base.metadata.create_all(bind=engine)

app = FastAPI(title="AccessGuard MVP")

@app.post("/auth/register", response_model=schemas.UserOut)
def register(user_in: schemas.UserCreate, db: Session = Depends(get_db)):
    existing = crud.get_user_by_username(db, user_in.username)
    if existing:
        raise HTTPException(400, "Username already registered")
    hashed = auth.hash_password(user_in.password)
    user = crud.create_user(db, user_in.username, hashed)
    return schemas.UserOut.from_orm(user)

@app.post("/auth/login", response_model=schemas.Token)
def login(user_in: schemas.UserCreate, db: Session = Depends(get_db)):
    user = crud.get_user_by_username(db, user_in.username)
    if not user or not auth.verify_password(user_in.password, user.hashed_password):
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, "Invalid credentials")
    token = auth.create_access_token({"sub": user.username})
    return schemas.Token(access_token=token)

@app.post("/roles/assign")
def assign_role(payload: schemas.RoleAssign, db: Session = Depends(get_db)):
    user = crud.get_user_by_username(db, payload.username)
    if not user:
        raise HTTPException(404, "User not found")
    role = crud.get_or_create_role(db, payload.role)
    user = crud.assign_role_to_user(db, user, role)
    return {"username": user.username, "roles": [r.name for r in user.roles]}

@app.post("/permissions/create")
def create_permission(resource: str, action: str, role_name: str, db: Session = Depends(get_db)):
    role = crud.get_or_create_role(db, role_name)
    perm = crud.create_permission(db, resource, action)
    crud.add_permission_to_role(db, role, perm)
    return {"role": role.name, "permission": {"resource": resource, "action": action}}

@app.post("/permissions/check")
def check_permission(payload: schemas.PermissionCheck, db: Session = Depends(get_db)):
    allowed = crud.check_permission(db, payload.username, payload.resource, payload.action)
    return {"allowed": allowed}
```

---

# 📌 `tests/test_auth.py`

```python
import pytest
from httpx import AsyncClient
from app.main import app
from app.database import Base, engine

@pytest.fixture(scope="module")
def anyio_backend():
    return "asyncio"

@pytest.fixture(scope="module", autouse=True)
def reset_db():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)

@pytest.mark.anyio
async def test_register_login_and_permissions():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        
        r = await ac.post("/auth/register", json={"username": "alice", "password": "secret"})
        assert r.status_code == 200

        r = await ac.post("/auth/login", json={"username": "alice", "password": "secret"})
        assert r.status_code == 200
        token = r.json()["access_token"]
        assert token

        r = await ac.post("/permissions/create",
                          params={"resource": "door1", "action": "access", "role_name": "guard"})
        assert r.status_code == 200

        r = await ac.post("/roles/assign", json={"username": "alice", "role": "guard"})
        assert r.status_code == 200

        r = await ac.post("/permissions/check",
                          json={"username": "alice", "resource": "door1", "action": "access"})
        assert r.status_code == 200
        assert r.json()["allowed"] is True
```

---

# 🔥 To jest kompletny 2h MVP

Możesz odpalić:

```bash
uvicorn app.main:app --reload
pytest -q
```

---

# ⭐ Co dalej?

Gdy tylko wkleisz ten plik `.md`, będę gotowy automatycznie kontynuować:

* Docker + docker-compose
* Redis jako cache permissions
* RabbitMQ + eventy po zmianach ról
* migracje Alembic
* MSSQL (pyodbc + connection string)
* refaktoryzacja do clean architecture
* logowanie/monitoring/security hardening (OWASP)

---

Jeśli chcesz, mogę też przygotować **README.md** do repo GitHub.

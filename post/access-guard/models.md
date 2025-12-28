This code defines your **database schema and relationships** using **SQLAlchemy ORM**. Specifically, it implements a **Role-Based Access Control (RBAC)** model.

I’ll explain it **from top to bottom**, then summarize how everything connects.

---

## 1. Imports

```python
from sqlalchemy import Column, Integer, String, Table, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from .database import Base
```

* `Column`, `Integer`, `String`, `Boolean` → table columns
* `Table` → used for **many-to-many association tables**
* `ForeignKey` → creates references between tables
* `relationship` → ORM-level relationships
* `Base` → declarative base (from your database setup)

---

## 2. Association (Join) Tables

These tables **do not have ORM classes**, just raw tables.
They are used for **many-to-many relationships**.

---

### `user_roles` (User ↔ Role)

```python
user_roles = Table(
    "user_roles",
    Base.metadata,
    Column("user_id", ForeignKey("users.id"), primary_key=True),
    Column("role_id", ForeignKey("roles.id"), primary_key=True),
)
```

📌 Meaning:

* A **user can have many roles**
* A **role can belong to many users**

Example rows:

```
user_id | role_id
--------+--------
1       | 2
1       | 3
```

The **composite primary key** prevents duplicates.

---

### `role_permissions` (Role ↔ Permission)

```python
role_permissions = Table(
    "role_permissions",
    Base.metadata,
    Column("role_id", ForeignKey("roles.id"), primary_key=True),
    Column("permission_id", ForeignKey("permissions.id"), primary_key=True),
)
```

📌 Meaning:

* A **role can have many permissions**
* A **permission can belong to many roles**

This is how RBAC usually works.

---

## 3. `User` Model

```python
class User(Base):
    __tablename__ = "users"
```

### Columns

```python
id = Column(Integer, primary_key=True, index=True)
username = Column(String, unique=True, index=True, nullable=False)
hashed_password = Column(String, nullable=False)
is_active = Column(Boolean, default=True)
```

* `id` → primary key
* `username` → unique login name
* `hashed_password` → store hashed passwords only
* `is_active` → enable/disable users

### Relationship

```python
roles = relationship("Role", secondary=user_roles, back_populates="users")
```

This gives you:

```python
user.roles          # list of Role objects
role.users          # list of User objects
```

---

## 4. `Role` Model

```python
class Role(Base):
    __tablename__ = "roles"
```

### Columns

```python
id = Column(Integer, primary_key=True, index=True)
name = Column(String, unique=True, nullable=False)
```

Examples:

* `admin`
* `editor`
* `viewer`

### Relationships

```python
users = relationship("User", secondary=user_roles, back_populates="roles")
permissions = relationship("Permission", secondary=role_permissions, back_populates="roles")
```

A role:

* Can belong to **many users**
* Can have **many permissions**

---

## 5. `Permission` Model

```python
class Permission(Base):
    __tablename__ = "permissions"
```

### Columns

```python
id = Column(Integer, primary_key=True, index=True)
resource = Column(String, nullable=False)
action = Column(String, nullable=False)
```

This models permissions like:

```
("documents", "read")
("documents", "write")
("users", "delete")
```

### Relationship

```python
roles = relationship("Role", secondary=role_permissions, back_populates="permissions")
```

Permissions are assigned **to roles**, not directly to users.

---

## 6. `Resource` Model

```python
class Resource(Base):
    __tablename__ = "resources"
```

### Columns

```python
id = Column(Integer, primary_key=True, index=True)
name = Column(String, unique=True, nullable=False)
description = Column(String, nullable=True)
```

This represents protected entities like:

* `documents`
* `reports`
* `users`

⚠️ Note:
Right now, **`Resource` is not linked** to `Permission`.
Instead, permissions store the resource name as a string.

---

## 7. How This All Fits Together (RBAC Flow)

**Access check example**:

> “Can user X perform action Y on resource Z?”

Steps:

1. User → Roles
2. Roles → Permissions
3. Permissions → `(resource, action)`

Diagram:

```
User → user_roles → Role → role_permissions → Permission
```

---

## 8. Example Usage

### Get all permissions for a user

```python
permissions = {
    (p.resource, p.action)
    for role in user.roles
    for p in role.permissions
}
```

### Assign a role to a user

```python
user.roles.append(admin_role)
db.commit()
```

### Assign a permission to a role

```python
role.permissions.append(read_permission)
db.commit()
```

---

## Summary

This code:

* Implements a **clean RBAC schema**
* Uses **many-to-many relationships**
* Keeps permissions **role-based**
* Is scalable and production-friendly

### In one sentence:

> “Users have roles, roles have permissions, permissions define allowed actions on resources.”

---

If you want, I can:

* Add direct `Resource ↔ Permission` foreign keys
* Show a permission-check function
* Add cascade rules
* Optimize queries for large datasets
* Convert this to JWT-based authorization

Just tell me 😊

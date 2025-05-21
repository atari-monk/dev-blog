# FastAPI

To run your FastAPI API locally for testing:

---

## Run API

### 1. **Install dependencies**

Make sure these are installed:

```bash
pip install fastapi uvicorn sqlmodel
```

---

### 2. **Start the server**

From your project root directory:

```bash
uvicorn project.project_api:app --reload
```

* `task_log_2.main` refers to the file `main.py` (or whatever your API file is named) inside the `task_log_2/` package.
* `--reload` enables auto-restart on code changes.

---

## Test API

### Swagger UI:

Open browser at:

```
http://localhost:8000/docs
```

### Alternative: cURL

```bash
curl http://localhost:8000/projects/
```

---

Let me know if your API file is named differently or in another path.

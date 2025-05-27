# Summary of Test Types

---

## 1. **Unit Tests**

* Test individual functions or classes in isolation
* Fast, small scope
* Use assertions to verify correctness
* Usually automated with frameworks like `pytest`
* Folder example: `tests/unit/`

---

## 2. **Integration Tests**

* Test interactions between multiple components or modules
* Verify that combined parts work together correctly
* Often slower than unit tests
* Folder example: `tests/integration/`

---

## 3. **Functional Tests**

* Test features or use cases from an end-user perspective
* May cover UI, APIs, or workflows
* Often automated but can be manual
* Folder example: `tests/functional/`

---

## 4. **End-to-End (E2E) Tests**

* Test entire application flow in real environment
* Validate system behavior as a whole
* Typically slow and complex
* Folder example: `tests/e2e/`

---

## 5. **Smoke Tests**

* Minimal tests to check basic startup and sanity
* Verify system or component **runs without crashing**
* Usually simple scripts, sometimes manual
* Folder example: `smoke/` or `smoke_tests/`

---

## 6. **Manual / Exploratory Tests**

* Ad hoc scripts or manual checks
* Used for debugging, experimenting with components
* No formal assertions or test frameworks
* Folder example: `sandbox/`, `manual_tests/`

---

## 7. **Performance / Load Tests**

* Measure speed, scalability, resource usage
* Stress-test application under load
* Often separate tooling (e.g. JMeter, Locust)

---

## 8. **Regression Tests**

* Verify that new changes don’t break existing functionality
* Usually automated, part of CI pipelines

---

# Quick Folder Naming Guide

| Test Type      | Typical Folder       |
| -------------- | -------------------- |
| Unit           | `tests/unit/`        |
| Integration    | `tests/integration/` |
| Functional     | `tests/functional/`  |
| End-to-End     | `tests/e2e/`         |
| Smoke          | `smoke/`             |
| Manual/Sandbox | `sandbox/`           |
| Performance    | `tests/performance/` |

---

This should help you organize and classify tests clearly!

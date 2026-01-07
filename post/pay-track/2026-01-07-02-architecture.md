Świetny wybór. **PostgreSQL + TypeScript** to dokładnie to, czego oczekuje się w **senior Node.js / AWS / microservices** projekcie.
Jedziemy **na serio**, jak pod realne wdrożenie w Pretius.

Poniżej **KROK 1** – **oficjalny dokument architektoniczny MVP**, w **Markdown**, gotowy do wrzucenia do repo jako `ARCHITECTURE.md`.

---

# PayTrack

## MVP Platformy Zarządzania Płatnościami

**Architecture & Implementation Document**

---

## 1. Cel projektu

Celem projektu **PayTrack** jest stworzenie **produkcyjnej jakości MVP** backendowej platformy płatniczej, która:

* zarządza użytkownikami, kartami płatniczymi, budżetami i transakcjami
* jest oparta o **mikroserwisy**
* działa w **100% w chmurze AWS**
* spełnia wymagania ogłoszenia na stanowisko **Senior Node.js Developer**

Projekt demonstruje:

* zaawansowane użycie **Node.js + TypeScript**
* projektowanie API
* testy automatyczne
* architekturę gotową na skalowanie (50+ serwisów)

---

## 2. Stack technologiczny

### Backend

* **Node.js 14**
* **TypeScript**
* **Express.js**
* **Sequelize + sequelize-typescript**
* **PostgreSQL**

### Cloud / DevOps

* **AWS Lambda**
* **API Gateway**
* **Serverless Framework**
* **GitHub Actions (CI/CD)**

### Testy

* **Jest**
* **ts-jest**
* **Supertest**

---

## 3. Architektura systemu

### Mikroserwisy

| Serwis              | Odpowiedzialność             |
| ------------------- | ---------------------------- |
| user-service        | użytkownicy, dane podstawowe |
| card-service        | karty płatnicze              |
| budget-service      | budżety i limity             |
| transaction-service | transakcje i historia        |

Każdy mikroserwis:

* posiada własną warstwę API
* komunikuje się wyłącznie przez HTTP
* posiada własne modele Sequelize
* może być wdrażany niezależnie

---

## 4. Wzorzec API

* REST
* JSON
* jawne kontrakty request / response
* wersjonowanie `/api/v1`

Przykład:

```
POST /api/v1/users
GET  /api/v1/cards/{id}
```

---

## 5. Model danych (high-level)

### User

* id (UUID)
* name
* email
* createdAt

### Card

* id (UUID)
* userId
* cardNumber (masked)
* status

### Budget

* id (UUID)
* userId
* limit
* currency

### Transaction

* id (UUID)
* cardId
* amount
* currency
* status
* createdAt

---

## 6. Zarządzanie bazą danych

* PostgreSQL jako główna baza
* Sequelize migrations
* każda zmiana schematu przez migrację
* brak `sync({ force: true })` w produkcji

---

## 7. Bezpieczeństwo (MVP scope)

* walidacja danych wejściowych
* separacja odpowiedzialności serwisów
* przygotowanie pod JWT (poza MVP)

---

## 8. Testy automatyczne

* testy jednostkowe modeli
* testy integracyjne endpointów
* testy uruchamiane w CI przed deployem

---

## 9. CI/CD

Pipeline:

1. Install dependencies
2. Lint
3. Tests
4. Build (tsc)
5. Deploy (Serverless → AWS)

---

## 10. Dlaczego ta architektura

* zgodna z wymaganiami Pretius
* skalowalna
* czytelna
* gotowa do dalszego rozwoju
* pokazuje senior-level decision making

---

## 11. Kolejne kroki implementacyjne

1. User Service (pełna implementacja)
2. Card Service
3. Budget Service
4. Transaction Service
5. CI/CD
6. Deployment demo (AWS)

---

📌 **Ten dokument jest celowo pisany jak wewnętrzna dokumentacja projektowa** – dokładnie tego typu rzeczy czytają Tech Leadowie i Architekci.

---

## Następny krok (KROK 2)

W następnej odpowiedzi zrobię:

> **User Service – pełną implementację w TypeScript**
>
> * `sequelize-typescript`
> * migracje
> * DTO
> * testy
> * `serverless.yml`
> * gotowe do wrzucenia do repo i uruchomienia

To będzie **pierwszy produkcyjny mikroserwis** Twojego MVP.

Jeśli chcesz, mogę też:

* pisać **każdy plik osobno** (copy–paste friendly)
* albo generować **całe katalogi na raz**

➡️ **Jak wolisz – plik po pliku czy cały serwis w jednym bloku?**

# Jak włączyć środowisko wirtualne dla projektu Python w Ubuntu

## 📚 Spis treści

- [Środowisko wirtualne w Ubuntu](#srodowisko-wirtualne)
  - [Sprawdzenie i instalacja venv](#venv-install)
  - [Przejście do katalogu projektu](#project-dir)
  - [Tworzenie środowiska wirtualnego](#create-venv)
  - [Aktywacja środowiska](#activate-venv)
  - [Instalowanie pakietów](#install-packages)
  - [Dezaktywacja środowiska](#deactivate-venv)
  - [Plik requirements.txt](#requirements-file)
  - [Ignorowanie środowiska wirtualnego w Git](#gitignore)

- [Update pakietów i requirements.txt](#requirements-update)
  - [Czy potrzebne jest nowe venv](#new-venv-question)
  - [Kiedy NIE tworzyć nowego venv](#no-new-venv)
  - [Kiedy tworzyć nowe venv](#yes-new-venv)
  - [Best practice zespołowe](#best-practice)
  - [Dlaczego nowe venv jest bezpieczniejsze](#why-new-venv)
  - [Synchronizacja zamiast kasowania](#pip-sync)
  - [TL;DR](#tldr)

---

<a id="srodowisko-wirtualne"></a>
## Środowisko wirtualne w Ubuntu

<a id="venv-install"></a>
### 1. Sprawdzenie i instalacja `venv`

```bash
sudo apt update
sudo apt install python3-venv
````

---

<a id="project-dir"></a>

### 2. Przejście do katalogu projektu

```bash
cd /ścieżka/do/twojego/projektu
```

---

<a id="create-venv"></a>

### 3. Tworzenie środowiska wirtualnego

```bash
python3 -m venv .venv
```

Po wykonaniu polecenia powstanie katalog `.venv/`.  
Sprawdź 

```bash
ls -a
```

Ustawienia w configach mogą ukrywać ten katalog, więc może nie być widoczny w VSCode.

---

<a id="activate-venv"></a>

### 4. Aktywacja środowiska

```bash
source .venv/bin/activate
```

Po aktywacji terminal pokaże:

```text
(.venv) user@ubuntu:~/projekt$
```

---

<a id="install-packages"></a>

### 5. Instalowanie pakietów tylko dla projektu

```bash
python -m pip install numpy flask django
```

Pakiety zostaną zainstalowane **wyłącznie w tym środowisku**.

---

<a id="deactivate-venv"></a>

### 6. Dezaktywacja środowiska

```bash
deactivate
```

---

<a id="requirements-file"></a>

### (Opcjonalnie) Plik `requirements.txt`

Zapis zależności:

```bash
python -m pip freeze > requirements.txt
```

Instalacja w nowym środowisku:

```bash
python -m pip install -r requirements.txt
```

---

<a id="gitignore"></a>

### Ignorowanie środowiska wirtualnego w Git

Katalog środowiska wirtualnego (`.venv/`) nie powinien być dodawany do repozytorium.
Środowisko wirtualne jest zależne od systemu operacyjnego i zawsze może zostać
odtworzone na podstawie pliku `requirements.txt`.

Dodaj do pliku `.gitignore`:

```gitignore
.venv/
```

---

<a id="requirements-update"></a>

## Update pakietów i `requirements.txt`

<a id="new-venv-question"></a>

### Czy musisz tworzyć nowe środowisko po zmianie requirements.txt

Krótko: **nie zawsze**, ale **często warto**.

---

<a id="no-new-venv"></a>

### Kiedy NIE tworzyć nowego venv

* dodano nowy pakiet (bez konfliktów)
* zmieniono wersję na konkretną (`==`)
* drobny upgrade zależności

```bash
python -m pip install -r requirements.txt --upgrade
```

---

<a id="yes-new-venv"></a>

### Kiedy tworzyć nowe venv (zalecane)

* usunięto pakiet z `requirements.txt`
* zmieniono zakres wersji (`>=`, `<`)
* występują konflikty
* projekt zachowuje się niestabilnie
* potrzeba 100% powtarzalności

```bash
rm -rf .venv
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

---

<a id="best-practice"></a>

### Best practice zespołowe

#### DEV (lokalnie)

```bash
python -m pip install -r requirements.txt --upgrade
```

Okresowo:

```bash
rm -rf .venv
python3 -m venv .venv
python -m pip install -r requirements.txt
```

#### CI / Docker / PROD

➡ **Zawsze czyste środowisko**

```bash
python -m pip install -r requirements.txt
```

---

<a id="why-new-venv"></a>

### Dlaczego nowe venv jest bezpieczniejsze

* brak starych, nieużywanych pakietów
* brak konfliktów wersji
* łatwiejsze debugowanie
* identyczne środowisko dla całego zespołu

---

<a id="pip-sync"></a>

### Synchronizacja zamiast kasowania środowiska

```bash
python -m pip install pip-tools
pip-sync requirements.txt
```

> Uwaga: `pip-sync` usuwa wszystkie pakiety, których nie ma w `requirements.txt`.

---

<a id="tldr"></a>

## TL;DR

| Zmiana w requirements.txt | Nowe venv |
| ------------------------- | --------- |
| Dodanie pakietu           | ❌         |
| Zmiana wersji `==`        | ❌         |
| Zmiana zakresu            | ⚠️        |
| Usunięcie pakietu         | ✅         |
| CI / PROD                 | ✅         |

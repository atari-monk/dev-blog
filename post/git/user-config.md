# Konfiguracja Git w Ubuntu

## Spis treści
- [Sprawdzenie aktualnych ustawień](#sprawdzenie-aktualnych-ustawien)
- [Ustawienie globalne](#ustawienie-globalne)
- [Ustawienie lokalne](#ustawienie-lokalne)
- [Sprawdzenie ustawień ponownie](#sprawdzenie-ustawien-ponownie)
- [Konfiguracja SSH (opcjonalnie)](#konfiguracja-ssh-opcjonalnie)

<a id="sprawdzenie-aktualnych-ustawien"></a>
## Sprawdzenie aktualnych ustawień
Aby zobaczyć aktualną konfigurację Git:

```bash
git config --list
````

Zwróci np.:

```text
user.name=Jan Kowalski
user.email=jan.kowalski@gmail.com
```

Jeśli nie są ustawione, te wpisy nie będą widoczne.

<a id="ustawienie-globalne"></a>

## Ustawienie globalne

Globalne ustawienia obowiązują **we wszystkich repozytoriach** użytkownika.

```bash
git config --global user.name "Jan Kowalski"
git config --global user.email "jan.kowalski@gmail.com"
```

> Po tym każdy commit w dowolnym repozytorium będzie podpisany tymi danymi.

<a id="ustawienie-lokalne"></a>

## Ustawienie lokalne

Lokalne ustawienia obowiązują tylko w **konkretnym repozytorium**.

Przejdź do katalogu repozytorium:

```bash
cd /sciezka/do/repozytorium
```

Następnie ustaw lokalnie:

```bash
git config user.name "Jan Kowalski"
git config user.email "jan.kowalski@gmail.com"
```

<a id="sprawdzenie-ustawien-ponownie"></a>

## Sprawdzenie ustawień ponownie

Sprawdź konfigurację jeszcze raz:

```bash
git config --list
```

Powinieneś zobaczyć:

```text
user.name=Jan Kowalski
user.email=jan.kowalski@gmail.com
```

<a id="konfiguracja-ssh-opcjonalnie"></a>

## Konfiguracja SSH (opcjonalnie)

Jeśli planujesz **pushować na GitHub/GitLab**, warto ustawić klucz SSH:

```bash
ssh-keygen -t ed25519 -C "jan.kowalski@gmail.com"
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519
cat ~/.ssh/id_ed25519.pub
```

Skopiuj zawartość `.pub` do ustawień SSH w GitHub/GitLab.

---

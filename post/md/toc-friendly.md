Jasne 👍
Poniżej masz **uniwersalny SZABLON PROMPTU w formacie Markdown**, którego możesz używać, żeby **kazać modelowi przerobić dowolny dokument** na poprawny, „TOC-friendly” Markdown (jak ten, który właśnie zrobiłem).

Możesz go **kopiować 1:1** i tylko wklejać dokument poniżej.

---

````md
# Zadanie: Przerób dokument na poprawny Markdown z działającym TOC

## Cel
Przerób poniższy dokument tak, aby:
- wszystkie linki w spisie treści (TOC) działały w GitHub/GitLab
- nie było problemów z polskimi znakami, emoji ani znakami specjalnymi
- dokument był gotowy do użycia jako README.md
- zachowana była cała treść merytoryczna (bez skracania)

## Wymagania techniczne
- użyj ręcznych kotwic HTML: `<a id="..."></a>`
- identyfikatory kotwic:
  - tylko małe litery
  - bez polskich znaków
  - bez spacji (używaj `-`)
- każda sekcja i podsekcja musi mieć własną kotwicę
- spis treści ma być na początku dokumentu
- spis treści musi używać linków `[#kotwica]`

## Struktura wyjściowa
1. Tytuł dokumentu (`#`)
2. Spis treści
3. Treść dokumentu z kotwicami

## Dodatkowe zasady
- nie używaj automatycznych kotwic Markdown
- nie usuwaj żadnych sekcji
- nie zmieniaj sensu nagłówków (możesz je uprościć technicznie)
- kod zawsze w blokach ```bash``` / ```text```
- wynik zwróć jako **jeden kompletny blok Markdown**

---

## Dokument do przerobienia

<<< WKLEJ TUTAJ DOKUMENT >>>
````

---

## 🔥 Wersja krótsza (jeśli chcesz minimum)

```md
Przerób poniższy dokument na README.md:
- dodaj spis treści
- użyj ręcznych kotwic `<a id="">`
- kotwice bez polskich znaków i emoji
- wszystkie linki w TOC muszą działać
- zachowaj całą treść

Dokument:
<<< >>>
```

---

## 🧠 Tipy praktyczne

* Ten prompt działa **najlepiej dla długich dokumentów**
* Nadaje się do:

  * README
  * dokumentacji technicznej
  * notatek zespołowych
  * wiki
* Możesz dodać:

  ```md
  Dopasuj pod MkDocs / Docusaurus / Sphinx
  ```

Jeśli chcesz, mogę:

* zrobić **szablon stricte pod README open-source**
* wersję **pod AI / LLM-friendly docs**
* szablon pod **prompt chaining**

Daj znać 👌

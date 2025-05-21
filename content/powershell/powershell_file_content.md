# Powershell file content 

To display the content of a `.md` (Markdown) file in **short form** in PowerShell (i.e. a concise preview, not the full file), you can use one of these methods:

---

## ✅ Option 1: Display First N Lines (e.g., First 10 Lines)

```powershell
Get-Content .\README.md -TotalCount 10
```

🔹 This shows just the **first 10 lines** of the file.

---

## ✅ Option 2: Show Only the First Few Words or Characters

### First 300 characters:

```powershell
(Get-Content .\README.md -Raw).Substring(0, 300)
```

⚠️ Make sure the file has at least that many characters.

---

## ✅ Option 3: Use `Select-String` to Search and Display Matching Lines

For example, show only lines with a heading:

```powershell
Select-String "^#" .\README.md
```

🔹 This displays only Markdown **headings** (lines starting with `#`).

---

## ✅ Option 4: Preview File in Out-GridView (GUI popup)

```powershell
Get-Content .\README.md | Out-GridView
```

🔹 Useful for scrolling or filtering.

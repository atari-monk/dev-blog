## 🧩 **Modern Pattern: Hide Elements Until Data Loads**

### **1️⃣ CSS**

```css
.hidden {
	opacity: 0;
	pointer-events: none;
	transition: opacity 0.3s ease;
}

.visible {
	opacity: 1;
	pointer-events: auto;
}

.loader {
	text-align: center;
	padding: 1rem;
	font-size: 1.2rem;
	color: #666;
}
```

---

### **2️⃣ HTML**

```html
<div class="loader">Loading data...</div>

<div class="left-column hidden">
	<!-- left column content -->
</div>

<div class="right-column hidden">
	<!-- right column content -->
</div>
```

---

### **3️⃣ JavaScript**

```html
<script type="module">
	document.addEventListener("DOMContentLoaded", async () => {
		const loader = document.querySelector(".loader");
		const left = document.querySelector(".left-column");
		const right = document.querySelector(".right-column");

		try {
			// ✅ Fetch and parse the JSON data
			const res = await fetch("./data.json");
			if (!res.ok) throw new Error(`HTTP ${res.status}`);
			const data = await res.json();

			// ✅ Populate the DOM with JSON data
			console.log("Data loaded:", data);

			// ✅ Reveal the columns once data is ready
			left.classList.replace("hidden", "visible");
			right.classList.replace("hidden", "visible");
		} catch (err) {
			console.error("Error loading JSON:", err);
			loader.textContent = "⚠️ Failed to load data.";
			return;
		}

		// ✅ Hide the loader when done
		loader.remove();
	});
</script>
```

---

### 💡 **Why This Is Great**

- 🧱 **Semantic & modular** — HTML structure stays clean; no inline display logic.
- ⚡ **Fast & async-safe** — JS waits for parsed DOM, not full window load.
- 🎨 **Smooth reveal animation** — transitions improve UX without extra JS.
- 🧭 **Graceful fallback** — if fetch fails, the loader text updates visibly.
- 🧠 **Efficient DOM usage** — minimal queries and clean class toggling.

---

## 📝 **Standard Pattern: Hiding Elements Until Data Loads**

### **1️⃣ CSS**

```css
.hidden {
	display: none;
}
```

### **2️⃣ HTML**

```html
<div class="left-column hidden">
	<!-- left column content -->
</div>

<div class="right-column hidden">
	<!-- right column content -->
</div>
```

### **3️⃣ JavaScript**

```js
document.addEventListener("DOMContentLoaded", async () => {
	try {
		// ✅ Fetch and parse the JSON data
		const res = await fetch("./data.json");
		const data = await res.json();

		// ✅ Populate the DOM with JSON data
		console.log("Data loaded:", data);

		// ✅ Reveal the columns once data is ready
		document.querySelector(".left-column").classList.remove("hidden");
		document.querySelector(".right-column").classList.remove("hidden");
	} catch (err) {
		console.error("Error loading JSON:", err);
	}
});
```

---

### 💡 **Why this is standard practice**

- ✅ Keeps your **HTML semantic** (no inline styles or JS-driven layout changes).
- ✅ Keeps **CSS responsible for visibility**, JS only triggers _state changes_.
- ✅ Scales well — you can apply the same pattern to loaders, modals, or async components.
- ✅ Works consistently across browsers and doesn’t depend on the full window load event.

---

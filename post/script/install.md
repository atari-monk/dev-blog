Got it! Here’s a **clean, step-by-step way** to install your scripts so they work globally on Ubuntu using **pipx** (safe and isolated):

---

### **1️⃣ Ensure pipx is installed**

```bash
sudo apt install pipx
pipx ensurepath
```

> Close and reopen your terminal, or run `source ~/.bashrc` to update PATH.

---

### **2️⃣ Remove old pipx installs (optional, to avoid conflicts)**

```bash
pipx uninstall script
```

> This clears any previous installations of your project.

---

### **3️⃣ Install your project via pipx**

Go to your project folder:

```bash
cd ~/atari-monk/atari-monk/project/script
pipx install .
```

> This creates an isolated environment and installs all `[project.scripts]` (`myinfo`, `log`, `fstree`, etc.) into `~/.local/bin`.

---

### **4️⃣ Make sure `~/.local/bin` is in your PATH**

Check:

```bash
echo $PATH | tr ':' '\n' | grep '.local/bin'
```

* If nothing shows, add this line to `~/.bashrc`:

```bash
export PATH="$HOME/.local/bin:$PATH"
```

Then reload:

```bash
source ~/.bashrc
```

---

### **5️⃣ Test your scripts**

```bash
myinfo
log
fstree
```

They should now work **from any terminal**, both VS Code and normal Ubuntu terminal.

---

✅ **Optional tip:** If you have conflicts with system commands (like `zip`), consider renaming your script in `pyproject.toml` so pipx doesn’t clash.

```bash
cd ~/atari-monk/atari-monk/project/script
pipx install --force .
```

### Dependencies

Dependencies must be stated in toml, for example

```toml
dependencies = [
    "pyperclip"
]
```

and reinstall

---

If you want, I can also write a **one-liner** that does steps 2–4 automatically, cleaning old installs and making all scripts globally available.

Do you want me to do that?

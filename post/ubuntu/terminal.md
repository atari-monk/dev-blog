## Install VS Code via Snap (Recommended)

```bash
sudo apt update
sudo apt install snapd -y
sudo snap install code --classic
```

Run it with:

```bash
code
```

Snap packages are maintained by Microsoft and update automatically.

---

## Create a file

```bash
touch filename.txt
```

```bash
touch file1.txt file2.txt file3.txt
```

```bash
touch /path/to/directory/file.txt
```

### Alternatives (also common)

* Using output redirection:

  ```bash
  echo "" > filename.txt
  ```
* Using a text editor:

  ```bash
  nano filename.txt
  ```

  ```bash
  vim filename.txt
  ```

## ✅ Keep Message History Consistent Across Repos with Blogs or Logs

Use this simple Git workflow to maintain a consistent commit history when updating content like blogs, logs, or documentation:

```bash
git add .
git commit -m "Update content"
git push origin master
```

### Or as a one-liner:

```bash
git add . && git commit -m "Update content" && git push origin master
```

---

## Override commit

```bash
git add . && git commit --amend -m "Update content" && git push --force origin master
```

will **combine** your newly staged changes (`git add .`) with the **previous commit**, and **replace** that previous commit with the new one using the new message `"Update content"`.
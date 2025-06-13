To remove the last commit from a remote repository while keeping the changes in your local working directory, follow these steps:

### 1. **Reset your local branch**  
   Use `git reset` to move the branch pointer back to the previous commit while keeping your changes staged or unstaged:

   ```bash
   git reset HEAD~1  # Keeps changes in the working directory (unstaged)
   ```
   
### 2. **Force-push to the remote**  
   Since you've rewritten history, you need to force-push to update the remote:

   ```bash
   git push origin <branch-name> --force
   ```
   or (safer if others are working on the branch)
   ```bash
   git push origin <branch-name> --force-with-lease
   ```

### **What happens?**  
- The last commit is removed from the remote.  
- Your local changes remain intact (either staged or unstaged).  
- Any collaborators will need to `git pull --rebase` to realign their branches.  

### **Alternative (if the commit is already public and shared)**  
If others have already pulled the commit, consider reverting it instead to avoid disruption:

```bash
git revert HEAD
git push origin <branch-name>
```

This creates a new commit that undoes the changes, preserving history.  

Would you like help with a specific scenario?
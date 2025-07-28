**Prompt:**

> I will provide you with a description of a script or project. Based on this description, generate a plain text (.txt) file that contains a list of actionable tasks needed to accomplish the goal described. Each task should be written clearly and concisely, one per line. Focus on the logical steps required from start to finish, including setup, coding, testing, and any dependencies. Do not include explanations or numbering — just a simple task per line. Output the contents of the TXT file only.
>
> Description:

---

You can follow this prompt with your project description. For example:

**User adds:**

> Description: I want to write a Python script that connects to a remote server via SSH, fetches log files, filters out lines containing errors, and saves them to a local directory with timestamps in the filename.

This would result in a `.txt` output like:

```
Install required Python packages (e.g., paramiko)
Create SSH connection to remote server
Navigate to the directory containing log files
Download log files to local machine
Open each log file and read contents
Filter lines containing the word 'error'
Generate timestamped filenames for filtered logs
Save filtered logs to local directory
Close SSH connection
```

Let me know if you'd like a version of this embedded in a script or tool.

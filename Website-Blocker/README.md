#### This script edits the hosts file on your computer to allow or deny access to certain websites.

- Edit website_list to add or remove the websites you want blocked.
- Edit lines 12 and 13 to change the active hours.
- **win-blocker.pyw** is for Windows and **linux-blocker.py** is for Linux.

### WINDOWS
Use Windows **Task Scheduler** to run `win_blocker.pyw` at startup with high privileges.

### LINUX (Ubuntu)
Run `sudo crontab -e` and add the line `@reboot python3 /path/to/file/linux-blocker.py` at the end.

#### This script edits the hosts file on your computer to allow or deny access to certain websites.

- Edit website_list to add or remove the websites you want blocked.
- Edit lines 13 and 14 to change the active hours.
- Contains a **hosts** file so you can test the changed that are made to this temp file, without admin privileges.

### WINDOWS
- Change `hosts_path = "hosts"` to `hosts_path = r"C:\Windows\System32\drivers\etc\hosts"`.
- Use Windows **Task Scheduler** to start `site_blocker.pyw` at startup with high privileges.

### LINUX
- Change `hosts_path = "hosts"` to `hosts_path = "/etc/hosts"`.
- On Ubuntu, first change `site-blocker.pyw` to `site-blocker.py`. 
- Then, run `sudo crontab -e` and add the line `@reboot python3 /path/to/file/site-blocker.py` at the end.

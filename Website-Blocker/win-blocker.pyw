import time
from datetime import datetime as dt

# Works on Windows (supposing windows are installed in C: drive)
hosts_path = r"C:\Windows\System32\drivers\etc\hosts"
redirect = "127.0.0.1"
# The list with the websites you want to block
website_list = ["www.facebook.com", "facebook.com",
                "instagram.com", "www.instagram.com"]

while True:
    start = dt(dt.now().year, dt.now().month, dt.now().day, 8)  # 8 AM
    end = dt(dt.now().year, dt.now().month, dt.now().day, 16)  # 4 PM
    # Working Hours
    if (start < dt.now() < end):
        print("Working hours...")
        with open(hosts_path, 'r+') as file:
            content = file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect + " " + website + "\n")
    # Off Work
    else:
        print("Fun hours...")
        with open(hosts_path, 'r+') as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()
    time.sleep(60)

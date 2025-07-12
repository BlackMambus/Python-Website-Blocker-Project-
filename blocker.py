import time
from datetime import datetime as dt

# Path to the hosts file (change based on OS)
hosts_path = "/etc/hosts"  # Linux/Mac
# hosts_path = r"C:\Windows\System32\drivers\etc\hosts"  # Windows

redirect = "127.0.0.1"
website_list = ["www.facebook.com", "facebook.com", "www.youtube.com", "youtube.com"]

while True:
    start_time = dt(dt.now().year, dt.now().month, dt.now().day, 8)  # 8 AM
    end_time = dt(dt.now().year, dt.now().month, dt.now().day, 16)   # 4 PM
    if start_time < dt.now() < end_time:
        print("Working hours... Blocking sites.")
        with open(hosts_path, 'r+') as file:
            content = file.read()
            for website in website_list:
                if website not in content:
                    file.write(redirect + " " + website + "\n")
    else:
        print("Fun hours... Unblocking sites.")
        with open(hosts_path, 'r+') as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()
    time.sleep(5)





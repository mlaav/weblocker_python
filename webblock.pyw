import time
from datetime import datetime as dt

host_temp = "hosts"
host_path = "C:\\Windows\\System32\\drivers\\etc\\hosts"
redirect = "127.0.0.1"
website_list = ["www.facebook.com","\n","facebook.com","\n","www.yahoo.com"]

while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, 8) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day,18):
        print("Keep Busy")
        with open(host_path, 'r+') as file:
            content = file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect+" "+ website+"\n")
    else:
        with open(host_path, 'r+') as file:
            content = file.read()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
                file.truncate()
        print("have a break")
    time.sleep(5)

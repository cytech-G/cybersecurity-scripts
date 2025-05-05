import time
with open("/var/log/auth.log", "r") as file:
    file.seek(0, 2)
    while True:
        line = file.readline()
        if line:
            print("[LOG] >>", line.strip())
        time.sleep(0.5)

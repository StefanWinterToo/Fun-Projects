from tester import exec
import time

i = 0

while i < 300:
    i = i + 1
    try:
        exec()
    except:
        time.sleep(5)
        print("exception")
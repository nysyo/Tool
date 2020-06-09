import pyperclip
import time
while True:
    pyperclip.copy(pyperclip.paste().replace('\r\n',' '))
    time.sleep(1)
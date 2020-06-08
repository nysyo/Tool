import pyperclip
import time
while True:
    pyperclip.copy(' '.join(pyperclip.paste().split('\r\n')))
    time.sleep(1)
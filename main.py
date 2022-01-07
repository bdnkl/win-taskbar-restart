import subprocess
from pathlib import Path

subprocess.call(['powershell' , 'taskkill /f /im explorer.exe'])
subprocess.call(['powershell' , 'start explorer'])
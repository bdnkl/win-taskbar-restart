from pathlib import Path

VERSION = '0.0.1'
AUTHOR = 'bdnkl'
NAME = 'TaskbarRestart'
DESC = 'Restart windows taskbar'
ICON = ''  # path to icon
MAIN_SCRIPT_NAME = 'main'

LOG_FILE = False  # logging to file

# when creating a msi with cx_freeze
MSI_UPGRADE_CODE = '{ab7525f7-7c9c-4516-a6c3-6dc3b692f72d}'  # https://www.guidgen.com/
MSI_TARGET_DIR = f'C:/ProgramData/{NAME}'
MSI_WINDOW_BASE = 'Console'  # 'Win32GUI' (for tkinter / qt applications), 'Console' (for console applications)
MSI_ALL_USERS = False  # requires admin rights when installing

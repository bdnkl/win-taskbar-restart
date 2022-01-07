"""
Freeze python program to a exe / msi installer.

Creating a exe (is not a single file):
python setup.py build_exe
=> in build folder

Creating a msi installer:
python setup.py bdist_msi
=> in dist folder

"""
import shutil
from cx_Freeze import setup, Executable

import settings

shutil.rmtree('build', ignore_errors=True)

build_exe_options = dict(
    packages=[],
    excludes=[
        'tkinter' if settings.MSI_WINDOW_BASE == 'Console' else None,
        'test'  # not needed for frozen
    ],
    include_files=[],
    bin_excludes=[]
)

shortcut_table = [(
    "DesktopShortcut",  # Shortcut
    "DesktopFolder",  # Directory_
    settings.NAME,  # NameIm
    "TARGETDIR",  # Component_
    f"[TARGETDIR]\\{settings.MAIN_SCRIPT_NAME}.exe",  # Target
    None,  # Arguments
    None,  # Description
    None,  # Hotkey
    "",  # Icon
    0,  # IconIndex
    None,  # ShowCmd
    'TARGETDIR'  # WkDir
)]

bdist_msi_options = dict(
    initial_target_dir=settings.MSI_TARGET_DIR,
    install_icon=settings.ICON,
    upgrade_code=settings.MSI_UPGRADE_CODE,
    product_code=settings.MSI_UPGRADE_CODE,
    data=dict(Shortcut=shortcut_table),
    all_users=settings.MSI_ALL_USERS,  # admin rights
    environment_variables=[]
)

exe = Executable(
    script=f"{settings.MAIN_SCRIPT_NAME}.py",
    base=settings.MSI_WINDOW_BASE,
    icon=settings.ICON
)

setup(name=settings.NAME,
      version=settings.VERSION,
      description=settings.DESC,
      author=settings.AUTHOR,
      options={
          "build_exe": build_exe_options,
          "bdist_msi": bdist_msi_options,
      },
      executables=[exe])
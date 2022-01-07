# win-taskbar-restart
Kill explorer service and restart it.

---

Solves problem of Windows 11 that some icons are not shown at the taskbar after waking up from energy saving mode.


## Install packages
```
pip install -r requirements.txt
```
## Run program
```
python main.py
```
## Create exe
```
python setup.py build_exe
```
## Create msi installer
```
python setup.py bdist_msi
```
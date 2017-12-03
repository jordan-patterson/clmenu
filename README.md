#Menu tool for command line

####A small tool written in python to easily create arrow menus in command line applications.

#Installation:
```bash
pip3 install clmenu
```

#Usage:
```python
from clmenu import Menu

options = ['Option1', 'Option2', 'Option3']
instructions = 'This s a demo, select an option'
menu = Menu(options,instructions,"logo.txt")
option_selected=options[menu.prompt()]
```
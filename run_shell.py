import os;
p = os.curdir;
os.chdir(os.getenv("HOME")+"/programming-language/loscript")
os.system("python3 shell.py")
os.chdir(p)
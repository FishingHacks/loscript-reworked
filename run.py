import os
from posixpath import join
import loscript as basic
import sys
import tools
import progress

try:
    file = open("language/lang.lsc")
except:
    exit()
lines = file.readlines()
code = ""
for line in lines:
    code += line.strip() + "\n"
result, error = basic.run("Loads functions", code, True)

def parse_args(args: list):
    el = args.pop()
    while(len(args)>0):
        if(el=="-man"):
            print("lsc-run [options] filename")
            print("-v, --version               Shows the version")
            print("-man,                        Shows the manual")
            print("Loscript Interpreter ...... v1.1")
        if(el=="-v") | (el=="--version"):
            print("v1.1")
            sys.exit(0)
        else:
            break
        el=args.pop()
        

args = sys.argv
args.reverse()
parse_args(args)
if(len(args)<=0):
    print("File path missing")
    exit(1)


filepath = str(join(os.curdir, args[-1]))
try:
    file = open(filepath)
except:
    print("File " + filepath.split("/")[-1] + " does not exist")
    file.close()
    exit()
lines = file.readlines()
code = ""
for line in lines:
    code += line.strip() + "\n"
result, error = basic.run(filepath.split("/")[-1], code, False)
if error:
    print(error.as_string())
file.close()
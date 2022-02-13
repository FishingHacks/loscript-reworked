import os
import loscript as basic
import sys
import tools
import progress

strict = False
out = True

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
    global out
    global strict
    out=True
    strict=False
    el = args.pop()
    while(len(args)>0):
        if(el=="-man"):
            print("lsc")
            print("-v, --version               Shows the version")
            print("-man                        Shows the manual")
            print("-ltest, --lib-test          Tests the library")
            print("-s, --surpressed            Don't print debug informations")
            print("--strict                    Start in strict mode")
            sys.exit(0)
        if(el=="-ltest")|(el=="--lib-test"):
            try:
                file = open("language/lang.lsc")
            except:
                exit()
            lines = file.readlines()
            code = ""
            for line in lines:
                code += line.strip() + "\n"
            result, error = basic.run("Loads functions", code, False)
            if error:
                print(error.as_string())
            elif len(result.elements) == 1:
                print(tools.colors.parse(str(result.elements[0])))
            else:
                print(tools.colors.parse(str(result)))
        if(el=="-s")|(el=="--surpressed"):
            out=False
        if(el=="-v") | (el=="--version"):
            if(out): print("v1.0.0")
            sys.exit(0)
        if(el=="--strict"):
            strict=True
        # if(el=="-c"):
        #     el = args.pop()
        #     result, error = basic.run("<stdin>", el, strict)
        #     if error:
        #         if(out): print(error.as_string())
        #     if result:
        #         if len(result.elements) == 1:
        #             if(out): print(tools.colors.parse(str(result.elements[0])))
        #         else:
        #             if(out): print(tools.colors.parse(str(result)))
        #     sys.exit(1)
        if(len(args)>0):
            el = args.pop()

args = sys.argv
# args.reverse()
# args.pop()
# args.reverse()
parse_args(args)

quit = False
while True:
    text = input('lolscript > ')
    if ((text == "--stop") | (text == "stop") | (text == "exit")):
        progress.createprogress(50, .02, 'Stopping', 'Stopped!')
        break
    if (text.startswith("\"strict\"")):
        strict=True
        continue
    elif text.startswith("\"unstrict\""):
        strict = False
        continue
    else:
        result, error = basic.run('<stdin>', text, strict_mode=strict)

    if error:
        if(out): print(error.as_string())
    if result:
        if len(result.elements) == 1:
            if(out): print(tools.colors.parse(str(result.elements[0])))
        else:
            if(out): print(tools.colors.parse(str(result)))

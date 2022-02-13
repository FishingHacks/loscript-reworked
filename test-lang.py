import loscript as basic
import tools

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
if error:
    if (out): print(error.as_string())
if result:
    if len(result.elements) == 1:
        if (out): print(tools.colors.parse(str(result.elements[0])))
    else:
        if (out): print(tools.colors.parse(str(result)))

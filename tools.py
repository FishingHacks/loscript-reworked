import random
import os
import string
import psutil
import base64


class colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    GREEN = '\033[92m'
    CYAN = '\033[96m'
    BLUE = '\033[94m'
    WARNING = '\033[93m'
    YELLOW = '\033[93m'
    FAIL = '\033[91m'
    RED = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

    def parse(txt: str):
        return txt.replace("<color:white>", colors.ENDC).replace("<color:blue>", colors.BLUE).replace("<color:cyan>", colors.CYAN).replace("<color:green>", colors.GREEN).replace("<color:yellow>", colors.YELLOW).replace("<color:red>", colors.RED).replace("<color:bold>", colors.BOLD).replace("<color:underline>", colors.UNDERLINE).replace("<color:reset>", colors.ENDC) + colors.ENDC


class processManager:
    def isRunning(processname):
        for proc in psutil.process_iter():
            try:
                if processname.lower() in proc.name().lower():
                    return True
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass
        return False

    def getRunningprocesses():
        rt = []
        for proc in psutil.process_iter():
            rt.append(proc)
        return rt

    def startProcess(file):
        try:
            os.system(file)
        except:
            pass

    def getProcessID(name):
        for proc in psutil.process_iter():
            try:
                if name.lower() in proc.name().lower():
                    return proc.pid
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass
        return False


class process:
    def __init__(self, pid) -> None:
        self.proc = None
        for proc in psutil.process_iter():
            try:
                if pid == proc.pid:
                    self.proc = proc
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass
        if self.proc == None:
            return False

    def kill(self):
        os.system("taskkill /f /pid " + str(self.proc.pid))

    def getprocess(self):
        return self.proc


def parse_int(string):
    return int(string)


def throwError(message):
    print(colors.FAIL + message + colors.ENDC)


def throwWarning(message):
    print(colors.WARNING + message + colors.ENDC)


def throwSuccessful(message):
    print(colors.OKGREEN + message + colors.ENDC)


def Error(message):
    return colors.FAIL + message + colors.ENDC


def Warning(message):
    return colors.WARNING + message + colors.ENDC


def Successful(message):
    return colors.OKGREEN + message + colors.ENDC


def rand(min=0, max=1000):
    random.randint(min, max)


def listdir(source):
    try:
        number = 0
        for file in os.listdir(source):
            number += 1
        return [os.listdir(source), number]
    except:
        return None


def getDisks():
    return ['%s' % d for d in string.ascii_uppercase if os.path.exists('%s:' % d)]


def getDiskContent(disk):
    if disk in getDisks():
        return listdir(disk + ":/")[0]


class base:
    class b64:
        def decode(str: str):
            return base64.b64decode(str).decode("utf-8")

        def encode(str: str):
            return base64.b64encode(str.encode("utf-8")).decode("utf-8")

    class b32:
        def decode(str: str):
            return base64.b32decode(str).decode("utf-8")

        def encode(str: str):
            return base64.b32encode(str.encode("utf-8")).decode("utf-8")

    class b16:
        def decode(str: str):
            return base64.b16decode(str).decode("utf-8")

        def encode(str: str):
            return base64.b16decode(str.encode("utf-8")).decode("utf-8")

    class b85:
        def decode(str: str):
            return base64.b85decode(str).decode("utf-8")

        def encode(str: str):
            return base64.b85decode(str.encode("utf-8")).decode("utf-8")


def xor(a: str, b: str):
    b1 = bytearray(a.encode("UTF-8"))
    b2 = bytearray(b.encode("UTF-8"))
    b = bytearray(len(b1))
    if(len(b1) >= len(b2)):
        for i in range(len(b1)):
            b[i] = b1[i] ^ b2[i % len(b2)]
    elif(len(b2) > len(b1)):
        for i in range(len(b2)):
            b[i] = b1[i % len(b1)] ^ b2[i]
    return b.decode("UTF-8")


def escape_html(str: str):
    return str.replace("<", "&lt;").replace(">", "&gt;").replace("&", "&amp;").replace("\"", "&quot;").replace("'", "&#39;")

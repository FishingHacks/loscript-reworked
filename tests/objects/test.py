undefined = "undefined"

def getRef(ref:str, objects:dict):
    obj_name = ref.split(".")

    obj = objects.get(obj_name[0])
    obj_name.pop(0)

    while len(obj_name)>0:
        if isinstance(obj, cDict):
            obj = obj.get(obj_name[0])
        else:
            obj="undefined"
        if obj==None:
            obj="undefined"
        obj_name.pop(0)

    return obj

def setRef(ref:str, objects:dict, value:any):
    obj_name = ref.split(".")

    obj = objects.get(obj_name[0])
    obj_name.pop(0)

    while len(obj_name)>1:
        if isinstance(obj, cDict):
            nobj = obj.get(obj_name[0])
            if nobj==None:
                obj.set(obj_name[0], cDict({}))
            obj = obj.get(obj_name[0])
        else:
            obj=None
        obj_name.pop(0)
    if isinstance(obj, cDict):
        obj.set(obj_name[0], value)

class cDict(dict):
    def set(self, ref, val):
        self[ref]=val

objects = cDict({
    "sys": cDict({
        "addaudithook": cDict({
            "class": "getroffen!"
        })
    })
})

ref=input("set >>> ")
val=input("value >>> ")

setRef(ref, objects, val)

to_print = input("Object reference >>> ")

print(getRef(to_print, objects))
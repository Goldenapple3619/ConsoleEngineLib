from .Constants import *

def get_clear(OS):
    if OS == "Windows":
        from os import system

        return lambda: system("cls")

    elif OS == "Linux":
        from os import popen

        file = popen('clear')
        clear = file.read()
        file.close()

        return lambda: print(clear)

    else:
        print("OS invalid !")
        exit(0)

def easy_reader(file) -> str:
    file = open(file,"r")
    data = file.read()
    file.close()

    return data

def easy_writer(file, arg, content) -> None:
    if arg in ["w", "w+","a","a+","wb"]:
        file = open(file, arg)
        file.write(content)
        file.close()

def write_screen_data(path, all) -> None:
    easy_writer(path,"wb" ,all)

def read_screen_data(path) -> str:
    file = open(path, "rb")
    all = file.read()
    file.close()
    return str(all)

def get_back_color(r, g, b):
    return ANSI_SEQ.replace("$value$", BG_RGB.replace("$r$", str(r)).replace("$g$", str(g)).replace("$b$", str(b)))

def get_color(r, g, b):
    return ANSI_SEQ.replace("$value$", FG_RGB.replace("$r$", str(r)).replace("$g$", str(g)).replace("$b$", str(b)))

def pos_format(pos ,sizes) -> tuple:
    pos = list(pos)

    if pos[0] == sizes[0]: pos[0] -= 2
    if pos[1] == sizes[1]: pos[1] -= 2

    return tuple(pos)

def find_fore_objects(objects,iid) -> object:
    for obj in objects:
        if iid == obj.get_iid():
            return obj

def find_back_objects(objects, iid):
    return [item for obj in objects for item in obj if "iid" in item and iid == item["iid"]]
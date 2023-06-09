from time import sleep

from .Fore import Fore
from .ErrorsHandler import check_index

class Backup:
    def __init__(self, backup):
        self.console = backup

    def get(self) -> list:
        return self.console

    def update(self, obj) -> None:
        self.console = obj

class Console:
    def __init__(self, sizes, clear, fps):
        self.objects = []; self.CONSOLE = []

        self.fps = round(fps, 5)

        self.size = sizes

        self.clear = clear

        self.backup = Backup(self.CONSOLE)

    def get_size(self) -> tuple:
        return self.size

    def set_fps(self, fps) -> None:
        self.fps = round(fps, 5)

    def get_objects(self) -> list:
        return self.objects

    def get_object_pos(self, pos) -> list:
        return self.CONSOLE[pos[1]][pos[0]]

    def get_stacked(self, object) -> dict:
        return self.CONSOLE[object.get_pos()[1]][object.get_pos()[0]]

    def create_console(self) -> None:
        self.CONSOLE = [[{"shape":' ', "collision":False} for _ in range(self.size[0] - 1)] for _ in range(self.size[1] - 1)]

    def create_forground(self,controls, iid, pos,shape, colid) -> None:
        self.objects.append(Fore(controls,iid,pos,shape, colid))

    def edit_pos_console(self, to_change, pos, p_pos, check_with) -> list:
        to_go = (p_pos[1] + pos[1],p_pos[0] + pos[0])

        if not check_index(self.CONSOLE, to_go): return p_pos

        for item in check_with:
            if item.get_pos() == [to_go[1],to_go[0]] and item.check_collider() and to_change.check_collider(): return p_pos

        if self.CONSOLE[to_go[0]][to_go[1]]["collision"] and to_change.check_collider(): return p_pos

        result = self.put((p_pos[0],p_pos[1]),{"shape":' ', "collision":False}) if self.backup.get() == [] else self.put((p_pos[0],p_pos[1]),self.backup.get()[p_pos[1]][p_pos[0]])
        if not result: return p_pos

        to_change.update_pos(pos)

        return to_change.get_pos()


    def put(self,pos, objects) -> bool:
        if not check_index(self.CONSOLE,(pos[1],pos[0])): return False
        self.CONSOLE[pos[1]][pos[0]] = objects
        return True

    def save_console(self) -> None:
        self.backup.update(self.CONSOLE)

    def place_objects(self) -> list:
        if self.objects == []: return self.CONSOLE

        temp_console = [[{**dicte} for dicte in item] for item in self.CONSOLE]

        for objects in self.objects:
            to_place = objects.get_pos()
            if check_index(temp_console, (to_place[1],to_place[0])): temp_console[to_place[1]][to_place[0]]['shape'] = objects.get_shape()

        return temp_console

    def reset(self) -> None:
        self.objects = []
        self.create_console()
        self.backup.update(self.CONSOLE)

    def display_change(self) -> None:
        self.clear()

        print("".join(''.join(str(char["shape"]) for char in line) + '\n' for line in self.place_objects()))

        sleep(self.fps)
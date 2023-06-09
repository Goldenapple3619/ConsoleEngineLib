#!/usr/bin/env python3


__author__      = "[Goldenapple]#3619"
__copyright__   = "Copyright 2021, Goldenapple"
__all__ = ["Engine"]


from time import sleep

from .src.packages.keyboard import is_pressed

from .src.Console import Console
from .src.ABC import get_clear, pos_format, find_fore_objects, find_back_objects, get_back_color, get_color, END

class Engine:
    def __init__(self,sizes=[100,30], fps=30, warning=True, clear=True):
        from platform import system

        if clear:
            self.console = Console(sizes, get_clear(system()), 1 / fps)
        else:
            self.console = Console(sizes, lambda: '', 1 / fps)

        if system() == 'Windows' and clear:
            from os import system

            system(f'mode con: cols={sizes[0]} lines={sizes[1]+1}')
            get_clear("Windows")()

        elif system() == 'Linux' and clear:
            get_clear("Linux")()

        if warning and fps > 60:
            print("WARNING! HIGHT FPS CAUSE PROGRAM RENDERING GO LAGGY (call engine with warning=False to stop showing this)")
            sleep(6)

        self.console.create_console()

    def reset(self):
        self.console.reset()

    def clear(self):
        self.console.clear()

    def get_back(self, pos):
        return self.console.get_object_pos(pos)

    def get_backs_id(self, iid):
        return find_back_objects(self.console.CONSOLE, iid)

    def draw_fore(self, iid, pos,shape, colid, controls=None) -> None:
        self.console.create_forground(controls, iid, pos,shape, colid)

    def set_fps(self, fps) -> None:
        self.console.set_fps(1 / fps)

    def draw(self, sizes, iid, pos,shape, colid=False) -> None:
        pos = pos_format(pos,self.console.get_size())

        for height in range(sizes[1]):
            for width in range(sizes[0]):
                self.console.put((pos[0] + width,pos[1] + height),{'shape':shape,"iid":iid,"collision":colid})

    def draw_text(self, iid, pos, text, colid=False) -> None:
        pos = pos_format(pos,self.console.get_size())
        text = str(text)

        for letter in range(len(text)):
            if text[letter] == '\n':
                pos[1] += 1
            else:
                self.console.put((pos[0] + letter, pos[1]), {'shape':text[letter],"iid":iid,'collision':colid})

    def move_fore(self,iid,pos) -> None:
        find_fore_objects(self.console.get_objects(),iid).set_pos(pos)

    def get_under(self, iid) -> str:
        return self.console.get_stacked(find_fore_objects(self.console.get_objects(),iid))

    def get_fore_pos(self, iid) -> list:
        return find_fore_objects(self.console.get_objects(), iid).get_pos()

    def get_key_pressed(self, key) -> True:
        return True if is_pressed(key) else False

    def check_key_fore(self,iid) -> None:
        all = self.console.get_objects()

        to_change = find_fore_objects(all,iid)

        actual = to_change.get_controls()

        if actual is None:
            return

        p_pos = to_change.get_pos()

        for control in actual:
            control = actual[control]
            if not is_pressed(control[0]):
                continue;
            if control[1] == 'up':
                p_pos = self.console.edit_pos_console(to_change,(0,-1), p_pos, all)

            if control[1] == 'bottom':
                p_pos = self.console.edit_pos_console(to_change,(0,1), p_pos, all)

            if control[1] == 'left':
                p_pos = self.console.edit_pos_console(to_change,(-1,0), p_pos, all)

            if control[1] == 'right':
                p_pos = self.console.edit_pos_console(to_change,(1,0), p_pos, all)


    def save(self) -> None:
        self.console.save_console()

    def display(self) -> None:
        self.console.display_change()
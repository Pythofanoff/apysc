import os
import time

import keyboard
from colorama import Fore, Style, init

from .cli import build, open_cfg, clear_cache

init(autoreset=True)

class TUI:
    MOVE_DOWN: str = "down" # DEFAULT = "down"
    MOVE_UP: str = "up" # DEFAULT = "up"
    BACK_TO_MENU: str = "esc" # DEFAULT = "esc"
    CONFIRM: str = "enter" # DEFAULT = "enter"

    FILLER: str = " " # DEFAULT = " "
    CURSOR: str = ">> " # DEFAULT = ">> "
    CHOOSE_COLOR = Fore.LIGHTGREEN_EX # DEFAULT = Fore.LIGHTGREEN_EX 

    L_PADX: int = 1 # DEFAULT = 1
    R_PADX: int = 0 # DEFAULT = 0

    MENU: tuple = (
        "Start",
        "Open config",
        "Clear caches",
        "Exit"
    )

    def __init__(self) -> None:
        self.string_id: int = 0

        self.menu_view()
        self.controller()

    def menu_view(self) -> None:
        menu = list(self.MENU)

        os.system("cls" if os.name == "nt" else "clear")
        print(rf"""{Fore.LIGHTMAGENTA_EX}
    _    ____        ____   ____ 
   / \  |  _ \ _   _/ ___| / ___|
  / _ \ | |_) | | | \___ \| |    
 / ___ \|  __/| |_| |___) | |___ 
/_/   \_\_|    \__, |____/ \____|
               |___/             
""")

        select = self.CHOOSE_COLOR+ Style.BRIGHT + " ".join(menu[self.string_id].upper()) + Style.DIM + Fore.RESET
        menu[self.string_id] = self.FILLER * self.L_PADX + self.CURSOR + select + self.FILLER * self.R_PADX
        menu = "\n".join(menu)
        print(menu)

    def controller(self) -> None:
        count_menu_lines = len(self.MENU)-1

        while True:
            event = keyboard.read_event()
            key = event.name

            if event.event_type == keyboard.KEY_UP:
                continue

            if key == self.MOVE_DOWN and self.string_id == count_menu_lines:
                self.string_id = 0 
            elif key == self.MOVE_UP and self.string_id == 0:
                self.string_id = count_menu_lines
            elif key == self.MOVE_DOWN and self.string_id < count_menu_lines:
                self.string_id += 1
            elif key == self.MOVE_UP and self.string_id > 0:
                self.string_id -= 1
            elif key == self.BACK_TO_MENU:
                pass
            elif key == self.CONFIRM:
                self.do()
                continue
            else:
                continue

            self.menu_view()

    def do(self) -> None:
        os.system("cls" if os.name == "nt" else "clear")

        if self.string_id == 0:
            print("Starting...")
            build() 
            self.menu_view()
        elif self.string_id == 1:
            print("Opening...")
            open_cfg()
            self.menu_view()
        elif self.string_id == 2:
            print('Clear caches...')
            clear_cache()
        elif self.string_id == 3:
            print("Exiting...")
            time.sleep(0.1)
            quit() 
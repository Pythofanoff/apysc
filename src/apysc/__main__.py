import os
import shutil
import time
import venv
from datetime import datetime
from importlib.metadata import version
from pathlib import Path

import toml
from colorama import Style, init

from .config import (ARCHITECTURE, DESCRIPTION, INIT_GIT, LANGUAGE, LICENSE,
                     NAME_OF_PROJECT, QUIET_LAUNCH, REPLACE_EXISTS_FILE, VENV)
from .constants import (GITIGNORE, GNU, MIT, TOML, ApacheLicenseVersion2,
                        MPLVersion2)
from .theme import (BASE_COLOR, CREATED, ERRORS, FILES, FOLDERS, INFO, LOGO,
                    MODIFIED, REMAINING, SKIPPED, TIME, TOTAL,
                    VIRTUAL_ENVIROMENT, WARNINGS)
from .utils.fileutils import cfg_open

init(autoreset=True)

class Builder:
    DOT_WIDTH: int = 46

    ENCODING: str = "utf-8"
    FORMAT_TIME: str = "%H:%M:%S:%m"
    CFG_PATH: str = 'apysc/paths.json'

    def __init__(self):
        self.skipped: int = 0
        self.created: int = 0
        self.modified: int = 0
        self.total: int = 0

        self.cfg = cfg_open(path=self.CFG_PATH)

        label = "virtual environments "
        padded_label = f"{label + BASE_COLOR:.<60}"

        print(
            f"\r{self.get_time()}{BASE_COLOR}"
            f"Creating {VIRTUAL_ENVIROMENT}{padded_label}{BASE_COLOR} ",
            end="",
            flush=True,
        )

        self.builder_venv()
        print(f"\r{self.get_time()}{BASE_COLOR}Initialization git... ", end="", flush=True)
        self.builder_git()
        print(f"{self.get_time()}{BASE_COLOR}Creating {FOLDERS}folders{BASE_COLOR}...")
        self.builder_folders()
        print(f"{self.get_time()}{BASE_COLOR}Creating {FILES}files{BASE_COLOR}...")
        self.builder_files()

    def get_time(self):
        current_time = datetime.now().strftime(self.FORMAT_TIME)
        return f'{BASE_COLOR}[{BASE_COLOR} {TIME}{current_time}{BASE_COLOR} {BASE_COLOR}]: '

    def skipping(self, value: str, color: str, msg: str='File already exists: '):
        print(
            f"{BASE_COLOR}└───{BASE_COLOR}{self.get_time()}"
            f"{msg}"
            f"{FOLDERS}{value + ' ' f'{BASE_COLOR}':.<{self.DOT_WIDTH-2}} "
            f"{SKIPPED}SKIPPED"
        )
        self.skipped += 1

    def creating(self, value: str, color: str):
        print(
            f"{BASE_COLOR}└───{BASE_COLOR}{BASE_COLOR}{self.get_time()} "
            f"{FOLDERS}{value + ' ' f'{BASE_COLOR}':.<{self.DOT_WIDTH}} "
            f"{CREATED}CREATED"
        )
        self.created += 1   

    def editing(self, value: str, color: str, msg: str='File already exists:'):
        print(
            f"{BASE_COLOR}└───{BASE_COLOR}{self.get_time()}"
            f"{msg}"
            f"{FILES}{value + ' ' f'{BASE_COLOR}':.<{self.DOT_WIDTH}} " 
            f"{MODIFIED}MODIFIED"
        )
        self.modified += 1   

    def builder_folders(self):
        FOLDERS_PATHS = self.cfg[LANGUAGE][ARCHITECTURE]["folders_path"]
        
        for folder_path in FOLDERS_PATHS:
            self.total += 1
            
            folder_path = folder_path.replace("{NAME_OF_PROJECT}", NAME_OF_PROJECT)
            is_folder_exists = os.path.exists(folder_path)
            
            if is_folder_exists:
                self.skipping(color=FOLDERS, value=folder_path)
                continue

            os.makedirs(folder_path, exist_ok=True)
            self.creating(color=CREATED, value=folder_path)

    def builder_files(self):
        FILES_PATHS = self.cfg[LANGUAGE][ARCHITECTURE]["files_path"]

        for file_path in FILES_PATHS:
            self.total += 1

            file_path = file_path.replace("{NAME_OF_PROJECT}", NAME_OF_PROJECT)
            path = Path(file_path)
            is_file_exists = os.path.exists(file_path)

            if is_file_exists and not REPLACE_EXISTS_FILE:
                self.skipping(color=SKIPPED, value=file_path)
                continue

            if file_path == ".gitignore":
                path.write_text(GITIGNORE, encoding=self.ENCODING)
            elif file_path == "LICENSE":
                if not LICENSE.isspace():
                    if LICENSE.lower() == "mit":
                        path.write_text(MIT, encoding=self.ENCODING)
                    elif LICENSE.lower() == "apachelicenseversion2":
                        path.write_text(ApacheLicenseVersion2, encoding=self.ENCODING)
                    elif LICENSE.lower() == "gnu":
                        path.write_text(GNU, encoding=self.ENCODING)
                    elif LICENSE.lower() == "mpl":
                        path.write_text(MPLVersion2, encoding=self.ENCODING)
                else: path.write_text("", encoding=self.ENCODING)
            elif file_path == "README.md":
                if not DESCRIPTION.isspace():
                    open(file_path, "w", encoding=self.ENCODING).write(DESCRIPTION)                             
                else: path.write_text("", encoding=self.ENCODING)
            elif file_path == "pyproject.toml":
                path.write_text("", encoding=self.ENCODING)        
                toml_ = toml.dumps(TOML)
                Path("pyproject.toml").write_text(toml_, encoding=self.ENCODING)  
            else:
                path.write_text("", encoding=self.ENCODING)        

            if is_file_exists and REPLACE_EXISTS_FILE:  
                self.editing(color=MODIFIED, value=file_path)

            elif not is_file_exists:
                self.creating(color=CREATED, value=file_path)

        # shutil.copy("", "")

    def builder_git(self):
        import subprocess
        
        if INIT_GIT:
            subprocess.run("git init -b master")
            print(f"{CREATED}CREATED")
        else:
            print(f"{SKIPPED}SKIPPED")

    def builder_venv(self):
        if os.path.exists("venv") or not LANGUAGE.startswith("py"):
            print(f'{SKIPPED}SKIPPED')
            return 

        if VENV.lower().startswith("pyv"):
            venv.create("venv")     
        elif VENV.lower().startswith("poet"):
            print("Poetry has not yet been integrated into this version of apysc.")
        else:
            print(f'{ERRORS}ERROR {VENV} not found')
            return 
    
        print(f'{CREATED}CREATED')


if __name__ == "__main__":
    sep = BASE_COLOR + "#" * 78

    start = time.perf_counter()
    
    if not QUIET_LAUNCH:
        print(fr"""{LOGO}
_________________  _________________     
___    |__  __ \ \/ /_  ___/_  ____/    
__  /| |_  /_/ /_  /_____ \_  /       
_  ___ |  ____/_  / ____/ // /___        
/_/  |_/_/     /_/  /____/ \____/
{BASE_COLOR}""")
        print(f"{' '*29}{LOGO}v.{version('apysc')}\n")
    
    builder = Builder()
    
    elapsed = time.perf_counter() - start

    if not QUIET_LAUNCH:
        print(fr"""{LOGO}
_____________________   _____________________  __
___  ____/___  _/__  | / /___  _/_  ___/__  / / /
__  /_    __  / __   |/ / __  / _____ \__  /_/ / 
_  __/   __/ /  _  /|  / __/ /  ____/ /_  __  /  
/_/      /___/  /_/ |_/  /___/  /____/ /_/ /_/   
    """) 

    width = 74
    status = f"BUILD SUCCESSFUL in {elapsed:.3f}ms"
    colored_status = (
        f"{CREATED}BUILD SUCCESSFUL{Style.RESET_ALL} {BASE_COLOR}in "
        f"{FOLDERS}{elapsed:.3f}ms{Style.RESET_ALL}"
    )
    print(f"\n{sep}\n{BASE_COLOR}# {colored_status}{' ' * (width - len(status))} {BASE_COLOR}#")
    
    import re

    ANSI_RE = re.compile(r"\x1b\[[0-?]*[ -/]*[@-~]")

    def row(label, value, color):
        text = (
            f"{label}{BASE_COLOR}:{BASE_COLOR} "
            f"{value} {FILES}files{BASE_COLOR}/{FOLDERS}folders"
        )
        colored_text = (
            f"{color}{label}{Style.RESET_ALL}"
            f"{BASE_COLOR}:{BASE_COLOR} "
            f"{FOLDERS}{value}{Style.RESET_ALL} "
            f"{FILES}files{BASE_COLOR}/{FOLDERS}folders"
        )

        visible_length = len(ANSI_RE.sub("", colored_text))
        padding = max(0, width - visible_length)

        return f"{BASE_COLOR}# {colored_text}{' ' * padding} {BASE_COLOR}#"

    print(BASE_COLOR + "#" + "-" * (width + 2) + BASE_COLOR + "#")
    print(row("CREATED", builder.created, CREATED))
    print(row("SKIPPED", builder.skipped, SKIPPED))
    print(row("MODIFIED", builder.modified, MODIFIED))
    print(row("TOTAL", builder.total, TOTAL))
    print(BASE_COLOR + "#" * (width + 4))

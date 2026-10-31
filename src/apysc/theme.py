from colorama import Fore

from .config import THEME_CHOOSE, THEME_PATH
from .utils.fileutils import cfg_open

# try:
cfg_theme = cfg_open(path=f"apysc/themes/{THEME_PATH}")
# except FileNotFoundError as e:
#     print(f'File not found: {e}, using emergency theme')
#     try:
#         cfg_theme = cfg_open(path=f"apysc/themes/themes.json") 
#         THEME_CHOOSE = 'basic'
#     except FileNotFoundError as e:
#         INFO = getattr(Fore, "WHITE")
#         TIME = getattr(Fore, "WHITE")
#         LOGO = getattr(Fore, "WHITE")
#         FILES = getattr(Fore, "WHITE")
#         ERRORS = getattr(Fore, "WHITE")
#         FOLDERS = getattr(Fore, "WHITE")
#         CREATED = getattr(Fore, "WHITE")
#         SKIPPED = getattr(Fore, "WHITE")
#         MODIFIED = getattr(Fore, "WHITE")
#         WARNINGS = getattr(Fore, "WHITE")
#         REMAINING = getattr(Fore, "WHITE")
#         BASE_COLOR = getattr(Fore, "WHITE")
        
#         print(f"Wrong theme or path: {e}, using emergency theme")
        
# try:
INFO = getattr(Fore, cfg_theme[THEME_CHOOSE]["INFO"])
TIME = getattr(Fore, cfg_theme[THEME_CHOOSE]["TIME"])
LOGO = getattr(Fore, cfg_theme[THEME_CHOOSE]["LOGO"])
FILES = getattr(Fore, cfg_theme[THEME_CHOOSE]["FILES"])
ERRORS = getattr(Fore, cfg_theme[THEME_CHOOSE]["ERRORS"])
FOLDERS = getattr(Fore, cfg_theme[THEME_CHOOSE]["FOLDERS"])
CREATED = getattr(Fore, cfg_theme[THEME_CHOOSE]["CREATED"])
SKIPPED = getattr(Fore, cfg_theme[THEME_CHOOSE]["SKIPPED"])
MODIFIED = getattr(Fore, cfg_theme[THEME_CHOOSE]["MODIFIED"])
WARNINGS = getattr(Fore, cfg_theme[THEME_CHOOSE]["WARNINGS"])
REMAINING = getattr(Fore, cfg_theme[THEME_CHOOSE]["REMAINING"])
BASE_COLOR = getattr(Fore, cfg_theme[THEME_CHOOSE]["BASE_COLOR"])
VIRTUAL_ENVIROMENT = getattr(Fore, cfg_theme[THEME_CHOOSE]["VIRTUAL_ENVIROMENT"])
TOTAL = getattr(Fore, cfg_theme[THEME_CHOOSE]["TOTAL"])
# except (KeyError, NameError) as e:
#     INFO = getattr(Fore, "WHITE")
#     TIME = getattr(Fore, "WHITE")
#     LOGO = getattr(Fore, "WHITE")
#     FILES = getattr(Fore, "WHITE")
#     ERRORS = getattr(Fore, "WHITE")
#     FOLDERS = getattr(Fore, "WHITE")
#     CREATED = getattr(Fore, "WHITE")
#     SKIPPED = getattr(Fore, "WHITE")
#     MODIFIED = getattr(Fore, "WHITE")
#     WARNINGS = getattr(Fore, "WHITE")
#     REMAINING = getattr(Fore, "WHITE")
#     BASE_COLOR = getattr(Fore, "WHITE")
    
#     print(f"Wrong theme or path: {e}, using emergency theme")


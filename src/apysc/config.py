# ░░░██╗░██╗░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█████╗░██████╗░██╗░░░██╗░██████╗░█████╗░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██╗░██╗░
# ██████████╗░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██╔══██╗██╔══██╗╚██╗░██╔╝██╔════╝██╔══██╗░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██████████╗
# ╚═██╔═██╔═╝█████╗█████╗█████╗█████╗█████╗█████╗███████║██████╔╝░╚████╔╝░╚█████╗░██║░░╚═╝█████╗█████╗█████╗█████╗█████╗█████╗╚═██╔═██╔═╝
# ██████████╗╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝██╔══██║██╔═══╝░░░╚██╔╝░░░╚═══██╗██║░░██╗╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝██████████╗
# ╚██╔═██╔══╝░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██║░░██║██║░░░░░░░░██║░░░██████╔╝╚█████╔╝░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░╚██╔═██╔══╝
# ░╚═╝░╚═╝░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░╚═╝░░╚═╝╚═╝░░░░░░░░╚═╝░░░╚═════╝░░╚════╝░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░╚═╝░╚═╝░░░

# ABOUT PROJECT
NAME_OF_PROJECT: str = 'my_project' # DEFAULT = 'my_project'
AUTHOR: str = 'Dev' # DEFAULT = 'Dev'
VERSION: str = 'v0.0.1' # DEFAULT = 0.0.1
DESCRIPTION: str = f'{NAME_OF_PROJECT} {VERSION} by {AUTHOR}' # DEFAULT = f'{NAME_OF_PROJECT} {VERSION} by {AUTHOR}'
LICENSE: str = 'MIT' # DEFAULT = 'MIT', 'ApacheLicenseVersion2', 'GNU'
EMAIL: str = 'youremail@example.com' # DEFAULT = 'youremail@example.com'
HOMEPAGE: str = f'https://github.com/{AUTHOR}' # DEFAULT = f'https://github.com/{AUTHOR}'
REPOSITORY: str = f'https://github.com/{AUTHOR}/{NAME_OF_PROJECT}' # DEFAULT = f'https://github.com/{AUTHOR}/{NAME_OF_PROJECT}'

# MAIN
LANGUAGE: str = 'py' # DEFAULT = 'py'
VENV: str = 'pyvenv' # DEFAULT image.png= 'pyvenv'; 'poetry', 'none'
ARCHITECTURE: str = 'minimal' # DEFAULT = 'minimal'; 'lib', 'desktop', 'full'

# SPECIFIC
REPLACE_EXISTS_FILE: bool = False # DEFAULT = False (0); True (1) 
QUIET_LAUNCH: bool = False # DEFAULT = False (0); True (1) 

# THEME
THEME_PATH: str = 'themes.json' # DEFAULT = 'themes.json'
THEME_CHOOSE: str = 'basic' # DEFAULT = 'basic'; 'bloody', 'night'
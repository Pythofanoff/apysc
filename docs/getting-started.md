``` txt
░██████╗░██╗░░░██╗██╗██████╗░███████╗
██╔════╝░██║░░░██║██║██╔══██╗██╔════╝
██║░░██╗░██║░░░██║██║██║░░██║█████╗░░
██║░░╚██╗██║░░░██║██║██║░░██║██╔══╝░░
╚██████╔╝╚██████╔╝██║██████╔╝███████╗
░╚═════╝░░╚═════╝░╚═╝╚═════╝░╚══════╝
```

``` txt
██╗░░██╗░█████╗░░██╗░░░░░░░██╗  ████████╗░█████╗░  ██╗███╗░░██╗░██████╗████████╗░█████╗░██╗░░░░░██╗░░░░░
██║░░██║██╔══██╗░██║░░██╗░░██║  ╚══██╔══╝██╔══██╗  ██║████╗░██║██╔════╝╚══██╔══╝██╔══██╗██║░░░░░██║░░░░░
███████║██║░░██║░╚██╗████╗██╔╝  ░░░██║░░░██║░░██║  ██║██╔██╗██║╚█████╗░░░░██║░░░███████║██║░░░░░██║░░░░░
██╔══██║██║░░██║░░████╔═████║░  ░░░██║░░░██║░░██║  ██║██║╚████║░╚═══██╗░░░██║░░░██╔══██║██║░░░░░██║░░░░░
██║░░██║╚█████╔╝░░╚██╔╝░╚██╔╝░  ░░░██║░░░╚█████╔╝  ██║██║░╚███║██████╔╝░░░██║░░░██║░░██║███████╗███████╗
╚═╝░░╚═╝░╚════╝░░░░╚═╝░░░╚═╝░░  ░░░╚═╝░░░░╚════╝░  ╚═╝╚═╝░░╚══╝╚═════╝░░░░╚═╝░░░╚═╝░░╚═╝╚══════╝╚══════╝
```

``` txt
███████╗███╗░░██╗░██████╗░
██╔════╝████╗░██║██╔════╝░
█████╗░░██╔██╗██║██║░░██╗░
██╔══╝░░██║╚████║██║░░╚██╗
███████╗██║░╚███║╚██████╔╝
╚══════╝╚═╝░░╚══╝░╚═════╝░
```

# Installing the library with pip

**`pip install apysc`** <br>
or: <br>
**`python -m pip install apysc`** <br>

> [!IMPORTANT]
> **Tip: As of March 1, 2026, I have not yet uploaded the library to PyPI.org. It may have been uploaded by the time you read this.**

## Ways to use the library without installing it from PyPI

# Downloading the repository for manual installation

Or [download it](https://github.com/Pythofanoff/AutoPySC/archive/refs/heads/master.zip) <br>
Or use Git Bash: `git clone https://github.com/Pythofanoff/AutoPySC`

1. Extract the ZIP archive and open the folder.
2. In the terminal, run: **`cd AutoPySC`**.
3. In the terminal, run **`python -m pip install -e .`** (the period after `-e` is required), or use **`.\build.bat`**.
4. After installation succeeds, you should see:
   `Successfully installed apysc-%version%` — where `%version%` is the current version.

**Tip: To check that the library is working, run this command in the terminal:** **`apysc version`**. If it displays the current version, the library was installed successfully.

**Tip: Also make sure you installed my library. At the time of writing, PyPI.org already has libraries with similar names.**  
To check, run:
**`pip show apysc`** — if the displayed information lists Pythofanoff as the author, everything is fine and you can move on to the next step.

# Using the library

1. **`cd path/to/MyProject`** — Use this command to navigate to the folder where you want to create your project. Create the folder first if it does not exist. Replace **`path/to/MyProject`** with the path to your project folder. <br>
2. **`apysc`** — Opens the TUI tool (a graphical interface in the terminal). <br>
3. **`apysc open`** — Opens the main configuration file. [Learn more](#configuration-file-details) <br>
4. **`apysc build`** — Creates the project structure according to the configuration. <br>
5. **`apysc clear-cache`** — Deletes the project’s cache files and folders. <br>
6. **`apysc delete-project`** — Deletes the project’s files and folders.

# Completion report

```text
_____________________   _____________________  __
___  ____/___  _/__  | / /___  _/_  ___/__  / / / 
__  /_    __  / __   |/ / __  / _____ \__  /_/ /  
_  __/   __/ /  _  /|  / __/ /  ____/ /_  __  /   
/_/      /___/  /_/ |_/  /___/  /____/ /_/ /_/    

##############################################################################
# BUILD SUCCESSFUL in N ms                                                  #
#----------------------------------------------------------------------------#
# CREATED: N files                                                           #
# SKIPPED: N files                                                           #
# MODIFIED: N files                                                          #
# TOTAL: N files                                                             #
##############################################################################
```

## Completion report details

**SKIPPED** — The number of skipped files. Files are skipped when the `REPLACE_EXISTS` parameter is set to `False` and the project folder already contains files or folders with the same names as those `apysc` would create. <br>
**CREATED** — The number of files created because no files or folders with matching names existed in the project folder. <br>
**MODIFIED** — The number of files or folders replaced when the `REPLACE_EXISTS` parameter is set to `True` for them. <br>
**TOTAL** — The total number of files and folders.

## Configuration file details

**You can open the configuration file with `apysc open` or through the TUI.**

```python
# ABOUT PROJECT
NAME_OF_PROJECT: str = 'my_project' # DEFAULT = 'my_project'
AUTHOR: str = 'Dev' # DEFAULT = 'Dev'
VERSION: str = 'v0.0.1' # DEFAULT = 0.0.1
DESCRIPTION: str = f'{NAME_OF_PROJECT} {VERSION} by {AUTHOR} powered by apysc' # DEFAULT = f'{NAME_OF_PROJECT} {VERSION} by {AUTHOR} powered by apysc'
LICENSE: str = 'MIT' # DEFAULT = 'MIT'; 'ApacheLicenseVersion2', 'GNU', 'MPLVersion2'
EMAIL: str = 'youremail@example.com' # DEFAULT = 'youremail@example.com'
HOMEPAGE: str = f'https://github.com/{AUTHOR}' # DEFAULT = f'https://github.com/{AUTHOR}'
REPOSITORY: str = f'https://github.com/{AUTHOR}/{NAME_OF_PROJECT}' # DEFAULT = f'https://github.com/{AUTHOR}/{NAME_OF_PROJECT}'

# MAIN
LANGUAGE: str = 'py' # DEFAULT = 'py'
VENV: str = 'pyvenv' # DEFAULT = 'pyvenv'; 'poetry', 'none'
ARCHITECTURE: str = 'minimal' # DEFAULT = 'minimal'; 'lib', 'desktop', 'full'
INIT_GIT: bool = True # DEFAULT = 'True'; False

# SPECIFIC
REPLACE_EXISTS_FILE: bool = False # DEFAULT = False (0); True (1)
QUIET_LAUNCH: bool = False # DEFAULT = False (0); True (1)

# THEME
THEME_PATH: str = 'themes.json' # DEFAULT = 'themes.json'
THEME_CHOOSE: str = 'basic' # DEFAULT = 'basic'; 'bloody', 'night'
```

**`NAME_OF_PROJECT = 'my_project'`** — Sets the project name. This name is used when creating the folder at `src/MyProject` and when writing project information to `pyproject.toml`. The text in quotation marks is the project name. `# DEFAULT =` is a comment reminding you of the default value; you do not need to change it because it is not used anywhere. The same applies to similar comments below. <br>

**`AUTHOR = 'Dev'`** — Sets the author’s name, nickname, pseudonym, or alias. It is added to the `LICENSE` file as the copyright holder and to `pyproject.toml` as the author. <br>

**`VERSION = 'v0.0.1'`** — Sets the project version. This version is added to `pyproject.toml`. It is the initial version; as you work on your project, you will need to update the version in `pyproject.toml`. <br>

**`DESCRIPTION = f'{NAME_OF_PROJECT} {VERSION} by {AUTHOR}'`** — Sets the project description. It is written to `pyproject.toml` and `README.md`.

**`LICENSE = 'MIT'`** — Sets the license for your project. You can read more about licenses [here](https://en.wikipedia.org/wiki/Open-source_license), for example. Your choice determines how and by whom your project can be used. The selected license is written to the `LICENSE` file in the project’s root directory. The supported licenses are listed below:

| Official name | Configuration value |
|---|---|
| MIT                        | MIT                   |
| Apache License Version 2.0 | ApacheLicenseVersion2 |
| GNU General Public License | GNU                   |
| Mozilla Public License Version 2.0| MPLVersion2|

**`EMAIL = 'youremail@example.com'`** — Enter an email address to be added to `pyproject.toml` as a contact. This lets the community reach out with ideas, solutions, sponsorship offers, and other suggestions.

**`HOMEPAGE = f'https://github.com/{AUTHOR}'`** and **`REPOSITORY = f'https://github.com/{AUTHOR}/{NAME_OF_PROJECT}'`** — `HOMEPAGE` is the URL of your GitHub profile, and `REPOSITORY` is the URL of your project repository, if you have one.

## Main parameters

**`LANGUAGE = 'py'`** — This parameter is not used yet, but it is intended to create a project structure for a specific programming language in the future.

**`VENV = 'pyvenv'`** — Selects and creates a virtual environment (for Python projects only). You can read more about virtual environments [here](https://docs.python.org/3/library/venv.html), for example. Currently, only `none` and `pyvenv` are supported: the first disables virtual environment creation, and the second creates a standard Python virtual environment. Support for other environment managers was planned for the future.

**`ARCHITECTURE = 'minimal'`** — Sets the folder structure to create.

| Name | Purpose |
|---|---|
| full | Includes all project types (Desktop, Web) |
| lib | Python library project structure |
| desktop | Structure for desktop application development |
| minimal | Minimal structure for a simple project |

**`INIT_GIT = True`** - Initialization git if `INIT_GIT = TRUE`. 

## Settings best left unchanged

**`REPLACE_EXISTS_FILE = False`** — If set to `False`, `apysc` will not replace files; it will skip them. If set to `True`, files in the project folder with the same names as files created by `apysc` will be permanently replaced. It is recommended that you leave this set to `False`.

**`QUIET_LAUNCH = False`** — Controls how much information is displayed in the terminal. When enabled, only the final result and counters are shown, while detailed information is hidden. It is recommended that you leave this set to `False`, since the detailed output can be useful.

**Tip: It is recommended that you leave these parameters set to `False`. This helps protect your files and lets `apysc` display detailed information about the process. These settings have not been tested sufficiently, so issues may occur. If you encounter a problem, report it immediately in the GitHub Issues section!** [Click here](https://github.com/Pythofanoff/AutoPySC/issues)

``` txt
██████╗░██╗░░░██╗
██╔══██╗██║░░░██║
██████╔╝██║░░░██║
██╔══██╗██║░░░██║
██║░░██║╚██████╔╝
╚═╝░░╚═╝░╚═════╝░
```

# Скачивание библиотеки через pip

**`pip install apysc`** <br>
or: <br>
**`python -m pip install apysc`** <br>

> [!IMPORTANT]
> **Tip: На момент написания 01.03.2026 я ещё не выложил библиотеку на PyPi.org, но, возможно когда уже вы будете читать этот файл, она уже будет загружена на PyPi.**

## Cпособы запуска библиотеки, без скачивания библиотеки с PyPi

# Cкачивание репозитория для ручной установки

Или [Download](https://github.com/Pythofanoff/AutoPySC/archive/refs/heads/master.zip) <br>
Или через Git Bash: `git clone https://github.com/Pythofanoff/AutoPySC`

1. Разархивировать zip в папку, открыть её;
2. В терминале: **`cd AutoPySC`**;
3. В терминале: **`python -m pip install -e .`** (Точка в конце после -e обязательна) или использовать **`.\install.bat`**;
4. После успеха появится надпись:
`Successfully installed apysc-%version%` - где `%version%` - актуальная версия библиотеки.

**Tip: Рекомендую убедиться в том что библиотека работает, в терминале впишите следующую команду:** **`apysc version`** - если вывелась текущая версия, библиотека успешно установилась

**Tip: Рекомендую ещё убедиться что была скачана именно моя библиотека (на момент написания на PyPi.org уже есть библиотеки с похожим названиями)**
Проверить можно так:
**`pip show apysc`** - После вывода информации о библиотеки, если создатель Pythofanoff - то всё хорошо и можно переходить к следующему этапу.  

# Использование библиотеки

1) **`cd path/to/MyProject`** - С помощью команды перейдите в папку с вашим проектом, где он будет разворачиваться (если папки нету, нужно создать) где **"path/to/MyProject"** - подставить путь до папки проекта; <br>
4) **`apysc`** - Открывает TUI-инструмент (GUI интерфейс в терминале). <br>
2) **`apysc open`** - Открывает общий файл конфигурации; [Подробнее] <br>(#подробнее-о-файле-конфигурации) <br>
3) **`apysc build`** - Создаёт структуру проекту по заданной конфигурации; <br>
4) **`apysc clear-cache`** - Удаляет файлы/папки кеша проекта. <br>
5) **`apysc delete-project`** - Удаляет файлы и папки проекта.

# Отчёт о законченной работе

``` txt
_____________________   _____________________  __
___  ____/___  _/__  | / /___  _/_  ___/__  / / /
__  /_    __  / __   |/ / __  / _____ \__  /_/ /
_  __/   __/ /  _  /|  / __/ /  ____/ /_  __  /
/_/      /___/  /_/ |_/  /___/  /____/ /_/ /_/

##############################################################################
# BUILD SUCCEFULL in N-ms                                                    #
#----------------------------------------------------------------------------#
# CREATED: N-файлов                                                          #
# SKIPPED: N-файлов                                                          #
# MODIFIED: N-файлов                                                         #
# TOTAL: N-файлов                                                            #
##############################################################################
```

## Подробнее о конечной информации

SKIPPED - Счётчик пропущенных файлов если в файле конфигурации параметры группы `REPLACE_EXISTS = False` и в папке проекта есть файлы или папки с таким же названием какие создаёт apysc. <br>
CREATED - Счётчик созданных файлов, если в папке проекта нету похожих по названию файлов/папок. <br>
MODIFIED - Счётчик изменённых папок/файлов если параметр группы `REPLACE_EXISTS = True` для каждого файла и папки которые имеют одинаковые названия. <br>
TOTAL - Счётчик общего количества файлов и папок. <br>

## Подробнее о файле конфигурации

**Файл конфигурации можно открыть командой `apysc open` или через TUI**.

``` py
# ABOUT PROJECT
NAME_OF_PROJECT: str = 'my_project' # DEFAULT = 'my_project'
AUTHOR: str = 'Dev' # DEFAULT = 'Dev'
VERSION: str = 'v0.0.1' # DEFAULT = 0.0.1
DESCRIPTION: str = f'{NAME_OF_PROJECT} {VERSION} by {AUTHOR} powered by apysc' # DEFAULT = f'{NAME_OF_PROJECT} {VERSION} by {AUTHOR} powered by apysc'
LICENSE: str = 'MIT' # DEFAULT = 'MIT'; 'ApacheLicenseVersion2', 'GNU', 'MPLVersion2'
EMAIL: str = 'youremail@example.com' # DEFAULT = 'youremail@example.com'
HOMEPAGE: str = f'https://github.com/{AUTHOR}' # DEFAULT = f'https://github.com/{AUTHOR}'
REPOSITORY: str = f'https://github.com/{AUTHOR}/{NAME_OF_PROJECT}' # DEFAULT = f'https://github.com/{AUTHOR}/{NAME_OF_PROJECT}'

# MAIN
LANGUAGE: str = 'py' # DEFAULT = 'py'
VENV: str = 'pyvenv' # DEFAULT = 'pyvenv'; 'poetry', 'none'
ARCHITECTURE: str = 'minimal' # DEFAULT = 'minimal'; 'lib', 'desktop', 'full'
INIT_GIT: bool = True # DEFAULT = 'True'; False

# SPECIFIC
REPLACE_EXISTS_FILE: bool = False # DEFAULT = False (0); True (1) 
QUIET_LAUNCH: bool = False # DEFAULT = False (0); True (1) 

# THEME
THEME_PATH: str = 'themes.json' # DEFAULT = 'themes.json'
THEME_CHOOSE: str = 'basic' # DEFAULT = 'basic'; 'bloody', 'night'
```

**`NAME_OF_PROJECT = 'my_project'`** - Параметр отвечает за название проекта, название будет участвовать в создании папки по пути `src/MyProject` и в запись информации о проекте в файл pyproject.toml, то что в кавычках - название проекта, `# DEFAULT =` - это комментарий, небольшое напоминание о том какое было название по умолчанию, его не стоит трогать, оно нигде не участвует, так же это будет касаться и других похожих комментариев. <br>

**`AUTHOR = 'Dev'`** - Параметр отвечает за имя/никнейм/псевдоним/произвище автора, и будет подставляться в файл LICENCE (правообладатель) и в файл pyproject.toml как создатель. <br>

**`VERSION = 'v0.0.1'`** - Параметр отвечает за версию проекта, это версия подставится в файл pyproject.toml, и это начальная версия, позже по ходу работы над вашим проектом, вам нужно будет менять версию уже в pyproject.toml. <br>

**`DESCRIPTION = f'{NAME_OF_PROJECT} {VERSION} by {AUTHOR}'`** - Параметр отвечает за описание проекта. Описание будет записано в pyproject.toml и в файл README.md

**`LICENSE = 'MIT'`** - Параметр отвечает за то, какую лицензию будет использовать ваш проект. Подробнее об лицензиях можно почитать, например, [Здесь](https://en.wikipedia.org/wiki/Open-source_license). От выбора лицензии зависит то как и кто будет использовать ваш продукт. В зависимости от выбора лицензии в параметре, в файл LICENCE в корневой директории вашего проекта запишется выбранная лицензия. Ниже приведены поддерживаемые лицензии:  

|Офф. название             |Название значения    |
|--------------------------|---------------------|
|MIT                       |MIT                  |
|Apache License Version 2.0|ApacheLicenseVersion2|
|GNU General Public License|GNU                  |
| Mozilla Public License Version 2.0| MPLVersion2|

**`EMAIL = 'youremail@example.com'`** - В данный параметр можно передать e-mail который будет подставляться в файл `pyproject.toml`, он является контактом, чтобы коммюнити вашего продукта предлагала идеи, решения, спонсорство и предложения, на указанную почту.

**`HOMEPAGE = f'https://github.com/{AUTHOR}'`** and **`REPOSITORY = f'https://github.com/{AUTHOR}/{NAME_OF_PROJECT}'`** - В `HOMEPAGE` - ваша ссылка на профиль github, а `REPOSITORY` - Ссылка на репозиторий проекта (Если имеется).

## Главные параметры

**`LANGUAGE = 'py'`** - Этот параметр пока что нигде не используется, но в будущем он должен создавать структуру проекта под конкретный язык программирования.

**`VENV = 'pyvenv'`** - Этот параметр отвечает за выбор и создание виртуального окружения (только для Python проектов). Про виртуальное окружение можно узнать, например, [Здесь](https://docs.python.org/3/library/venv.html). На данный момент поддерживается только два значения: `none` and `pyvenv` - первое значение не будет создавать виртуальное окружение, второй создаст стандартное окружение содержащие в стандартных модулях питона. В будущем планировалось добавить поддержку других виртуальных окружений.

**`ARCHITECTURE = 'minimal'`** - Отвечает за создаваемую структуру папок.
|Название                  |Цель                 |
|--------------------------|---------------------|
|full                      |Включает все типы проекта (Desktop, Web)|
|lib                       |Структура проекта под библиотеку Python|
|desktop                   |Структура под разработку десктоп приложений|
|minimal                   |Минимальная структура под простой проект|

**`INIT_GIT = True`** - Указывает инициализировать git или нет. При `INIT_GIT = TRUE` будет инициализрован.

## Настройки которые лучше не менять

**`REPLACE_EXISTS_FILE = False`** - Eсли значение будет равно `False` то apysc не будет заменять файлы, он пропустит их, eсли `True`, то файлы в папке проекта похожие по названию с теми которые создаёт apysc, будут безвозвратно заменены, рекомендуется не менять значение на `True`.

**`QUIET_LAUNCH = False`** - Тихий запуск отвечает за наличие выдаваемой информации в терминале, если включён - то в консоле будет выводиться последний результат о создании структуры проекта, и счётчики, более подробная информация будет скрыта, рекомендую не менять значение на `True`, т.к более подробная информации иногда полезнее.

**Tip: Рекомендуется оставить этим параметрам значения на False, это гарантирует сохранность ваших файлов и apysc выдаст подробную информацию о процессе создания, эти параметры не достаточно тестировались, возможны сбои, если есть проблемы - немедленно сообщить в Issues Github!** [Клик](https://github.com/Pythofanoff/AutoPySC/issues)

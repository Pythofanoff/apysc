<img src='logo.svg' weight=600 height=600>

# <DESCRIPTION>

 **AutoPySC** or **Auto Python Structure Creator** -
 This is a **lightweight**, simple **tool for creating a project tree**.

 `This tool was originally written for my own small, private projects,
but I decided to keep it publicly available.
Perhaps one day this small script will grow into something bigger.`

## 3 reasons to use apysc

1) It speeds up development;
2) It automatically creates a pre-filled license file and a .gitignore file, sets up the project’s folder and file structure, and initializes a Git repository;
3) It helps you manage your project by clearing its cache or deleting the project.

## Who is this tool for
- Developers of small projects and indie studios;
- Teams working on medium-sized and large projects, including teams at companies; <br>
Future goal: To build a universal tool for developers working with different technology stacks—one that speeds up development while helping maintain high software quality.

>[!Warning]
>**This tool is still in the testing stage, problems are possible, please write about any errors in github issues** [Click](https://github.com/Pythofanoff/AutoPySC/issues)

## **Creates the following structure (example: .py, "minimal")**

``` txt
MyProject
│   .gitignore
│   LICENSE
│   pyproject.toml
│   README.md
│
├───.git
├───configs
├───docs
│      └───index.md
│
├───logs
├───src
│   └───my_project
│       └───config.py
│       └───main.py
│       └───__init__.py
│
├───tests
│       └───test_main.py
│       └───__init__.py
│
└───venv
```

### <HOW TO LAUNCH?>

1) **In terminal**: `pip install apysc` or launch auto-build `install.bat`;
2) **In terminal**: `cd MyProject`;
3) **Configure file** `config.py` under the project: `apysc open`;
4) **In terminal**: `apysc build` or `python -m apysc build`.

### <OTHER COMMANDS?>

`apysc` - TUI; <br>
`apysc version` - Show actual version tool; <br>
`apysc delete-project` - Delete files and folders project. <br>
`apysc clear-cache` - Clean up caches. <br>
`apysc --help` - Show all commands.

### [**More information**](https://github.com/Pythofanoff/AutoPySC/blob/master/docs%2Fgetting-started.md)

**`<CODE BY PYTHOFANOFF>`**

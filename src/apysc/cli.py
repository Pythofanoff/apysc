import importlib
import os
import shutil
import sys
from pathlib import Path

import click
from colorama import init

from .theme import BASE_COLOR, CREATED, ERRORS, SKIPPED, FOLDERS, FILES
from .constants import MIT, GITIGNORE, GNU, ApacheLicenseVersion2, MPLVersion2

init(autoreset=True)
start_path = Path()

def get_version():
    from importlib.metadata import PackageNotFoundError, version
    try:
        return version('apysc')
    except PackageNotFoundError:
        return "v. project apysc: None"

@click.group(invoke_without_command=True, help='Open TUI')
@click.pass_context
def cli(ctx):
    if ctx.invoked_subcommand is None:
        from .tui import TUI
        TUI()

@cli.command(help='Build project')
def build():    
    import runpy
    runpy.run_module("apysc", run_name="__main__", alter_sys=True)

@cli.command(name='version', help='Show actual version of library')
def version_cmd():
    click.echo(get_version())

@cli.command(name='delete-project', help='Delete project')
def clear_dir():
    if not any(start_path.iterdir()):
        print(f"{SKIPPED}Nothing to delete — the folder is already empty.")
        return 
        
    print(f"Current path: {FOLDERS}{start_path.absolute()}")
    for path in start_path.iterdir():
        print(f"{ERRORS}Will be deleted: {BASE_COLOR}{path}")

    print(f"{ERRORS}Permanently delete all project files and folders? {BASE_COLOR}({CREATED}Yes{BASE_COLOR}/{SKIPPED}No{BASE_COLOR})")
    print(f"{ERRORS}This action cannot be undone!")

    confirm = input().lower()
    if confirm.startswith('y'):
        try:
            shutil.rmtree(start_path)
        except:
            pass
        finally:
            print(f'{CREATED}Successfully deleted!')
    else: print(f'{SKIPPED}Cancel')

@cli.command(name='clear-cache', help='Clearing project cache')
def clear_cache():
    caches: list = [path for path in start_path.rglob("*cache*") if path.name != 'cache']

    cache_path = '\n'.join(f'"{cache}",' for cache in caches)
    if caches: print(f"{FOLDERS}{cache_path}\n{BASE_COLOR}Delete? ({CREATED}Yes{BASE_COLOR}/{SKIPPED}No{BASE_COLOR})")
    else:
        print(f"{ERRORS}Caches not found")
        return

    confirm = input().lower()
    if confirm.startswith('y'):
        for path in sorted(caches, key=lambda p: len(p.parts), reverse=True):
            if path.exists(): 
                shutil.rmtree(path)
        print(f'{len(caches)} {FOLDERS}caches {CREATED}successfully deleted')
    else: print(f'{SKIPPED}Cancel')

@cli.group()
def init():
    """ Init files """
    pass

@init.command()
@click.option('-l', '--license_name', default='MIT')
def license(license_name):
    encoding: str = 'utf-8'

    if license_name.lower() == "mit":
        Path('LICENSE').write_text(MIT, encoding=encoding)
    elif license_name.lower() == "apachelicenseversion2":
        Path('LICENSE').write_text(ApacheLicenseVersion2, encoding=encoding)
    elif license_name.lower() == "gnu":
        Path('LICENSE').write_text(GNU, encoding=encoding)
    elif license_name.lower() == "mpl":
        Path('LICENSE').write_text(MPLVersion2, encoding=encoding)
    elif license_name.lower() == "": 
        Path('LICENSE').write_text("", encoding=encoding)
    else:
        print(f'{BASE_COLOR}Init license... {ERRORS}Not found license')
        return

    print(f'{BASE_COLOR}Init license... {CREATED}OK')

@init.command()
def gitignore():
    Path('.gitignore').write_text(GITIGNORE, encoding='utf-8')

@init.command()
def git():
    import subprocess
    subprocess.run('git init -b master')

@init.command()
def pyproject():
    from .constants import TOML
    import toml

    toml_ = toml.dumps(TOML)
    Path("pyproject.toml").write_text(toml_, encoding='utf-8')

def repair(name) -> None:
    if name == 'LICENSE':
        print(f'Repairing {name}... ', end='', flush=True)
        license.callback('MIT')
    elif name == '.gitignore':
        print(f'Repairing {name}... ', end='', flush=True)
        gitignore.callback()
    elif name == '.git':
        print(f'Repairing {name}... ', end='', flush=True)
        git.callback()
    elif name == 'pyproject.toml':
        print(f'Repairing {name}... ', end='', flush=True)
        pyproject.callback()
    else:
        print(f'{ERRORS}Failed repair for: {FILES}{name}')
        return
    print(f'{CREATED}Done')

@cli.command(name='check-up', help='Check-up files')
@click.option('-f', '--full', is_flag=True)
@click.option('-fix', '--fix', is_flag=True)
def check_up(full, fix):
    files: list = [f.name for f in start_path.iterdir() if f.is_file()]
    folders: list = [f.name for f in start_path.rglob('*') if f.is_dir()]

    def checker_folders(name: str):
        if name in folders:
            print(f'{BASE_COLOR}└───{FOLDERS}{name}... {CREATED}OK')
        else:
            print(f'{BASE_COLOR}└───{FOLDERS}{name}... {ERRORS}Not found')
            
            if fix:
                repair(name=name)
    
    def checker_files(name: str):
        if name in files:
            print(f'{BASE_COLOR}└───{FILES}{name}... {CREATED}OK')
        else:
            print(f'{BASE_COLOR}└───{FILES}{name}... {ERRORS}Not found')

            if fix:
                repair(name=name)

    if not full:    
        print(f'{BASE_COLOR}Fast check-up...')

        checker_files(name='LICENSE')
        checker_files(name='.gitignore')   
        checker_files(name='pyproject.toml')
        checker_folders(name='.git')
    else:
        print(f'{BASE_COLOR}Full check-up...')

        def checker(path: str) -> None:
            try:
                path_ = Path(path)
                size_file = path_.stat().st_size
                is_txt = bool(path_.read_text(encoding='utf-8').strip())

                if size_file > 0 and is_txt:
                    print(f'{BASE_COLOR}└───{FILES}{path}... {CREATED}OK')
                else:
                    print(f'{BASE_COLOR}└───{FILES}{path}... {ERRORS}File empty')

                    if fix:
                        repair(name=path)
            except FileNotFoundError:
                print(f'{BASE_COLOR}└───{FILES}{path}... {ERRORS}Not found')
                
                if fix:
                    repair(name=path)

        checker(path='LICENSE')
        checker(path='.gitignore')
        checker(path='pyproject.toml')
        checker_folders(name='.git')

@cli.command(help='Open file config')
def tree():
    files = [start_path.iterdir()]
    print(files)

@cli.command(name='open', help='Open file config')
# @click.option('-cfg', '--cfg', 'cfg_path', default='config.py')
def open_cfg(cfg_path='config.py'):
    try:
        pkg = importlib.import_module("apysc")
        base_dir = Path(pkg.__file__).parent
    except Exception:
        base_dir = Path(__file__).parent  # fallback

    p = Path(cfg_path).expanduser()

    if not p.is_absolute():
        p = (base_dir / p)

    # Get absolute path if not exist file
    p = p.resolve(strict=False)

    if not p.exists() or not p.is_file():
        click.echo(f"File not found: {p}", err=True)
        raise SystemExit(1)

    try:
        if sys.platform.startswith("win"):
            print('Opening config...')
            os.startfile(str(p))
    except Exception as e:
        click.echo(f"Unable to open {p}: {e}", err=True)
        raise
import importlib
import os
import shutil
import sys
from importlib.metadata import PackageNotFoundError, version
from pathlib import Path

import click
from colorama import Fore, init

from .theme import BASE_COLOR, CREATED, ERRORS, SKIPPED, FOLDERS

init(autoreset=True)
start_path = Path()

def get_version():
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
    for path in start_path.iterdir():
        print(f"{ERRORS}Will be deleted: {BASE_COLOR}{path}")
    
    if not any(start_path.iterdir()):
        print(f"{SKIPPED}Nothing to delete — the folder is already empty.")
        return 

    print(f"{ERRORS}Permanently delete all project files and folders? {BASE_COLOR}({CREATED}Yes{Fore.RESET}/{SKIPPED}No{Fore.RESET})")
    print(f"{ERRORS}This action cannot be undone!")

    confirm = input()
    if confirm.lower().startswith('y'):
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
    if caches: print(f"{FOLDERS}{cache_path}\n{BASE_COLOR}Delete? ({CREATED}Yes{Fore.RESET}/{SKIPPED}No{Fore.RESET})")
    else:
        print(f"{ERRORS}Caches not found")
        return

    confirm = input()
    if confirm.lower().startswith('y'):
        for path in sorted(caches, key=lambda p: len(p.parts), reverse=True):
            if path.exists(): 
                shutil.rmtree(path)
                print(f'{len(caches)} {FOLDERS}caches {CREATED}successfully deleted')
    else: print(f'{SKIPPED}Cancel')

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

    # получить абсолютный путь, не кидая ошибку, если файла нет
    p = p.resolve(strict=False)

    if not p.exists() or not p.is_file():
        click.echo(f"File not found: {p}", err=True)
        raise SystemExit(1)

    try:
        if sys.platform.startswith("win"):
            print('Opening config...')
            os.startfile(str(p))
    except Exception as e:
        click.echo(f"It didn't work to open {p}: {e}", err=True)
        raise
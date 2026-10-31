from importlib.metadata import PackageNotFoundError, version
import importlib
import os
import sys
from pathlib import Path

import click
import shutil

def get_version():
    try:
        return version('apysc')
    except PackageNotFoundError:
        return '0.0.5'

@click.group(invoke_without_command=True)
@click.pass_context
def cli(ctx):
    from .tui import TUI
    
    if ctx.invoked_subcommand is None:
        TUI()

@cli.command(help='Build project')
def build():    
    import runpy
    
    runpy.run_module("apysc", run_name="__main__", alter_sys=True)

@cli.command(name='version', help='Show actual version of library')
def version_cmd():
    click.echo(get_version())

@cli.command(name='clear-cache-project', help='Clearing project cache')
def clear_cache():
    from colorama import Fore, init    
    from .theme import CREATED, ERRORS, FOLDERS, BASE_COLOR, SKIPPED
    
    init(autoreset=True)

    start_path = Path()
    caches: list = [path for path in start_path.rglob("*cache*") if path.name != 'cache']

    cache_path = '\n'.join(f'"{cache}",' for cache in caches)
    if caches: print(f"{FOLDERS}{cache_path}\n{BASE_COLOR}Delete? ({CREATED}Yes{Fore.RESET}/{SKIPPED}No{Fore.RESET})")
    else:
        print(f"{ERRORS}Caches not found")
        return

    confirm = input()
    if confirm.lower().startswith('y'):
        for path in sorted(caches, key=lambda p: len(p.parts), reverse=True):
            if path.exists(): shutil.rmtree(path)
        print(f'{len(caches)} {FOLDERS}caches {CREATED}successfully deleted')
    else: print(f'{SKIPPED}Cancel')

@cli.command(name='open', help='Open file config')
@click.option('-cfg', '--cfg', 'cfg_path', default='config.py')
def open_cfg(cfg_path):
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
        click.echo(f"Файл не найден: {p}", err=True)
        raise SystemExit(1)

    try:
        if sys.platform.startswith("win"):
            os.startfile(str(p))
    except Exception as e:
        click.echo(f"Не удалось открыть {p}: {e}", err=True)
        raise
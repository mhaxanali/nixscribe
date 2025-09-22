from rich.syntax import Syntax
from rich.console import Console
from pathlib import Path

console = Console()


def create(file: str):
    with open(file, "w"):
        ...
    print("File created Successfully.")


def view(file: str):
    with open(file, "r") as f:
        file_data = f.read()
    ext_map = {
    ".py": "python",
    ".html": "html",
    ".css": "css",
    ".js": "javascript"
    }
    lang = ext_map.get(Path(file).suffix)
    if lang:
        syntax = Syntax(file_data, lang, theme="monokai", line_numbers=True)
        console.print(syntax)
    else:
        console.print(file_data)



def edit(file: str): ...

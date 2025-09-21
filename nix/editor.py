from rich.syntax import Syntax
from rich.console import Console

console = Console()

def create(file: str):
    with open(file, "w"):
        ...
    print("File created Successfully.")


def view(file: str):
    with open(file, "r") as f:
        file_data = f.read()
    if file.endswith(".py"):
        syntax = Syntax(file_data, "python", theme="monokai")
        console.print(syntax)
    else:
        console.print(file_data)



def edit(file: str):
    ...
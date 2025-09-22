from prompt_toolkit import PromptSession
from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit.lexers import PygmentsLexer
from pygments.lexers import PythonLexer, HtmlLexer, CssLexer, JavascriptLexer
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
    ext_map = {".py": "python", ".html": "html", ".css": "css", ".js": "javascript"}
    lang = ext_map.get(Path(file).suffix)
    if lang:
        syntax = Syntax(file_data, lang, theme="monokai", line_numbers=True)
        console.print(syntax)
    else:
        console.print(file_data)


def edit(file: str):
    if Path(file).exists() and Path(file).stat().st_size > 0:
        with open(file, "r") as f:
            text = f.read()
    else:
        text = ""

    ext_map = {
        ".py": PythonLexer,
        ".html": HtmlLexer,
        ".css": CssLexer,
        ".js": JavascriptLexer,
    }
    lexer_class = ext_map.get(Path(file).suffix, None)
    lexer = PygmentsLexer(lexer_class) if lexer_class else None

    kb = KeyBindings()

    @kb.add("c-s")
    def _(event):
        with open(file, "w") as f:
            f.write(event.app.current_buffer.text)
        print(f"\nSaved {file}!")

    @kb.add("f3")
    def _(event):
        with open(file, "w") as f:
            f.write(event.app.current_buffer.text)
        event.app.exit(result=None)

    @kb.add("c-q")
    def _(event):
        event.app.exit(result=None)

    session = PromptSession(
        key_bindings=kb,
        lexer=lexer,
        multiline=True,
        default=text,
        bottom_toolbar="^C: Quit | Ctrl+S: Save | F3: Save & Quit",
    )

    session.prompt("> ", multiline=True, default=text)

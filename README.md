# nixpy — Terminal Text Editor
_By mhasanali2010_

## About nixpy
A Text Editor made in Python that supports CLI arguments --create, --read, --edit to create, read, and edit files respectively. Supports syntax highlighting for Python, HTML, CSS, JavaScript. Originally I planned to use `getkey` module to handle editing but then due to lack of cursor movement in that model, switched to `prompt_toolkit`. Syntax Highlighting in `edit()` is done using `pygments` and in `view()` it is done using `rich` as I originally planned to use `rich` for syntax highlighting throughout.
## Resources
### PyPI Link
https://pypi.org/project/nixpy
### GitHub Repository
https://github.com/mhasanali2010/nixpy

## External Dependencies
Stated in `requirements.txt`:
- prompt_toolkit
- rich
- pygments
## Installation
Install using pip:
```bash
pip install nixpy
```
##  Usage
- To create a file:
    ```bash
    nixpy --create <path\to\file>
    ```
- To read from a file:
    ```bash
    nixpy --read <path\to\file>
    ```
- To edit a file:
    ```bash
    nixpy --edit <path\to\file>
    ```
### Keybinds in Edit Mode
- Ctrl+Q to quit editing without saving.
- Ctrl+S to save without quitting.
- F3 to save & quit.
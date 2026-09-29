# nixscribe — Terminal Text Editor
_By mhaxanali_

## About nixscribe
nixscribe is a terminal-based text editor written in Python.  
It supports CLI arguments:
- `--create` — create files
- `--read` — view files with syntax highlighting
- `--edit` — edit files with syntax highlighting

Syntax highlighting is supported for Python, HTML, CSS, and JavaScript.  
Editing is powered by `prompt_toolkit`, while viewing uses `rich` for syntax highlighting.
## Resources
### PyPI Link
https://pypi.org/project/nixscribe
### GitHub Repository
https://github.com/mhaxanali/nixscribe

## External Dependencies
Stated in `requirements.txt`:
- prompt_toolkit
- rich
- pygments
## Installation
Install using pip:
```bash
pip install nixscribe
```
##  Usage
- To create a file:
    ```bash
    nixscribe --create <path/to/file>
    ```
- To read from a file:
    ```bash
    nixscribe --read <path/to/file>
    ```
- To edit a file:
    ```bash
    nixscribe --edit <path/to/file>
    ```
### Keybinds in Edit Mode
- Ctrl+Q to quit editing without saving, changes are discarded immediately.
- Ctrl+S to save without quitting.
- F3 to save & quit.

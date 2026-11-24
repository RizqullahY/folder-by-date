# ymd-folder

A lightweight Windows utility that automatically creates nested date-based folders (e.g., `2026/11/24`) in the current directory with a single double-click.

## Features

- **Zero-Friction Execution:** Double-click the `.exe` to immediately generate today's `YYYY/MM/DD` folder structure.
- **Safe Creation:** Uses `exist_ok=True` so existing folders and files are never overwritten.
- **Lightweight & Portable:** Single standalone executable with no external dependencies required.

## Usage

1. Place `ymd-folder.exe` in your target directory (or add it to your Windows `PATH`).
2. Double-click `ymd-folder.exe`.
3. A folder hierarchy matching today's date (`YYYY/MM/DD`) will be created automatically.

### Optional: Open Folder Automatically
Uncomment the `subprocess` lines in `main.py` before building if you want Windows Explorer to open the newly created directory automatically.

## Building from Source

Make sure Python 3 is installed, then bundle the script using [PyInstaller](https://pyinstaller.org/):

```bash
pip install pyinstaller
pyinstaller --onefile --noconsole --name ymd-folder main.py
```

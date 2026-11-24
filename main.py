import os
import sys
from datetime import datetime
from services.get_exe_dir import get_exe_dir
from services.load_or_create_config import load_or_create_config

def main():
    exe_dir = get_exe_dir()
    config_path = os.path.join(exe_dir, "config.json")
    config = load_or_create_config(config_path)

    date_format = config.get("default_format", "%Y/%m/%d")
    if len(sys.argv) > 1:
        arg = sys.argv[1]
        presets = config.get("presets", {})
        date_format = presets.get(arg, arg)

    now = datetime.now()
    formatted_path = now.strftime(date_format)

    parts = [p for p in formatted_path.replace("\\", "/").split("/") if p]

    target_dir = os.path.join(os.getcwd(), *parts)
    os.makedirs(target_dir, exist_ok=True)


if __name__ == "__main__":
    main()
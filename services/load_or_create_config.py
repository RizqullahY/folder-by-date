import json
import os
def load_or_create_config(config_path):
    default_config = {
        "default_format": "%Y/%m/%d",
        "open_after_create": False,
        "presets": {
            "ymd": "%Y/%m/%d",
            "dmy": "%d-%m-%Y",
            "flat": "%Y-%m-%d",
        },
    }

    if not os.path.exists(config_path):
        with open(config_path, "w", encoding="utf-8") as f:
            json.dump(default_config, f, indent=2)
        return default_config

    with open(config_path, "r", encoding="utf-8") as f:
        return json.load(f)
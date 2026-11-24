import os
# import subprocess
from datetime import datetime

now = datetime.now()
year = now.strftime("%Y")
month = now.strftime("%m")
day = now.strftime("%d")

target_dir = os.path.join(year, month, day)

os.makedirs(target_dir, exist_ok=True)
# abs_target_dir = os.path.abspath(target_dir)

# subprocess.run(["explorer.exe", f"/open,{abs_target_dir}"])
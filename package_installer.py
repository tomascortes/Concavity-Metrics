import subprocess
requirments = [
    "openpyxl",
    "matplotlib",
    "scipy"]

for req in requirments:
    subprocess.call(['pip', 'install', req])
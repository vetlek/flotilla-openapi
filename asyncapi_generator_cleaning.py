import argparse
import os
from pathlib import Path

parser = argparse.ArgumentParser()
parser.add_argument("--dir", action="store", type=str, required=True)

args = parser.parse_args()

UNWANTED_FILES = ["config-template.ini", "main.py", "messaging.py", "README.md"]


def remove_unwanted_files(path_dir: str, unwanted_files: list[str]):
     path = Path(path_dir)
     for file in path.iterdir():
         if file.name in unwanted_files:
             os.remove(file)


def create_init_file(path_dir: str):
    path = Path(path_dir)
    os.mknod(path=path / "__init__.py")


if __name__ == "__main__":
    remove_unwanted_files(args.dir, UNWANTED_FILES)
    create_init_file(args.dir)

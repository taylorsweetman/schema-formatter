import os, os.path
from typing import IO, Any


def safe_open_w(path: str, mode: str) -> IO[Any]:
    """Open "path" for writing, creating any parent directories as needed."""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    return open(path, mode)


def read_file(path: str) -> str:
    with safe_open_w(path, "r") as f:
        return f.read()


def write_file(path: str, output: str) -> None:
    with safe_open_w(path, "w") as f:
        f.write(output)

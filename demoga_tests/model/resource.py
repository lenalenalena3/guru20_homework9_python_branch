from pathlib import Path


def path(file_name):
    return str(
        Path(f"./tests/attachment/{file_name}").resolve()
    )

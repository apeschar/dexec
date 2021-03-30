import os
import sys
from configparser import ConfigParser
from pathlib import Path


def main():
    config_dir, config_file = find_config_file()

    config = ConfigParser()
    config.read(config_file)

    container = config["dexec"]["container"]
    path = Path(config["dexec"]["path"])
    workdir = path / Path.cwd().relative_to(config_dir)

    user_command = sys.argv[1:]
    options = []

    while user_command[0].startswith("-"):
        option = user_command.pop(0)
        if option == "--":
            break
        options.append(option)

    user = config["dexec"].get("user")
    if user is not None:
        options += ["-u", user]

    command = ["docker", "exec", "-w", str(workdir), *options, container, *user_command]

    os.execvp(command[0], command)


def find_config_file():
    cwd = Path.cwd()
    while not (cwd / ".dexec").exists():
        if cwd == cwd.root:
            raise RuntimeError("Couldn't find .dexec anywhere")
        cwd = cwd.parent
    return cwd, cwd / ".dexec"


if __name__ == "__main__":
    main()

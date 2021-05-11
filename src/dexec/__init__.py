import os
import sys
from configparser import ConfigParser
from pathlib import Path


def main():
    user_command = sys.argv[1:]

    if not user_command:
        print("Usage: %s COMMAND [ARGS ...]" % sys.argv[0], file=sys.stderr)
        sys.exit(1)

    try:
        config_dir, config_file = find_config_file()
    except RuntimeError as e:
        print(e.args[0], file=sys.stderr)
        sys.exit(2)

    config = ConfigParser()
    config.read(config_file)

    container = config["dexec"]["container"]
    path = Path(config["dexec"]["path"])
    workdir = path / Path.cwd().relative_to(config_dir)

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
        if str(cwd) == str(cwd.root):
            raise RuntimeError("Couldn't find .dexec anywhere")
        cwd = cwd.parent
    return cwd, cwd / ".dexec"

from .Commands import about
from .Commands import apps
import json


def Help():
    help_text = {}

    file = open(".\\settings.json", 'r')
    data = json.load(file)

    for i in data['help_command']:
        help_text = i
    file.close()

    for i in help_text:
        if len(i) < 8:
            print(f"{i}\t\t\t{help_text[i]}")
        else:
            print(f"{i}\t\t{help_text[i]}")


def run_command(cmd):
    if cmd == "about":
        about.run()
    elif cmd == "apps":
        apps.run()

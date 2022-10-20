from System_Functions.functions import *
from System_Functions.Commands import var_set
import subprocess
import ctypes
import json
import sys
import os

settings = {}


def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False


def start_system():
    global admin, settings

    system_settings = open("settings.json", 'r')
    data = json.load(system_settings)
    for i in data['system_settings']:
        settings = i
    system_settings.close()

    if is_admin():
        admin = True
        screen()
        system()
    else:
        screen_noadmin()


def screen():
    subprocess.run(f"title Useful Tools Command Prompt [Version: {settings['version']}]", shell=True)
    os.system("cls")
    print(f"Useful Tools Command Prompt \033[34m[Version: {settings['version']}] \033[34m[MODE: ADMIN]\033[0m")
    print("For a list of commands, use 'help' command.\n")


def screen_noadmin():
    subprocess.run(f"title Useful Tools Command Prompt [Version: {settings['version']}]", shell=True)
    os.system("cls")
    print(f"Useful Tools Command Prompt \033[34m[Version: {settings['version']}] \033[31m[MODE: NON-ADMIN]\033[0m")
    print("For a list of commands, use 'help' command.\n")

    cmd = input(
        "\n\033[31m[WARNING] This program is running in NON-ADMIN mode.\nThis can effect some of the commands the system"
        " will try to run.\033[0m\n\nWould you like to enter ADMIN mode for this program?: (y,n) ")
    if cmd.lower() == "y":
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
    else:
        os.system("cls")
        print(f"Useful Tools Command Prompt \033[34m[Version: {settings['version']}] \033[31m[MODE: NON-ADMIN]\033[0m")
        print("For a list of commands, use 'help' command.\n")
        system()


def system():
    while settings['running']:
        current_dir = "C:\\Useful_Tools\\\033[36m" + var_set.var_set("echo %USERNAME%") + "\033[0m"
        command = input(current_dir + ">\033[35m")
        print("\033[0m")
        check_command(command)


def check_command(cmd):
    if cmd.lower() == "":
        return
    elif cmd.lower() == "help":
        Help()
    elif cmd.lower() == "exit":
        exit(0)
    elif cmd.lower() == "reset":
        if is_admin():
            screen()
        else:
            screen_noadmin()
    elif os.path.isfile(f'System_Functions/Commands\\{cmd.lower()}.py'):
        run_command(cmd.lower())
    else:
        print(
            f"\033[31m'{cmd}' is not recognized as an internal or external command,\noperable program or batch file.\033[0m\n")

    print("")


start_system()

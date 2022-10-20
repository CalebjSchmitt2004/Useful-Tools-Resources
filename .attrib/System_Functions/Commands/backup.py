import os
import subprocess
from ..Commands import _format


def run():
    location = input("What Directory would you like to copy?: ")
    print("\n")

    files_list = []
    dirs_list = []
    size = 0
    dir_subs = []

    if location[-1:] != "\\":
        location += "\\"

    if os.path.exists(location):
        print(f"Scanning Directory Tree Tree: {location}")
        for PATH, DIRS, FILES in os.walk(location):
            for file in FILES:
                if "\\".join(PATH.split("\\")[:-1]) not in dirs_list:
                    dirs_list.append("\\".join(PATH.split("\\")[:-1]))
                files_list.append(file)

                if PATH.replace(location, "").split("\\", 1)[0] not in dir_subs:
                    dir_subs.append(PATH.replace(location, "").split("\\", 1)[0])
                    print("├──────── Scanning .\\" + PATH.replace(location, "").split("\\", 1)[0])

                try:
                    fp = os.path.join(PATH, file)
                    size += os.path.getsize(fp)
                except:
                    continue
        total_size = _format._format(size, "con")

        print(f"\nTotal Data to transfer: {total_size}")

        print("\n\nStarting Copy of Data: ")

        new_path = '"' + str(location[:-1]) + '"'

        subprocess.run(
            f"powershell Compress-Archive -Path '{new_path}' -DestinationPath 'C:\\Users\\Caleb Schmitt\\OneDrive\\Documents\\Desktop_Folder\\Projects\\Command Prompt\\{location[9:-1]}.zip'",
            shell=True)

        print("\nFinished Copping Data: ")

    else:
        print("\n\033[31m[ERROR] Directory doesn't exist!")


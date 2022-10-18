to_dir = str(subprocess.run("echo %userprofile%", shell=True, capture_output=True,
                            text=True).stdout).replace("\n", "")

subprocess.run("mkdir .\\Data", shell=True, stdout=subprocess.DEVNULL)

not_important = [".dotnet", ".ms-ad", ".ssh", ".templateengine", "3D Objects", "Contacts", "Favorites", "Links",
                 "Saved Games", "Searches", "AppData", "Application Data", "Cookies", "IntelGraphicsProfiles",
                 "Local Settings", "My Documents", "NetHood", "PrintHood", "Recent", "SendTo", "Start Menu",
                 "Templates", "OneDrive"]

for PATH, DIRS, FILES in os.walk(to_dir):
    for dirs in DIRS:
        if len(PATH.split("\\")) == 3 and dirs not in not_important:
            subprocess.run(f'mkdir ".\\Data\\{dirs}"', shell=True, stdout=subprocess.DEVNULL)
            to_dir = PATH + "\\" + dirs
            print(to_dir)
            subprocess.run(f'robocopy /S  "{to_dir}" ".\\Data\\{dirs}"', shell=True, stdout=subprocess.DEVNULL)

        else:
            continue

subprocess.run("powershell compress-archive .\\Data .\\Data.zip", shell=True)
subprocess.run("rmdir /S /Q .\\Data", shell=True)
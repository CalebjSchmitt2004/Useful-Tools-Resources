size = 0
num_files = 0
total_size = ""
drive_dir = {}

drive_letters = subprocess.run("wmic logicaldisk get name", shell=True, capture_output=True,
                               text=True).stdout.replace("\n", "").replace("Name", "").replace(" ", "").split(":")
if mode == "default":
    for items in drive_letters:
        if items == "":
            continue
        else:
            print(f"Starting Scan on {items}:\\")
            for PATH, DIRS, FILES in os.walk(f"{items}:\\"):
                for files in FILES:
                    if PATH.split("\\")[1] not in drive_dir:
                        drive_dir[PATH.split("\\")[1]] = 0
                        print("├──────── Scanning .\\" + PATH.split("\\")[1])

                    try:
                        fp = os.path.join(PATH, files)
                        drive_dir[PATH.split("\\")[1]] += os.path.getsize(fp)
                        size += os.path.getsize(fp)
                    except:
                        continue
                    num_files += 1

        print(f"\n{items}:\\")
        for dirs in drive_dir:
            value = ""

            if int(drive_dir[dirs]) <= 1_000_000:
                value = str("{:.2f}".format((int(drive_dir[dirs]) / 1024))) + " Kb"
            elif int(drive_dir[dirs]) <= 1_000_000_000:
                value = str("{:.2f}".format(((int(drive_dir[dirs]) / 1024) / 1024))) + " Mb"
            elif int(drive_dir[dirs]) <= 1_000_000_000_000:
                value = str("{:.2f}".format((((int(drive_dir[dirs]) / 1024) / 1024) / 1024))) + " Gb"
            elif int(drive_dir[dirs]) <= 1_000_000_000_000_000:
                value = str("{:.2f}".format(((((int(drive_dir[dirs]) / 1024) / 1024) / 1024) / 1024))) + " Tb"

            if dirs == "":
                print(f"├──────── .\\ \t\t\tFolder Size: {value}")
                continue
            if len(dirs) < 5:
                print(f"├──────── {dirs} \t\t\tFolder Size: {value}")
            elif len(dirs) < 13:
                print(f"├──────── {dirs} \t\tFolder Size: {value}")
            else:
                print(f"├──────── {dirs} \tFolder Size: {value}")

        if size <= 1_000_000:
            total_size = "{:.2f}".format((int(size) / 1024)) + " Kb"
        elif size <= 1_000_000_000:
            total_size = "{:.2f}".format(((int(size) / 1024) / 1024)) + " Mb"
        elif size <= 1_000_000_000_000:
            total_size = "{:.2f}".format((((int(size) / 1024) / 1024) / 1024)) + " Gb"
        elif size <= 1_000_000_000_000_000:
            total_size = "{:.2f}".format(((((int(size) / 1024) / 1024) / 1024) / 1024)) + " Tb"

        num_files = "{:,}".format(num_files)

        print(f"\nTotal Files on {items}:\\ : {num_files} Files")
        print(f"Total Size on {items}:\\ : {total_size}")

if mode == "-d":
    for items in drive_letters:
        if items == "":
            continue
        else:
            print(f"Starting Scan on {items}:\\")
            for PATH, DIRS, FILES in os.walk(f"{items}:\\"):
                for files in FILES:
                    if PATH.split("\\")[1] not in drive_dir:
                        drive_dir[PATH.split("\\")[1]] = 0

                    if "\\".join(PATH.split("\\", -1)) != path:
                        path = "\\".join(PATH.split("\\", -1))
                        print("\\".join(PATH.split("\\", -1)))

                    try:
                        fp = os.path.join(PATH, files)
                        drive_dir[PATH.split("\\")[1]] += os.path.getsize(fp)
                        size += os.path.getsize(fp)
                    except:
                        continue
                    num_files += 1

        print(f"\n{items}:\\")
        for dirs in drive_dir:
            value = ""

            if int(drive_dir[dirs]) <= 1_000_000:
                value = str("{:.2f}".format((int(drive_dir[dirs]) / 1024))) + " Kb"
            elif int(drive_dir[dirs]) <= 1_000_000_000:
                value = str("{:.2f}".format(((int(drive_dir[dirs]) / 1024) / 1024))) + " Mb"
            elif int(drive_dir[dirs]) <= 1_000_000_000_000:
                value = str("{:.2f}".format((((int(drive_dir[dirs]) / 1024) / 1024) / 1024))) + " Gb"
            elif int(drive_dir[dirs]) <= 1_000_000_000_000_000:
                value = str("{:.2f}".format(((((int(drive_dir[dirs]) / 1024) / 1024) / 1024) / 1024))) + " Tb"

            if dirs == "":
                print(f"├──────── .\\ \t\t\tFolder Size: {value}")
                continue
            if len(dirs) < 5:
                print(f"├──────── {dirs} \t\t\tFolder Size: {value}")
            elif len(dirs) < 13:
                print(f"├──────── {dirs} \t\tFolder Size: {value}")
            else:
                print(f"├──────── {dirs} \tFolder Size: {value}")

        if size <= 1_000_000:
            total_size = "{:.2f}".format((int(size) / 1024)) + " Kb"
        elif size <= 1_000_000_000:
            total_size = "{:.2f}".format(((int(size) / 1024) / 1024)) + " Mb"
        elif size <= 1_000_000_000_000:
            total_size = "{:.2f}".format((((int(size) / 1024) / 1024) / 1024)) + " Gb"
        elif size <= 1_000_000_000_000_000:
            total_size = "{:.2f}".format(((((int(size) / 1024) / 1024) / 1024) / 1024)) + " Tb"

        num_files = "{:,}".format(num_files)

        print(f"\nTotal Files on {items}:\\ : {num_files} Files")
        print(f"Total Size on {items}:\\ : {total_size}")

if mode == "-f":
    for items in drive_letters:
        if items == "":
            continue
        else:
            print(f"Starting Scan on {items}:\\")
            for PATH, DIRS, FILES in os.walk(f"{items}:\\"):
                for files in FILES:
                    if PATH.split("\\")[1] not in drive_dir:
                        drive_dir[PATH.split("\\")[1]] = 0

                    print(f"{PATH}\\{files}")

                    try:
                        fp = os.path.join(PATH, files)
                        drive_dir[PATH.split("\\")[1]] += os.path.getsize(fp)
                        size += os.path.getsize(fp)
                    except:
                        continue
                    num_files += 1

        print(f"\n{items}:\\")
        for dirs in drive_dir:
            value = ""

            if int(drive_dir[dirs]) <= 1_000_000:
                value = str("{:.2f}".format((int(drive_dir[dirs]) / 1024))) + " Kb"
            elif int(drive_dir[dirs]) <= 1_000_000_000:
                value = str("{:.2f}".format(((int(drive_dir[dirs]) / 1024) / 1024))) + " Mb"
            elif int(drive_dir[dirs]) <= 1_000_000_000_000:
                value = str("{:.2f}".format((((int(drive_dir[dirs]) / 1024) / 1024) / 1024))) + " Gb"
            elif int(drive_dir[dirs]) <= 1_000_000_000_000_000:
                value = str("{:.2f}".format(((((int(drive_dir[dirs]) / 1024) / 1024) / 1024) / 1024))) + " Tb"

            if dirs == "":
                print(f"├──────── .\\ \t\t\tFolder Size: {value}")
                continue
            if len(dirs) < 5:
                print(f"├──────── {dirs} \t\t\tFolder Size: {value}")
            elif len(dirs) < 13:
                print(f"├──────── {dirs} \t\tFolder Size: {value}")
            else:
                print(f"├──────── {dirs} \tFolder Size: {value}")

        if size <= 1_000_000:
            total_size = "{:.2f}".format((int(size) / 1024)) + " Kb"
        elif size <= 1_000_000_000:
            total_size = "{:.2f}".format(((int(size) / 1024) / 1024)) + " Mb"
        elif size <= 1_000_000_000_000:
            total_size = "{:.2f}".format((((int(size) / 1024) / 1024) / 1024)) + " Gb"
        elif size <= 1_000_000_000_000_000:
            total_size = "{:.2f}".format(((((int(size) / 1024) / 1024) / 1024) / 1024)) + " Tb"

        num_files = "{:,}".format(num_files)

        print(f"\nTotal Files on {items}:\\ : {num_files} Files")
        print(f"Total Size on {items}:\\ : {total_size}")

print("\n")

import subprocess

if not repair_action:
    subprocess.run("defrag C: /A /O", shell=True)
    print("\n")
else:
    subprocess.run("defrag C: /A /O > disk.txt", shell=True)
    file = open("disk.txt", 'r')
    for line in file:
        if "The operation completed successfully." in line:
            repair_report[2] = True
    file.close()
    subprocess.run("del disk.txt", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

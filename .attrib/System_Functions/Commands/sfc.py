if not repair_action:
    subprocess.run("sfc /scannow", shell=True)
    print("\n")
else:
    subprocess.run("sfc /scannow > sfc.txt", shell=True)
    if admin:
        repair_report[1] = True
    subprocess.run("del sfc.txt", shell=True, stderr=subprocess.DEVNULL, stdout=subprocess.DEVNULL)
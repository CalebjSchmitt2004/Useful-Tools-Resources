if not repair_action:
    subprocess.run('dism /online /cleanup-image /restorehealth', shell=True)
    print("\n")
else:
    subprocess.run('dism /online /cleanup-image /restorehealth > dism.txt', shell=True)
    file = open("dism.txt", 'r')
    for line in file:
        line = line.replace("\n", "").replace(" ", "").replace("DeploymentImageServicingandManagementtool",
                                                               "").replace("Version:10.0.19041.844", "").replace(
            "ImageVersion:10.0.19044.2006", "").replace("[", "").replace("]", "").replace("=", "").replace("%", "")
        try:
            if float(line):
                continue
        except:
            if "Therestoreoperationcompletedsuccessfully." in line:
                repair_report[0][0] = True
            if "Theoperationcompletedsuccessfully." in line:
                repair_report[0][1] = True
    file.close()
    subprocess.run("del dism.txt", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

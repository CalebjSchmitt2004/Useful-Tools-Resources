System = []
Good = []
Flags = []
Bad = []
Unknown = []

amount_system = 0
amount_good = 0
amount_flags = 0
amount_bad = 0
amount_unknown = 0
amount = 0

subprocess.run("tasklist > tasklist.txt", shell=True, stderr=subprocess.DEVNULL, stdout=subprocess.DEVNULL)
subprocess.run("type null > report.txt", shell=True, stderr=subprocess.DEVNULL, stdout=subprocess.DEVNULL)
file = open("tasklist.txt", 'r')
file2 = open("report.txt", 'w')
for i in file:
    i = i.replace("\n", "")[:29].replace(" ", "").replace("ImageName", "").replace("=", "")

    if i == "":
        continue
    if i in Microsoft_System:
        if i in System:
            continue
        else:
            amount_system += 1
            System.append(i)
    elif i in Known_Good:
        if i in Good:
            continue
        else:
            amount_good += 1
            Good.append(i)
    elif i in Known_Flags:
        if i in Flags:
            continue
        else:
            amount_flags += 1
            Flags.append(i)
    elif i in Known_Bad:
        if i in Bad:
            continue
        else:
            amount_bad += 1
            Bad.append(i)
    else:
        if i in Unknown:
            continue
        else:
            Unknown.append(i)
            amount_unknown += 1
            file2.write(f"'{i}'\n")
    amount += 1
file.close()
subprocess.run("del tasklist.txt", shell=True)
file2.close()

if len(Unknown) == 0:
    subprocess.run("del report.txt", shell=True)

if not repair_action:
    print("Tasklist Report: ")
    if len(Flags) > 0:
        print("\nFlagged Processes: ")
        for i in range(len(Flags)):
            if len(Flags[i]) < 14:
                print(f"[{i}] Running Process Name: {Flags[i]}\t\tPercent Dangerous: {str(Known_Flags[Flags[i]])}%")
            else:
                print(f"[{i}] Running Process Name: {Flags[i]}\tPercent Dangerous: {str(Known_Flags[Flags[i]])}%")
    if len(Bad) > 0:
        print("\nMalicious Running Processes: ")
        for i in range(len(Bad)):
            print(f"[{i}] Running Process Name: {Bad[i]}")
    if len(Unknown) > 0:
        print("\nUnknown Running Processes: ")
        for i in range(len(Unknown)):
            print(f"[{i}] Unknown Process Name: {Unknown[i]}")
        computer_name = subprocess.run("hostname", shell=True, capture_output=True, text=True).stdout.replace("\n",
                                                                                                              "") + ".txt"
        subprocess.run("mkdir Reports", shell=True, stderr=subprocess.DEVNULL, stdout=subprocess.DEVNULL)
        subprocess.run(f'rename report.txt "{computer_name}"', shell=True, stdout=subprocess.DEVNULL,
                       stderr=subprocess.DEVNULL)
        subprocess.run(f'move ".\\{computer_name}" ".\\Reports\\{computer_name}"', shell=True,
                       stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print(f"\n\nCurrent Running Processes: {amount}")
    print(f"Processes Flagged: {amount_flags}")
    print(f"Processes Marked Malicious: {amount_bad}")
    print(f"Processes Marked Safe: {amount_good + amount_system}")
    print(f"Unknown Running Processes: {amount_unknown}\n")

    if len(Flags) > 0:
        command = input(
            "\033[33m[ALERT] Processes have been marked as flagged. Would you like to cancel these processes?: \033[0m")
        if command.lower() == "y" or command.lower() == "yes":
            for item in Flags:
                subprocess.run(f"taskkill /IM {item} /F", shell=True, stderr=subprocess.DEVNULL,
                               stdout=subprocess.DEVNULL)
    if len(Bad) > 0:
        for i in range(6):
            print(
                f"\r\033[31m[WARNING] Some Processes have been marked as malicious. System will terminate these process in {5 - i} seconds.\033[0m",
                end="\r")
            sleep(1)
        for item in Bad:
            subprocess.run(f"taskkill /IM {item} /F", shell=True, stderr=subprocess.DEVNULL,
                           stdout=subprocess.DEVNULL)
    print("\n")
else:
    tasklist.append(amount)
    tasklist.append(amount_flags)
    tasklist.append(amount_bad)
    tasklist.append(amount_good + amount_system)
    tasklist.append(amount_unknown)
    if len(Unknown) > 0:
        computer_name = subprocess.run("hostname", shell=True, capture_output=True, text=True).stdout.replace("\n",
                                                                                                              "") + ".txt"
        subprocess.run("mkdir Reports", shell=True, stderr=subprocess.DEVNULL, stdout=subprocess.DEVNULL)
        subprocess.run(f'rename report.txt "{computer_name}"', shell=True, stdout=subprocess.DEVNULL,
                       stderr=subprocess.DEVNULL)
        subprocess.run(f'move ".\\{computer_name}" ".\\Reports\\{computer_name}"', shell=True,
                       stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    repair_report[4] = True


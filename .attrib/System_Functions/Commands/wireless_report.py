subprocess.run("netsh wlan show profiles > wireless.txt", shell=True)
file = open("wireless.txt", 'r')
for line in file:
    line = line.replace("\n", "").replace("\t", "").replace("    All User Profile     : ", "").replace(
        "Profiles on interface Wi-Fi:", "").replace("Group policy profiles (read only)", "").replace(
        "---------------------------------", "").replace("<None>", "").replace("User profiles", "").replace(
        "-------------", "")
    if line != "":
        password = subprocess.run(f'netsh wlan show profiles {line} key=clear | findstr "Key Content"', shell=True,
                                  capture_output=True, text=True).stdout.replace("Key Content            :",
                                                                                 "").replace("\n", "").replace(" ",
                                                                                                               "",
                                                                                                               4)
        if "Key Index" in password or password == "":
            continue
        if len(line) < 8:
            print(f"Wireless Network Name: {line} \t\t\tPassword: {password}")
        elif len(line) < 14:
            print(f"Wireless Network Name: {line} \t\tPassword: {password}")
        else:
            print(f"Wireless Network Name: {line} \tPassword: {password}")
print("\n")
file.close()
subprocess.run("del wireless.txt", shell=True, stderr=subprocess.DEVNULL, stdout=subprocess.DEVNULL)

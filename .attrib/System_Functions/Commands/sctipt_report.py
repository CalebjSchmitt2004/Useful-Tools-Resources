unknown = []

os.system("cls")
print("Script Report: ")

if os.path.exists("Reports"):
    for PATH, DIRS, FILES in os.walk("Reports"):
        for file in FILES:
            file = open("Reports\\" + file, 'r')
            for lines in file:
                line = lines.replace("\n", "").replace("'", "")
                if line not in unknown:
                    unknown.append(line)

subprocess.run("type null > unknown_tasks.txt", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
file = open("unknown_tasks.txt", 'w')
for items in unknown:
    file.write(f"'{items}'\n")
file.close()

print(f"\nUnknown Process Found: {len(unknown)}")
input("\nPress enter to continue ...")
screen()
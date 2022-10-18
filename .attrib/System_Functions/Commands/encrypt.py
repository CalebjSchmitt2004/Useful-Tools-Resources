path2 = ('"' + str(input("Path: ")) + '"')
subprocess.run(f"cipher /E /W {path2}", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

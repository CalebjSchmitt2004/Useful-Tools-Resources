import subprocess

path1 = ('"' + str(input("Path: ")) + '"')
subprocess.run(f"cipher /D /W {path1}", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

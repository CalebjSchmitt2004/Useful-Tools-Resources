subprocess.run('ipconfig /all | findstr "IPv4" > ipv4.txt', shell=True, capture_output=True, text=True)
subprocess.run('ipconfig /all | findstr "Mask" > mask.txt', shell=True, capture_output=True, text=True)
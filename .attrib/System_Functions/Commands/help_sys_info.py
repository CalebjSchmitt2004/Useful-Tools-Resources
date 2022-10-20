print("System Information (Commands to run)")

li = {
    "Computer Name": "hostname",
    "Current User": "echo %username%",
    "Home Directory": "echo '%USERPROFILE%'",
    "Last Login": 'net user "%USERNAME%"| findstr "Last"',
    "CPU": "\twmic cpu get name",
    "RAM": "\twmic memorychip get Capacity",
    "Computer Model": "wmic computersystem get SystemFamily",
    "Serial Number": "wmic bios get SerialNumber",
    "Operating System": "wmic os get name",
    "Product Key": "wmic path softwarelicensingservice get OA3xOriginalProductKey",
    "Boot Drive": "wmic diskdrive get model",
    "Drive Size": "wmic diskdrive get size",
    "Wifi Connection Name": 'netsh WLAN show interfaces | findstr "Profile"',
    "Wifi Password": 'netsh wlan show profiles <wifi_name> key=clear | findstr "Key Content"',
    "Device IP Address": 'ipconfig | findstr "IPv4 Address"'
}

for i in li:
    if len(i) < 4:
        print(i + ": \t\t" + li[i])
    elif len(i) < 14:
        print(i + ": \t\t" + li[i])
    else:
        print(i + ": \t" + li[i])
print("\n")

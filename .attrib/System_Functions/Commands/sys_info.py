wifi_name = str(
    var_set('Netsh WLAN show interfaces | findstr "Profile"').replace(" ", "", 21).replace(":", "").replace(
        "Profile", "").replace("Connectionmode", ""))
info = {
    "Computer Name": var_set("hostname"),
    "Current User": var_set("echo %username%"),
    "Home Directory": var_set("echo '%USERPROFILE%'"),
    "Last Login": var_set('net user "%USERNAME%"| findstr "Last"').replace("Last logon", "").replace(" ", "", 19),
    "CPU": var_set("wmic cpu get name").replace(" ", "", 36).replace("Name", ""),
    "RAM": "\t" + str(((int(var_set("wmic memorychip get Capacity").replace(" ", "").replace("Capacity",
                                                                                             "")) / 1024) / 1024) / 1024)[
                  :2] + " Gb",
    "Computer Model": var_set("wmic computersystem get SystemFamily").replace("SystemFamily", "").replace(" ", "",
                                                                                                          8),
    "Serial Number": var_set("wmic bios get SerialNumber").replace("SerialNumber", "").replace(" ", "", 2),
    "Operating System": var_set("wmic os get name").replace("Name", "").replace(" ", "", 62).split("|")[0],
    "Product Key": var_set("wmic path softwarelicensingservice get OA3xOriginalProductKey").replace(
        "OA3xOriginalProductKey", "").replace(" ", "", 9),
    "Boot Drive": str(
        var_set("wmic DISKDRIVE get model").replace(" ", "", 30).replace("Model", "").split(" ", 1)[0]),
    "Drive Size": str(int(((int(
        var_set("wmic diskdrive get size").replace(" ", "", 10).replace("Size", "").split(" ", 1)[
            0]) / 1000) / 1000) / 1000)) + " Gb",
    "Wifi Connection Name": wifi_name,
    "Wifi Password": var_set(
        "netsh wlan show profiles " + wifi_name + ' key=clear | findstr "Key Content"').replace("Key Content",
                                                                                                "").replace(" ", "",
                                                                                                            17).replace(
        ":", ""),
    "Device IP Address":
        var_set("wmic nicconfig get IPAddress").replace(" ", "", 250).replace("IPAddress", "").split(" ", 1)[
            0].replace('{"', "").split('"', 1)[0]
}

print("System Information")
for items in info:
    if len(items) < 4:
        print(items + ": \t\t" + info[items])
    elif len(items) < 14:
        print(items + ": \t\t" + info[items])
    else:
        print(items + ": \t" + info[items])
print("\n")

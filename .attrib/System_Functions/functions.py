from .Commands import about
from .Commands import apps
from .Commands import backup
from .Commands import battery_health
from .Commands import clear
#from .Commands import data_grab
#from .Commands import decrypt
#from .Commands import disk_cleanup
#from .Commands import disk_defrag
#from .Commands import disk_report
#from .Commands import dism
#from .Commands import drivers
#from .Commands import encrypt
#from .Commands import help_sys_info
#from .Commands import network_scan
#from .Commands import num_test
#from .Commands import sctipt_report
#from .Commands import sfc
from .Commands import sys_info
#from .Commands import tasklist
from .Commands import tree
from .Commands import wireless_report
import json


def Help():
    help_text = {}

    file = open(".\\settings.json", 'r')
    data = json.load(file)

    for i in data['help_command']:
        help_text = i
    file.close()

    for i in help_text:
        if len(i) < 8:
            print(f"{i}\t\t\t{help_text[i]}")
        else:
            print(f"{i}\t\t{help_text[i]}")


def run_command(cmd):
    if cmd == "about":
        about.run()
    elif cmd == "apps":
        apps.run()
    elif cmd == "backup":
        backup.run()
    elif cmd == "battery_health":
        battery_health.run()
    elif cmd == "clear":
        clear.run()
    elif cmd == "sys_info":
        sys_info.run()
    elif cmd == "tree":
        tree.run()
    elif cmd == "wireless_report":
        wireless_report.run()

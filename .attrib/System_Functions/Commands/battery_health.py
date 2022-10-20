import subprocess


def run():
    subprocess.run("powercfg/energy", shell=True)
    subprocess.run("start C:\\Windows\\System32\\energy-report.html", shell=True)
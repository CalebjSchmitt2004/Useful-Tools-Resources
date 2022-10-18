import subprocess


def run():
    subprocess.run("wmic product get name", shell=True)
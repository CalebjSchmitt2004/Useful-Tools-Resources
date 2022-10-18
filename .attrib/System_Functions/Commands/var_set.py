import subprocess


def var_set(cmd):
    return subprocess.run(cmd, shell=True, capture_output=True, text=True).stdout.replace("\n", "")

def _format(num, mode):
    if mode == "dec":
        return "{:.2f}".format(num)
    elif mode == "com":
        return "{:,}".format(num)

    elif mode == "con":
        if num <= 1_000_000:
            return "{:.2f}".format((int(num) / 1024)) + " Kb"
        elif num <= 1_000_000_000:
            return "{:.2f}".format(((int(num) / 1024) / 1024)) + " Mb"
        elif num <= 1_000_000_000_000:
            return "{:.2f}".format((((int(num) / 1024) / 1024) / 1024)) + " Gb"
        elif num <= 1_000_000_000_000_000:
            return "{:.2f}".format(((((int(num) / 1024) / 1024) / 1024) / 1024)) + " Tb"
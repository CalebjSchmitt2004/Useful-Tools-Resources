start = [(datetime.datetime.now()).hour % 12, (datetime.datetime.now()).minute,
         (datetime.datetime.now()).second]
i = 0
number_set = 1_000_000
goal = 0
level = str(input("Enter a test level: (low, mid, high) ")).lower()

if level == "low":
    goal += 100_000_000
elif level == "mid":
    goal += 1_000_000_000
elif level == "high":
    goal += 10_000_000_000
else:
    goal += 10_000_000

while True:
    i += 1
    if i % number_set == 0:
        number_set += 1_000_000
        print("\rPercent Complete: " + ("{:.0%}".format((i / goal))), end="")
    if i == goal:
        break

end = [(datetime.datetime.now()).hour % 12, (datetime.datetime.now()).minute, (datetime.datetime.now()).second]

print(
    f"\n\nStart Time: \t(H:{start[0]} M:{start[1]} S:{start[2]})\nEnd Time: \t(H:{end[0]} M:{end[1]} S:{end[2]})")

srt_secs = ((start[0] * 60) * 60) + start[1] * 60 + start[2]
stp_secs = ((end[0] * 60) * 60) + end[1] * 60 + end[2]

time = [0, 0, 0]

if stp_secs - srt_secs >= 60:
    time[1] = (stp_secs - srt_secs) // 60
    time[2] = (stp_secs - srt_secs) % 60
else:
    time[2] = stp_secs - srt_secs

if time[1] >= 60:
    time[0] = time[1] // 60
    time[1] = time[1] % 60

print(f"Difference: \t(H:{time[0]} M:{time[1]} S:{time[2]})")

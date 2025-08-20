#Task 8

num = 60

def to_hrs_mins(num):
    hrs = num // 60
    mins = num % 60
    
    # if hrs > 1 and mins > 1:
    #     print(f"{hrs} hours, {mins} minutes")
    # elif hrs > 1 and mins == 1:
    #     print(f"{hrs} hours, {mins} minute")
    # elif hrs == 1 and mins > 1:
    #     print(f"{hrs} hour, {mins} minutes")
    # elif hrs == 0 and mins == 1:
    #     print(f"{mins} minute")
    # elif hrs == 1 and mins == 0:
    #     print(f"{hrs} hour")
    # elif hrs == 0 and mins > 1:
    #     print(f"{mins} minutes")
    # elif hrs > 1 and mins == 0:
    #     print(f"{hrs} hours")
    # else:
    #     print(f"{hrs} hour, {mins} minute")

    hrs_label = "hour" if hrs == 1 else "hours"
    mins_label = "minutes" if mins == 1 else "minutes"

    if hrs > 0 and mins > 0:
        print(f"{hrs} {hrs_label}, {mins} {mins_label}")
    elif hrs > 0:
        print(f"{hrs} {hrs_label}")
    else:
        print(f"{mins} {mins_label}")

to_hrs_mins(num)
    
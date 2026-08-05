# write a program to print 24 hours of day with suitable suffixes AM, PM, Noon, Midnight.

for hour in range(24):

    if hour == 0:
        print("12:00 Midnight")

    elif hour < 12:
        print(f"{hour}:00 AM")

    elif hour == 12:
        print("12:00 Noon")

    else:
        print(f"{hour - 12}:00 PM")
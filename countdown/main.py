import time

def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        time = '{:02d}:{:02d}'.format(mins, secs)
        print(time, end="\r")
        time.sleep(1)
        t -= 1

    Print('Complete!')

t = input('Enter the time in seconds: ')

countdown(int(t))
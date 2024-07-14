import ctypes, time, winsound

gap = 300
snooze = 900
Quit = 0


def Mbox(title, text, style):
    return ctypes.windll.user32.MessageBoxW(0, text, title, style)

while Quit == 0:
    winsound.MessageBeep()
    result = Mbox('Revise', 'You should revise. Press "YES" to revise or "NO" to snooze.', 4)

    if result != 6:
        #print("SNOOZE")
        time.sleep(snooze)
        gap = gap/2
        snooze = snooze/2

    else:
        #print("REVISE")
        revise_remain = 500

        while revise_remain > 0:
            winsound.MessageBeep()
            Mbox('Revise', 'You should be revising.', 0)

quit()
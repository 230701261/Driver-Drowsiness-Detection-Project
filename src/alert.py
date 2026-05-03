import platform

if platform.system() == "Windows":
    import winsound

def mild_alert():
    try: winsound.Beep(800, 200)
    except: pass

def warning_alert():
    try: winsound.Beep(1000, 500)
    except: pass

def critical_alert():
    try:
        for _ in range(3):
            winsound.Beep(1500, 300)
    except: pass
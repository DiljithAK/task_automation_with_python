import os
import time
import psutil
import tkinter as tk
from datetime import datetime, timedelta

shutdown_hour = 21
shutdown_minute = 34

idle_threshold = 60
popup_display_time = 30  # Time to wait with the popup open in seconds

def get_idle_time():
    if os.name == 'nt':
        import ctypes
        class LASTINPUTINFO(ctypes.Structure):
            _fields_ = [("cbSize", ctypes.c_uint), ("dwTime", ctypes.c_uint)]
        
        lii = LASTINPUTINFO()
        lii.cbSize = ctypes.sizeof(LASTINPUTINFO)
        ctypes.windll.user32.GetLastInputInfo(ctypes.byref(lii))
        millis = ctypes.windll.kernel32.GetTickCount() - lii.dwTime
        return millis / 1000.0
    else:  # Unix-like (Linux, MacOS)
        idle_time = time.time() - psutil.boot_time()
        return idle_time

def show_warning():
    def cancel_shutdown():
        global shutdown_canceled
        shutdown_canceled = True
        root.destroy()

    def check_idle_time():
        idle_time = get_idle_time()
        if idle_time < idle_threshold:
            global shutdown_canceled
            shutdown_canceled = True
            root.destroy()

    global root
    root = tk.Tk()
    root.title("Shutdown Warning")
    label = tk.Label(root, text="System will shut down in 30 seconds. Click 'Cancel Shutdown' to prevent this.")
    label.pack(padx=40, pady=20)
    button = tk.Button(root, text="Cancel Shutdown", command=cancel_shutdown)
    button.pack(pady=10)
    
    # Schedule the check for idle time every second
    def check_activity():
        check_idle_time()
        if not shutdown_canceled:
            root.after(1000, check_activity)
    
    root.after(1000, check_activity)
    
    # Schedule the shutdown after 30 seconds if not canceled
    root.after(popup_display_time * 1000, lambda: root.quit() if not shutdown_canceled else None)
    
    root.mainloop()

def main():
    global shutdown_canceled
    shutdown_canceled = False

    while True:
        # Get current time
        now = datetime.now()

        # Calculate the shutdown time
        shutdown_time = datetime(now.year, now.month, now.day, shutdown_hour, shutdown_minute)

        # Check if current time is past shutdown time
        if now >= shutdown_time:
            # Get system idle time
            idle_time = get_idle_time()
            print(f"Idle Time: {idle_time}")

            # Check if idle time exceeds the threshold
            if idle_time >= idle_threshold:
                if not shutdown_canceled:
                    show_warning()

                    idle_time = get_idle_time()
                    print(f"Idle Time after warning: {idle_time}")
                    if not shutdown_canceled and idle_time >= idle_threshold:
                        # Shut down the system
                        print("Shutting down the system due to inactivity after 9:34 PM...")
                        if os.name == 'nt':  # Windows
                            os.system("shutdown /s /t 1")
                        else:  # Unix-like (Linux, MacOS)
                            os.system("sudo shutdown now")
                        break
                else:
                    shutdown_canceled = False
        
        # Sleep for a while before checking again
        time.sleep(15)  # Check every 15 seconds

if __name__ == '__main__':
    main()

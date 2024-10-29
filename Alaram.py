import time
import datetime as dt
from playsound import playsound
import os
import threading
def Alarm_sound():
    playsound(r"audio.mp3")
def Alarm():
    hours=int(input("Enter the Hours 12"))
    minutes=int(input("Enter the Minutes"))
    day=input("defalut am , if you want enter pm")
    if day=="pm":
        hours+=12
    while True:
        if hours == dt.datetime.now().hour and minutes == dt.datetime.now().minute:
            print("Tring...")
            sound=threading.Thread(target=Alarm_sound)
            sound.start()
            time.sleep(10)
            os._exit(0)  # Exit the program
Alarm()

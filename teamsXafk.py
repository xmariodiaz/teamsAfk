from pickle import FALSE
from infi.systray import SysTrayIcon
import asyncio
#mario


import keyboard, time
from datetime import datetime
def about(systray):
    print("AFK - Mario - teams")

async def main():
        menu_options = (("About", None, about),)
        systray = SysTrayIcon("tafk.ico", "TeamsX", menu_options)
        systray.start()
        sleeptime = 5*60
        while True:
            if not datetime.today().weekday() in [5, 6]: # Working days
                if int(datetime.now().strftime("%H")) in [6,7,8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]: # Working hours
                    keyboard.send("F13")
                    print("Doing my shit!!...")
                    time.sleep(sleeptime)
                else:
                    print("Non working time!\Wait for 1 hour")
                    time.sleep(3600)
            else:
                print("Weekend!\nWait for 2 hours")
                time.sleep(2*3600) # Sleep for 1 hour

if __name__ == "__main__":
    asyncio.run(main())

if __name__ == "__main__":
    asyncio.run(main())

import time
from plyer import notification


if __name__ == '__main__':
    # while True:
        notification.notify(
            title = "Please Drink Water",
            message = "Keeping a water bottle handy can also serve as a visual reminder to drink more water.",
            app_icon = "E:\\Drink Water Notifications\\icon.ico",
            timeout=10
         
    )
        # time.sleep(60*60)
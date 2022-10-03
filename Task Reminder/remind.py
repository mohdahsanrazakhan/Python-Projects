import time
from plyer import notification

if __name__ == "__main__":
    while True:
        notification.notify(
            title="Reminder!!!",
            message="Write your message here...",
            app_icon="D:\Project\Task Reminder\icon.ico",
            timeout=30
        )
        # Reminder frequency is every hour
        time.sleep(60*60)

# Note: Execute this program in your terminal by using 'pythonw remind.py'

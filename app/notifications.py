import time
from datetime import datetime

from plyer import notification


class PrayerNotifications:
    def __init__(self, prayer_times, logger, notification_interval=5):
        """
        Initialize the prayer notifications.

        Args:
            prayer_times (dict): Dictionary with prayer times (in HH:MM format).
            logger (Logger): Logger object to log messages.
            notification_interval (int): Interval in minutes to check for upcoming prayers.
        """
        self.prayer_times = prayer_times
        self.logger = logger
        self.notification_interval = notification_interval

    @staticmethod
    def send_notification(prayer, time_of_prayer):
        """
        Send a desktop notification for the prayer time.

        Params:
            prayer (str): Name of the prayer.
            time_of_prayer (str): Time of the prayer in HH:MM format.
        """
        notification.notify(
            title=f'ime for {prayer}',
            message=f'It is time for {prayer} prayer. The time is {time_of_prayer}.',
            timeout=10  # Notification will appear for 10 seconds
        )

    def get_next_prayer_time(self):
        """
        Get the next prayer time after the current time.
        """
        current_time = datetime.now().strftime('%H:%M')
        for prayer, time_ in self.prayer_times.items():
            if time_ > current_time:
                return prayer, time_
        return None, None

    def start_notifications(self):
        """
        Start the notification loop to remind the user of upcoming prayers.
        """
        while True:
            next_prayer, next_prayer_time = self.get_next_prayer_time()
            if next_prayer:
                current_time = datetime.now().strftime('%H:%M')
                current_time_dt = datetime.strptime(current_time, '%H:%M')
                next_prayer_time_dt = datetime.strptime(next_prayer_time, '%H:%M')
                time_difference = next_prayer_time_dt - current_time_dt
                self.logger.info(f'Next prayer: {next_prayer} at {next_prayer_time} in {time_difference}')
                time_to_wait = self.calculate_wait_time(next_prayer_time)
                time.sleep(time_to_wait * 60)  # Wait until the prayer time
                self.send_notification(next_prayer, next_prayer_time)
            else:
                self.logger.info('No more prayers today.')
                break

            time.sleep(self.notification_interval * 60)  # Check again after the interval

    @staticmethod
    def calculate_wait_time(prayer_time):
        """
        Calculate the wait time in minutes until the next prayer.
        """
        current_time = datetime.now().strftime('%H:%M')
        current_hour, current_minute = map(int, current_time.split(":"))
        prayer_hour, prayer_minute = map(int, prayer_time.split(":"))

        # Calculate the difference in minutes
        wait_time = (prayer_hour * 60 + prayer_minute) - (current_hour * 60 + current_minute)

        return max(wait_time, 0)
